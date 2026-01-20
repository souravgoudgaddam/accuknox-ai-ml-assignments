## 3. Vector Databases (Based on My Document Q&A System)

A vector database is used to store embeddings that represent the semantic meaning of documents. Instead of relying on exact keyword matching, it enables similarity-based retrieval, which is essential for building effective document question-answering systems.

---

## How It Was Used in My Project
In my document Q&A application, uploaded documents are first loaded from a directory and split into manageable text units. These document chunks are then converted into vector embeddings using a sentence-transformer model and stored in a vector database. The vector database serves as persistent storage for these embeddings.

When a user submits a question, the query is also converted into an embedding and compared against the stored document vectors using similarity search. The most relevant document chunks are retrieved and passed to the language model, which generates a context-aware response grounded in the actual document content.

---

## Vector Database Choice
For this project, I used **ChromaDB** as the vector database. ChromaDB supports persistent storage, efficient similarity search, and integrates seamlessly with Python-based AI workflows. It was well-suited for local development and made it straightforward to store, manage, and query document embeddings during both document ingestion and question-answering.

---

**Project Repository:**  
https://github.com/souravgoudgaddam/AskMyDocs-System
