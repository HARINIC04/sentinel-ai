# 🛰️ sentinel-ai

![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)
![Framework](https://img.shields.io/badge/framework-CrewAI-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

> A multi-agent AI system for real-time disaster early warning, risk prediction, and automated rescue planning.

This project is designed to pull data from weather, satellite, and ground-level sources to provide immediate, actionable intelligence to civilians and authorities during emergencies like floods, cyclones, and wildfires.

---

## ✨ Key Features

* **Real-time Data Fusion:** Aggregates live data from NASA, weather services, and map APIs.
* **AI-Powered Risk Prediction:** Uses ML models to forecast disaster paths and impact zones.
* **Dynamic Safe Routing:** Calculates the safest evacuation routes that actively avoid danger zones.
* **Automated Reporting:** Generates instant situation summaries for emergency responders.
* **100% Free & Open Source:** Built with free APIs and open-source models (Groq/Llama 3).

---

## 🤖 Core Architecture: The Agent Team

The system is built as a collaborative team of AI agents, each with a specialized role:

### 1. Data Collector Agent
* **Task:** Fetches real-time data from various APIs (NASA FIRMS for fire, IMD/NWS for weather, OpenRouteService for maps).

### 2. Risk Prediction Agent
* **Task:** Uses ML models and LLM analysis to predict the likelihood and path of a disaster.

### 3. Route Planner Agent
* **Task:** Calculates the *safest* (not just fastest) evacuation routes that avoid high-risk zones.

### 4. Emergency Action Agent
* **Task:** Generates personalized, simple "what-to-do" instructions for users based on their location.

### 5. Government Report Agent
* **Task:** Automatically generates daily situation reports and risk summaries for authorities.

---

## 💻 Tech Stack

* **Backend & AI:** Python
* **Agent Framework:** CrewAI
* **LLM "Brains":** Groq API (Llama 3)
* **Data Sources:** NASA FIRMS, IMD, NWS, OpenFEMA
* **Routing:** OpenRouteService
* **Deployment:** Docker, AWS/GCP/Azure (Free Tier)
* **Frontend (Future):** React, Node.js, MongoDB (MERN Stack)

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR_USERNAME/sentinel-ai.git](https://github.com/YOUR_USERNAME/sentinel-ai.git)
cd sentinel-ai
