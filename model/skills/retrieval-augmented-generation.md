---
source: Local
group: AI
---

# Retrieval-augmented generation

> Building systems that retrieve relevant external content and feed it to a language model so its output is grounded in that content.

## In practice

Design how content is chunked, indexed and retrieved so the most relevant material is available
at query time. Tune retrieval quality, such as ranking and filtering, and shape how retrieved
content is presented to the model. Evaluate whether generated answers stay grounded in the
retrieved content rather than drifting from it. Typical tools: Pinecone, Weaviate, FAISS.
