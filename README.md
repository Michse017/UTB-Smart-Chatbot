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

## Planned Diagrams 📊

Activity diagrams and use case diagrams help visualize the system's flow and interactions. Below is a brief description of each type of diagram:

1. **Use Case Diagram**  
   - **Purpose:** Shows how different actors (e.g., User, Admin, Agent) interact with the chatbot. It highlights the main functionalities (use cases) such as asking questions, updating the knowledge base, and customizing the chatbot.  
   - **Example:** In the figure, you can see how the “Usuario” actor uses the chatbot, and the “Admin” actor updates or customizes it, while an internal “Agente” can respond to queries or consult the knowledge base.

   ![Use Case Diagram](diagrams/Diagrama_de_caso_de_uso_chatbot_UTB.png)

2. **Activity Diagram**  
   - **Purpose:** Depicts the sequence of activities (steps or states) within the chatbot’s workflow. It covers how the user’s input is processed, how the chatbot checks the knowledge base, and how it decides on a response.  
   - **Example:** In the figure, you can see how the chatbot processes input, determines if the query can be answered, and either returns structured information or asks for clarification if the user’s intent is unclear.

   ![Activity Diagram](diagrams/Diagrama_de_actividades_chatbot_UTB.png)

3. **Agent Diagram**  
   - **Purpose:** Illustrates how the chatbot agent perceives inputs (Sensors), processes them (NPL and knowledge base), and then makes decisions leading to actions (Actuators). It also shows the environment in which the agent operates.  
   - **Example:** In the figure, you can see how the user’s query becomes a “sensor” input, how the agent checks its internal state and knowledge base, and finally produces a response (actuation) to the user.

   ![Agent Diagram](diagrams/Agent_Diagram.png)

## Repository Structure:

- **UTB-Smart-Chatbot/**
  - **diagrams/**
    - Diagrama_de_actividades_chatbot_UTB.png
    - Diagrama_de_caso_de_uso_chatbot_UTB.png
  - information_base.py
  - chatbot_utb.py
  - README.md


## Installation & Stuff 🛠️

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your_username/UTB-Smart-Chatbot.git
   cd UTB-Smart-Chatbot

2. **Install Dependencies:**

    Make sure you have Python 3.12 or later installed, then run:
    pip install pyDatalog

## How to Use It 🤖

    Run the chatbot with:
    
    python chatbot_utb.py

    The chatbot will launch an interactive session. Type queries like "sistemas", "civil", or "biomedica" to get program info. The bot will also handle thanks and farewells, and it will check if you have already queried a program. 🔥


