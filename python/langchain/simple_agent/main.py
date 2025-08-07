"""
Dual-Agent Chatbot with Message Classification

This module implements a chatbot system that classifies user messages as either
emotional or logical, then routes them to specialized agent responses.
"""

import os
from dotenv import load_dotenv
from typing import Annotated, Literal
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from typing_extensions import TypedDict

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI language model
llm = ChatOpenAI(
    model="gpt-4o-mini",            # Use a lightweight GPT-4 model
    temperature=0,                  # Deterministic output (no randomness)
    api_key=os.environ["OPEN_AI_SECRET_KEY"]  # Pull your OpenAI key from environment
)


class MessageClassifier(BaseModel):
    """
    Pydantic model for structured output of message classification.
    
    Attributes
    ----------
    message_type : Literal["emotional", "logical"]
        The classification of the message type, either "emotional" for messages
        requiring empathetic responses or "logical" for factual inquiries.
    """
    message_type: Literal["emotional", "logical"] = Field(
        ...,
        description="Classify if the message requires an emotional (therapist) or logical response."
    )


class State(TypedDict):
    """
    TypedDict defining the state structure for the conversation graph.
    
    Attributes
    ----------
    messages : Annotated[list, add_messages]
        List of conversation messages with automatic message addition functionality.
    message_type : str | None
        The classified type of the current message, either "emotional", "logical", or None.
    """
    messages: Annotated[list, add_messages]
    message_type: str | None


def classify_message(state: State):
    """
    Classify a user message as emotional or logical using structured LLM output.
    
    This function takes the last message in the conversation state and uses
    a language model with structured output to classify whether the message
    requires an emotional (therapist-style) or logical (factual) response.
    
    Parameters
    ----------
    state : State
        The current conversation state containing messages and message type.
        
    Returns
    -------
    dict
        Dictionary containing the classified message_type ("emotional" or "logical").
        
    Examples
    --------
    >>> state = {"messages": [{"content": "I'm feeling sad"}], "message_type": None}
    >>> result = classify_message(state)
    >>> result["message_type"]
    "emotional"
    """
    last_message = state["messages"][-1]
    classifier_llm = llm.with_structured_output(MessageClassifier)

    result = classifier_llm.invoke([
        {
            "role": "system",
            "content": """Classify the user message as either:
            - 'emotional': if it asks for emotional support, therapy, deals with feelings, or personal problems
            - 'logical': if it asks for facts, information, logical analysis, or practical solutions
            """
        },
        {"role": "user", "content": last_message.content}
    ])
    return {"message_type": result.message_type}


def router(state: State):
    """
    Route the conversation to the appropriate agent based on message classification.
    
    This function determines which agent (therapist or logical) should handle
    the user's message based on the previously classified message type.
    
    Parameters
    ----------
    state : State
        The current conversation state containing the classified message_type.
        
    Returns
    -------
    dict
        Dictionary with "next" key indicating which agent to route to
        ("therapist" for emotional messages, "logical" for factual messages).
        
    Examples
    --------
    >>> state = {"messages": [...], "message_type": "emotional"}
    >>> result = router(state)
    >>> result["next"]
    "therapist"
    """
    message_type = state.get("message_type", "logical")
    if message_type == "emotional":
        return {"next": "therapist"}

    return {"next": "logical"}


def therapist_agent(state: State):
    """
    Generate an empathetic, therapy-style response to emotional user messages.
    
    This agent focuses on emotional support, validation, and helping users
    process their feelings. It avoids logical solutions unless explicitly
    requested and instead provides compassionate, therapeutic responses.
    
    Parameters
    ----------
    state : State
        The current conversation state containing the user's message.
        
    Returns
    -------
    dict
        Dictionary containing the assistant's empathetic response message.
        
    Examples
    --------
    >>> state = {"messages": [{"content": "I'm feeling overwhelmed"}]}
    >>> result = therapist_agent(state)
    >>> "empathy" in result["messages"][0]["content"].lower()
    True
    """
    last_message = state["messages"][-1]

    messages = [
        {"role": "system",
         "content": """You are a compassionate therapist. Focus on the emotional aspects of the user's message.
                        Show empathy, validate their feelings, and help them process their emotions.
                        Ask thoughtful questions to help them explore their feelings more deeply.
                        Avoid giving logical solutions unless explicitly asked."""
         },
        {
            "role": "user",
            "content": last_message.content
        }
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}


def logical_agent(state: State):
    """
    Generate a factual, logic-based response to informational user queries.
    
    This agent focuses purely on facts, information, and logical analysis.
    It provides clear, concise answers based on evidence and avoids
    emotional considerations or therapeutic responses.
    
    Parameters
    ----------
    state : State
        The current conversation state containing the user's query.
        
    Returns
    -------
    dict
        Dictionary containing the assistant's logical, fact-based response.
        
    Examples
    --------
    >>> state = {"messages": [{"content": "What is the capital of France?"}]}
    >>> result = logical_agent(state)
    >>> "Paris" in result["messages"][0]["content"]
    True
    """
    last_message = state["messages"][-1]

    messages = [
        {"role": "system",
         "content": """You are a purely logical assistant. Focus only on facts and information.
            Provide clear, concise answers based on logic and evidence.
            Do not address emotions or provide emotional support.
            Be direct and straightforward in your responses."""
         },
        {
            "role": "user",
            "content": last_message.content
        }
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}


# Build the conversation graph with nodes and edges
graph_builder = StateGraph(State)

# Add nodes for each step in the conversation flow
graph_builder.add_node("classifier", classify_message)
graph_builder.add_node("router", router)
graph_builder.add_node("therapist", therapist_agent)
graph_builder.add_node("logical", logical_agent)

# Define the conversation flow edges
graph_builder.add_edge(START, "classifier")
graph_builder.add_edge("classifier", "router")

# Add conditional routing based on message classification
graph_builder.add_conditional_edges(
    "router",
    lambda state: state.get("next"),
    {"therapist": "therapist", "logical": "logical"}
)

# Both agents end the conversation flow
graph_builder.add_edge("therapist", END)
graph_builder.add_edge("logical", END)

# Compile the graph into an executable workflow
graph = graph_builder.compile()


def run_chatbot():
    """
    Run the interactive chatbot with dual-agent message classification.
    
    This function provides a command-line interface for users to interact
    with the dual-agent system. It continuously processes user input,
    classifies messages as emotional or logical, routes them to the
    appropriate agent, and displays the responses.
    
    The chatbot continues running until the user types "exit".
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    
    Examples
    --------
    >>> run_chatbot()  # doctest: +SKIP
    Message: How are you feeling today?
    Assistant: I understand you're asking about feelings...
    Message: exit
    Bye
    
    Notes
    -----
    - Type "exit" to quit the chatbot
    - Messages are automatically classified and routed to appropriate agents
    - Emotional messages go to the therapist agent
    - Logical/factual messages go to the logical agent
    """
    state = {"messages": [], "message_type": None}

    while True:
        user_input = input("Message: ")
        if user_input == "exit":
            print("Bye")
            break

        state["messages"] = state.get("messages", []) + [
            {"role": "user", "content": user_input}
        ]

        state = graph.invoke(state)

        if state.get("messages") and len(state["messages"]) > 0:
            last_message = state["messages"][-1]
            print(f"Assistant: {last_message.content}")


if __name__ == "__main__":
    run_chatbot()