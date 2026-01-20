## 2. Chatbot Architecture (LLM-Based)

The following architecture and key components are based on the LLM-based chatbot that I implemented using **FastAPI**, **LangChain**, and **Mistral AI**. The components and flow described below reflect the actual design choices used in my project and demonstrate my practical approach to building an end-to-end chatbot system.

**Project Repository:**  
https://github.com/souravgoudgaddam/AI_chatbot

---
## Chatbot Architecture

![LLM Chatbot Architecture](Chatbot_architecture.jpg)


## Key Architectural Components (Project-Oriented)

### 1. API Entry Point
A REST API endpoint is used to receive user messages and return chatbot responses. This layer is responsible for request validation and ensures that the chatbot logic remains independent of the client interface.

### 2. Chat Service Logic
The core chatbot behavior is encapsulated within a dedicated service layer. This component coordinates prompt execution, manages conversation flow, and handles interaction with the language model.

### 3. Prompt Construction
User messages are combined with a structured prompt template to guide the chatbot’s behavior. This ensures consistent, context-aware responses while allowing flexibility in conversation handling.

### 4. Conversation Memory
Conversation history is summarized and maintained using a memory mechanism. This preserves contextual continuity across interactions without storing full message logs, helping the system remain efficient while staying on topic.

### 5. LLM Response Generation
A large language model (Mistral AI) is used to generate responses based on the constructed prompt and conversation context. The model is designed as a replaceable component, allowing flexibility in switching LLM providers if needed.

### 6. Response Delivery
The generated response is formatted and returned to the user through the API in a simple and structured format, completing the request–response cycle.
