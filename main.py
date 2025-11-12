import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process

# Load environment variables
load_dotenv()

# --- Set Environment Variables for Groq (Our AI Brain) ---
# This is the correct, stable way to connect
os.environ["OPENAI_API_KEY"] = os.getenv("GROQ_API_KEY")
# This is the corrected line
os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"
os.environ["OPENAI_MODEL_NAME"] = "llama-3.1-8b-instant"
# ----------------------------------------------------

# Import our tools
from tools.data_tools import weather_data_tool, routing_tool

# --- 1. Define Agents ---

# Agent 1: The Data Collector
data_collector_agent = Agent(
    role='Data Collector',
    goal='Fetch real-time weather data for a specific location.',
    backstory=(
        "You are an agent that fetches data from APIs. "
        "You must use the 'Weather Data Tool' to get the current weather."
    ),
    tools=[weather_data_tool], # Only has the weather tool
    verbose=True,
    allow_delegation=False
)

# Agent 2: The Risk Analyst (AI-Only)
risk_analysis_agent = Agent(
    role='Risk Analysis Expert',
    goal='Analyze weather data to determine if there is an immediate disaster risk (flood, cyclone, or fire).',
    backstory=(
        "You are an expert meteorologist and disaster analyst. "
        "You will receive raw weather data. Your job is to analyze this data and state a clear risk level. "
        "For example, high rain (e.g., > 10mm) means 'High Flood Risk'. High wind (e.g., > 40 km/h) means 'High Cyclone Risk'. "
        "If there is no high rain or wind, the risk is 'Low'."
    ),
    tools=[], # No tools, it only thinks
    verbose=True,
    allow_delegation=False
)

# Agent 3: The Route Planner
route_planner_agent = Agent(
    role='Evacuation Route Planner',
    goal='Provide a safe evacuation route from a high-risk area to a designated safe point.',
    backstory=(
        "You are a logistics and emergency response planner. "
        "You receive a starting location (the user) and a safe location. "
        "Your job is to use the 'Safe Evacuation Route Tool' to calculate the driving route between them."
    ),
    tools=[routing_tool],
    verbose=True,
    allow_delegation=False
)

# --- NEW AGENT ---
# Agent 4: The Notification Agent (AI-Only)
notification_agent = Agent(
    role='Emergency Notification Specialist',
    goal='Create a simple, human-readable alert message for a user based on risk and evacuation data.',
    backstory=(
        "You are an expert in public safety alerts. You receive technical data "
        "(weather, risk level, and a route) and must summarize it into a "
        "clear, calm, and actionable message for a civilian. "
        "Your message must state the risk level and, if a route is provided, the distance and time."
    ),
    tools=[], # No tools, it only thinks
    verbose=True,
    allow_delegation=False
)


# --- 2. Define Tasks ---

# We'll use our test location (Coimbatore)
user_latitude = 11.0168
user_longitude = 76.9558

# A safe point (e.g., a known shelter or just a point 10km away)
safe_point_latitude = 11.0500 
safe_point_longitude = 77.0000

# Task 1: Get Weather Data
data_collection_task = Task(
    description=f'Fetch current weather for latitude {user_latitude} and longitude {user_longitude}.',
    expected_output='A JSON string of the current weather data.',
    agent=data_collector_agent
)

# Task 2: Analyze the Risk
# This task will use the output of the first task (context)
risk_analysis_task = Task(
    description='Analyze the provided weather data. Determine a risk level (e.g., "High Flood Risk", "Low Risk").',
    expected_output='A simple string stating the risk level and the reason (e.g., "High Flood Risk due to 15mm rain").',
    agent=risk_analysis_agent,
    context=[data_collection_task] # This is how we pass data
)

# Task 3: Plan the Route
# This task will run after the risk analysis
route_planning_task = Task(
    description=(
        f'Calculate the safest evacuation route from the user at ({user_latitude}, {user_longitude}) '
        f'to the safe point at ({safe_point_latitude}, {safe_point_longitude}).'
    ),
    expected_output='A string summarizing the route distance and duration.',
    agent=route_planner_agent,
    context=[risk_analysis_task] # Depends on the risk being analyzed
)

# --- NEW TASK ---
# Task 4: Create the Final Notification
notification_task = Task(
    description='''
        Create a final, human-readable notification for the user.
        You must use the information from all previous tasks:
        1. The current weather data.
        2. The official risk analysis.
        3. The evacuation route summary.
        
        Combine all this into a single, simple message. For example:
        "Risk: [Risk Level]. Weather: [Weather Summary]. Evacuation Route: [Route Summary]."
    ''',
    expected_output='A single, concise string containing the final alert message for the user.',
    agent=notification_agent,
    context=[data_collection_task, risk_analysis_task, route_planning_task]
)


# --- 3. Create and Update the Crew ---
sentinel_crew = Crew(
    agents=[data_collector_agent, risk_analysis_agent, route_planner_agent, notification_agent], # <-- AGENT ADDED
    tasks=[data_collection_task, risk_analysis_task, route_planning_task, notification_task], # <-- TASK ADDED
    process=Process.sequential,
    verbose=True
)

# --- 4. Run the Crew ---
print("🚀 Starting Sentinel-AI Crew (Full Mission)...")
result = sentinel_crew.kickoff()

print("\n---  Crew Mission Finished ---")
print("Final Result:")
print(result)