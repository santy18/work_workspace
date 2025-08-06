```python
import torch
import torch.nn.functional as F

def top_k_sampling(logits, k):
    """
    Applies top-k sampling to logits.

    Parameters:
    - logits (torch.Tensor): Logits from the model (unnormalized probabilities).
    - k (int): Number of top tokens to consider.

    Returns:
    - torch.Tensor: Index of the sampled token.
    """
    # Filter logits to keep only the top-k tokens
    top_k_logits, top_k_indices = torch.topk(logits, k)
    
    # Apply softmax to normalize the filtered logits
    probabilities = F.softmax(top_k_logits, dim=-1)
    
    # Sample from the top-k probabilities
    sampled_index = torch.multinomial(probabilities, num_samples=1)
    
    # Map the sampled index back to the original vocabulary index
    return top_k_indices[sampled_index]

# Example usage:
logits = torch.tensor([0.4, 0.3, 0.2, 0.05, 0.05])  # Example logits
k = 2  # Retain the top 2 tokens
sampled_token = top_k_sampling(logits, k)
print("Sampled Token Index:", sampled_token.item())

```

### **When to Use top_k**

- **Text Generation**: Ensure generated text is coherent and relevant.
- **Dialog Systems**: Avoid nonsensical or irrelevant responses.
- **Creative Tasks**: Use with larger `k` for more diverse, creative outputs (e.g., poetry generation).