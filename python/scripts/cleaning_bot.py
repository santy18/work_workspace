
import os
import openai
import tiktoken
from pathlib import Path

# 🔧 CONFIG
INPUT_FILE = "input.html"
OUTPUT_FILE = "cleaned_output.txt"
CHUNK_TOKEN_LIMIT = 1500
MODEL = "gpt-4o-mini"
openai.api_key = os.environ["OPEN_AI_SECRET_KEY"]
  

# 📐 Tokenizer
enc = tiktoken.encoding_for_model(MODEL)

def tokenize(text):
    return enc.encode(text)

def detokenize(tokens):
    return enc.decode(tokens)

def chunk_text(text, max_tokens=CHUNK_TOKEN_LIMIT):
    tokens = tokenize(text)
    return [detokenize(tokens[i:i + max_tokens]) for i in range(0, len(tokens), max_tokens)]

def extract_text_with_llm(chunk):
    prompt = f"""You are a cleaning bot. Remove all HTML tags and keep only the human-readable text.

    HTML:
    {chunk}

    Cleaned text:"""

    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that cleans HTML."},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
    )
    return response.choices[0].message["content"].strip()

def main():
    raw_html = Path(INPUT_FILE).read_text(encoding="utf-8")
    chunks = chunk_text(raw_html)

    print(f"Processing {len(chunks)} chunks...")

    cleaned_parts = []
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}/{len(chunks)}")
        cleaned = extract_text_with_llm(chunk)
        cleaned_parts.append(cleaned)

    Path(OUTPUT_FILE).write_text("\n\n".join(cleaned_parts), encoding="utf-8")
    print(f"Done. Output written to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()