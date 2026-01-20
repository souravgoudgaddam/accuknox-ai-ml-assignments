# Problem 5 – Most Complex Database Code

## Project: AskMyDocs – Document Question Answering System

### Overview
This project implements a document-based question answering system that uses a vector database to store and retrieve document embeddings. The system allows users to upload documents, persist their semantic representations, and query them using natural language.

Unlike traditional relational databases, this project uses a vector database to enable similarity-based retrieval, which is essential for AI-driven document search and question answering.

---

### Database Design and Usage
- Documents are loaded and split into manageable chunks
- Each document chunk is converted into an embedding using a sentence-transformer model
- Embeddings are stored persistently using **ChromaDB**
- Metadata and vector representations are managed through the vector store
- During querying, user questions are embedded and compared against stored vectors to retrieve the most relevant document content

---

### GitHub Repository
🔗 **Link:**  
https://github.com/souravgoudgaddam/AskMyDocs-System
