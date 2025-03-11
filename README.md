# UTB-Smart-Chatbot 🚀

UTB-Smart-Chatbot is an interactive chatbot that provides information about undergraduate programs at Universidad Tecnológica de Bolívar (UTB). It leverages first-order logic with PyDatalog for knowledge representation and inference, a BFS algorithm for keyword matching, text normalization, query history tracking, and custom responses for gratitude and farewells.

## Features & Stuff 😎

- **First-Order Logic Knowledge Base**  
  Programs are stored as PyDatalog facts with rules to infer additional details like faculty affiliations.

- **BFS Keyword Matching**  
  Uses a keyword graph and BFS algorithm to map user queries (including synonyms) to official program names.

- **Text Normalization**  
  Normalizes input text by removing accents and converting to lowercase for consistent matching.

- **Query History Tracking**  
  Maintains a history of user queries to avoid repetition and prompts users if they repeat a question. 🔄

- **Special Responses**  
  Custom replies for gratitude ("gracias") and farewells ("adiós", "chao").

- **Extensibility**  
  Easily add new programs from different schools (e.g., Engineering, Digital Transformation).

## Diagrams 📊 (Planned)

### Activity Diagram  
**Purpose:**  
Illustrates the workflow from user input to response, including normalization, BFS matching, and history checks.

### Use Case Diagram  
**Purpose:**  
Shows interactions between users and the chatbot, covering use cases like "Query Program Information" and "Manage Knowledge Base".

## Repo Structure 😅
  UTB-Smart-Chatbot/
  ├── information_base.py # Knowledge base, facts, rules, keyword graph
  ├── chatbot_utb.py # Main chatbot script with interactive session
  └── README.md # Project documentation
  