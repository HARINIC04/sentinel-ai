sentinel-ai
A multi-agent AI system for real-time disaster early warning, risk prediction, and automated rescue planning.

This project is designed to pull data from weather, satellite, and ground-level sources to provide immediate, actionable intelligence to civilians and authorities during emergencies like floods, cyclones, and wildfires.

Project Goal
The mission of sentinel-ai is to reduce human and economic loss from natural disasters by providing a completely open-source, free-to-use, and intelligent warning system.

Core Architecture: Multi-Agent System
The system is built as a collaborative team of AI agents, each with a specialized role.

Data Collector Agent: Fetches real-time data from various APIs (NASA FIRMS for fire, IMD/NWS for weather, OpenRouteService for maps).

Risk Prediction Agent: Uses ML models and LLM analysis to predict the likelihood and path of a disaster.

Route Planner Agent: Calculates the safest (not just fastest) evacuation routes that avoid high-risk zones.

Emergency Action Agent: Generates personalized, simple "what-to-do" instructions for users based on their location.

Government Report Agent: Automatically generates daily situation reports and risk summaries for authorities.

Tech Stack
Backend & AI: Python

Agent Framework: CrewAI (or Microsoft AutoGen)

LLM Brains: Groq API (Llama 3) - 100% Free

Data Sources: NASA FIRMS, IMD, NWS, OpenFEMA

Routing: OpenRouteService

Deployment: Docker, AWS/GCP/Azure (Free Tier)

Frontend (Future): React, Node.js, MongoDB (MERN Stack)

Getting Started
1. Clone the repository
Bash

git clone https://github.com/YOUR_USERNAME/sentinel-ai.git
cd sentinel-ai
2. Create a virtual environment
Bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
Bash

pip install -r requirements.txt
4. Set up API keys
Create a .env file and add your keys:

GROQ_API_KEY=your_groq_api_key
OPENROUTESERVICE_API_KEY=your_ors_api_key
5. Run the main agent task
Bash

python main.py
