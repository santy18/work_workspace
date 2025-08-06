*created at:* 2025-01-2411:48


*Created At:* 2025-01-24:11:49

#literature #aichunking

>[!question] Questions
> Why do we chunk data?


>[!example] Evidence:

We chunk data due to the [[LLMs]] having a limited context window. this is why we cannot just add the whole document in. 

If chunks are too big, this becomes an issue, where we can experience [[Loss In The Middle]] problem.
where a LLM will look at the beginning and end of the prompt but not pay much attention to the middle.

##### Chunk Sizes
Different documents have different optimal chunk sizes
![[Pasted image 20250124161656.png]]
you have to see which one works better for you and for your document.

### Example:
we have some code here to explain how this works under the hood [[Chunking Algorithm]]



>[!Success] Conclusion:

Chunking is important to get right, get the right [[AI Data Parsers]] in order to get the best and cleanest output to embed. 


