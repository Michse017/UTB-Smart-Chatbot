# UTB-Smart-Chatbot 🚀

UTB-Smart-Chatbot is an interactive chatbot that provides information about the undergraduate programs offered by the Universidad Tecnológica de Bolívar (UTB). The chatbot leverages first-order logic using PyDatalog for knowledge representation and inference, combined with a breadth-first search (BFS) algorithm to match user queries with the corresponding program information. It also features text normalization (to handle accents), a query history to avoid repetition, and special responses for thanks and farewells. 😃

## Features & Stuff 😎

- **First-Order Logic Knowledge Base:**  
  Programs are stored as facts with PyDatalog. Rules help infer extra info (like which faculty a program belongs to).

- **BFS Keyword Matching:**  
  A keyword graph maps your query to the right program using a BFS algorithm. The process involves:
  - **Text Normalization:** Input strings are normalized (accents removed, converted to lowercase) for better matching.
  - **Graph Traversal:** The BFS algorithm explores related keywords to find the official program name.

- **Query History:**  
  The bot keeps track of what you've already asked and asks if you want to see the info again. 🔄

- **Special Responses:**  
  Custom replies are provided for thanks ("gracias", etc.) and farewells ("adiós", "chao", etc.).

- **Extensibility:**  
  New programs (including those from the School of Engineering, Architecture and Design, and the School of Digital Transformation) can be added easily.

- **Planned Diagrams:**  
  Activity diagrams and use case diagrams will be added later to illustrate system processes and interactions. 📊

## Repository Structure:

- **UTB-Smart-Chatbot/**
  - **diagrams/**
    - Diagrama_de_actividades_chatbot_UTB.png
    - Diagrama_de_caso_de_uso_chatbot_UTB.png
  - information_base.py
  - chatbot_utb.py
  - README.md


