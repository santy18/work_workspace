#ai_transformers

```ruby
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Define model parameters
d_model = 512  # Embedding size
nhead = 8  # Number of attention heads
num_encoder_layers = 6
num_decoder_layers = 6
dim_feedforward = 2048
dropout = 0.1
seq_length = 10  # Length of input/output sequences
vocab_size = 100  # Vocabulary size for tokens

# Create a simple Transformer model
class SimpleTransformer(nn.Module):
    def __init__(self, vocab_size, d_model, nhead, num_encoder_layers, num_decoder_layers, dim_feedforward, dropout):
        super(SimpleTransformer, self).__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.positional_encoding = nn.Parameter(torch.zeros(1, seq_length, d_model))  # Learnable position embeddings
        self.transformer = nn.Transformer(
            d_model=d_model,
            nhead=nhead,
            num_encoder_layers=num_encoder_layers,
            num_decoder_layers=num_decoder_layers,
            dim_feedforward=dim_feedforward,
            dropout=dropout
        )
        self.fc_out = nn.Linear(d_model, vocab_size)

    def forward(self, src, tgt):
        src_emb = self.embedding(src) + self.positional_encoding
        tgt_emb = self.embedding(tgt) + self.positional_encoding
        src_emb = src_emb.permute(1, 0, 2)  # Sequence first for Transformer
        tgt_emb = tgt_emb.permute(1, 0, 2)
        transformer_output = self.transformer(src_emb, tgt_emb)
        output = self.fc_out(transformer_output.permute(1, 0, 2))
        return output

# Instantiate the model
model = SimpleTransformer(vocab_size, d_model, nhead, num_encoder_layers, num_decoder_layers, dim_feedforward, dropout)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.0001)

# Sample input (source and target sequences with random indices from vocabulary)
src = torch.randint(0, vocab_size, (32, seq_length))  # Batch size of 32, sequence length 10
tgt = torch.randint(0, vocab_size, (32, seq_length))

# Shift target for teacher forcing
tgt_input = tgt[:, :-1]
tgt_output = tgt[:, 1:]

# Forward pass
output = model(src, tgt_input)

# Compute loss
loss = criterion(output.view(-1, vocab_size), tgt_output.view(-1))

# Backpropagation
loss.backward()
optimizer.step()

print(f"Loss: {loss.item():.4f}")

```

### Explanation:

1. **Embedding**:
    
    - Converts token indices into dense vectors of size `d_model`.
2. **Positional Encoding**:
    
    - Adds positional information to the embeddings so the Transformer can understand sequence order.
3. **Transformer**:
    
    - The core model with encoder and decoder layers. Encoders process the input sequence, and decoders generate the output.
4. **Training Loop**:
    
    - Source (`src`) and target (`tgt`) sequences are passed through the model.
    - Loss is calculated using CrossEntropy, and the model is optimized using backpropagation.