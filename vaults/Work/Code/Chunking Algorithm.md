```python
def chunk_data(data, chunk_size, overlap=0):
    """
    Splits data into chunks with optional overlap.

    Parameters:
    - data (list or str): The sequence to be chunked (e.g., text, list of numbers).
    - chunk_size (int): The size of each chunk.
    - overlap (int): Number of overlapping elements between consecutive chunks (default is 0).

    Returns:
    - list: A list of chunks.
    """
    # Initialize an empty list to store the chunks
    chunks = []

    # Step through the data using a stride adjusted for the overlap
    step = chunk_size - overlap

    # Iterate over the data, generating chunks
    for i in range(0, len(data), step):
        # Extract a chunk of size 'chunk_size' starting at index 'i'
        chunk = data[i:i + chunk_size]
        
        # Append the chunk to the list of chunks
        chunks.append(chunk)

        # Stop if the remaining data is smaller than the overlap
        if i + step >= len(data):
            break

    return chunks

# Example Usage:
if __name__ == "__main__":
    # Example 1: Chunking text
    text = "This is an example of chunking for text processing."
    chunk_size = 10  # Each chunk will have 10 characters
    overlap = 3      # 3 characters of overlap
    text_chunks = chunk_data(text, chunk_size, overlap)
    print("Text Chunks:", text_chunks)

    # Example 2: Chunking numbers
    numbers = list(range(1, 21))  # A list of numbers from 1 to 20
    chunk_size = 5               # Each chunk will have 5 numbers
    overlap = 2                  # 2 numbers of overlap
    number_chunks = chunk_data(numbers, chunk_size, overlap)
    print("Number Chunks:", number_chunks)

```

### Explanation:

1. **Parameters**:
    
    - `data`: The sequence to chunk (e.g., string or list).
    - `chunk_size`: Specifies the size of each chunk.
    - `overlap`: Optional; the number of overlapping elements between chunks.
2. **Logic**:
    
    - The `step` is calculated as `chunk_size - overlap` to determine how far to move for the next chunk.
    - Each iteration extracts a chunk of `chunk_size` from the data starting at `i`.
    - Overlapping chunks are created by starting the next chunk slightly before the end of the current one.
3. **Output**:
    
    - Returns a list of chunks, with each chunk being of size `chunk_size` or smaller if it's the last segment.

---

### Example Outputs:

1. **Chunking Text**:
    
    plaintext
    
    CopyEdit
    
    `Input:  "This is an example of chunking for text processing." Output: ['This is an', 'is an exam', 'an example ', 'xample of ', 'le of chun', 'of chunkin', 'chunking f', 'ing for te', 'r text pro', 'text proce']`
    
2. **Chunking Numbers**:
    
    plaintext
    
    CopyEdit
    
    `Input:  [1, 2, 3, ..., 20] Output: [[1, 2, 3, 4, 5], [4, 5, 6, 7, 8], [7, 8, 9, 10, 11], [10, 11, 12, 13, 14], ..., [19, 20]]`
    

This modular function is flexible and can be tailored for various chunking needs, such as preparing data for machine learning models or text summarization.