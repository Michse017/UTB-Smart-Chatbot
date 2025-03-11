# UTB-Smart-Chatbot 🚀

UTB-Smart-Chatbot is an interactive chatbot that gives info about undergraduate programs at Universidad Tecnológica de Bolívar (UTB). It uses first-order logic with PyDatalog for knowledge representation and inference, plus a BFS algorithm to match queries with program info. It also normalizes text (removes accents), keeps a query history to avoid repetition, and gives special responses for thanks and farewells. 😃

## Features & Stuff 😎

- **First-Order Logic Knowledge Base:**  
  Programs are stored as facts with PyDatalog. Rules help infer extra info (like which faculty a program belongs to).

- **BFS Keyword Matching:**  
  The chatbot uses a keyword graph where each node represents a keyword or synonym related to a specific program. When a user enters a query, the input is first normalized (accents removed, converted to lowercase), then tokenized. The chatbot applies a Breadth-First Search (BFS) algorithm to traverse this graph starting from the query tokens, exploring neighboring nodes until it finds a match with an official program name. This approach ensures that even if a user uses different terms or synonyms, the system can still map the query to the correct program.

- **Text Normalization:**  
  Input strings are normalized (accents removed, lowercase conversion) to improve matching.

- **Query History:**  
  The bot keeps track of what you've already asked and asks if you want to see the info again. 🔄

- **Special Responses:**  
  Custom replies for thanks ("gracias", etc.) and farewells ("adiós", "chao", etc.).

- **Extensibility:**  
  Easily add new programs (e.g., from the School of Engineering, Architecture and Design, and the School of Digital Transformation).

- **Planned Diagrams:**  
  ## Diagrams 📊

Activity diagrams and use case diagrams will be added later to show the system's flow. In this section, I will include the diagrams along with a description of their purpose and instructions on how to embed them in this document.

### Activity Diagram

**Purpose:**  
An Activity Diagram illustrates the workflow of the system. It shows the sequence of activities and decision points that occur during a particular process. In the context of the UTB-Smart-Chatbot, an activity diagram could depict the steps from when a user inputs a query, through text normalization, BFS matching in the keyword graph, retrieving program details, checking query history, and finally displaying the result.

### Use Case Diagram

**Purpose:**
The use case diagram provides an overview of the interactions between the UTB-Smart-Chatbot and its users. It identifies the main functionalities (use cases) such as "Query Program Information", "Receive Program Details", and "Manage Knowledge Base", along with the actors (e.g., User, Administrator).

## Repo Structure (Sorta) 😅
  UTB-Smart-Chatbot/ ├── information_base.py # Contains the knowledge base, facts, rules, and the keyword graph. ├── chatbot_utb.py # Main chatbot script implementing the interactive session and query history. └── README.md # This file.

## Installation & Stuff 🛠️

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your_username/UTB-Smart-Chatbot.git
   cd UTB-Smart-Chatbot

2. **Install Dependencies:**

  Ensure you have Python 3.12 or later installed, then run:
  pip install pyDatalog

## Usage 🤖

  o start the chatbot, run the following command in your terminal:

  python chatbot_utb.py

  The chatbot will launch an interactive session. Type your queries (e.g., "sistemas", "civil", "biomedica") to receive program information. The system will also handle thanks and farewells and    will check if you have already queried a program.