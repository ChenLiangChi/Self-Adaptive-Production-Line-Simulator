import threading
import queue
import os
import time
from openai import OpenAI
import json

# Set DEBUG_MODE to True to print debug messages
DEBUG_MODE = False 

# Set API key for LLM
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

production_data = {
    "time": "day",
    "temperature": "200 °C",
    "pressure": "80 bar",
    "electricity_price": "0.25 USD/kWh",
    "plastic_waste": "17 %",
    "yield": "0.78 (ratio)"
}

shared_context = {
    "goal": None,                  
    "historical_analysis": None,   
    "current_production_data": production_data,  
    "previous_strategies": []      
}

# Synchronization events for strict sequential execution
goal_done = threading.Event()
strategy_management_done = threading.Event()
strategy_enactment_done = threading.Event()

# Initialize the first cycle
strategy_enactment_done.set()

# Load historical data from a JSON file
def load_historical_data(file_path="historical_data.json"):
    """
    Load historical production data from the specified JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list: List of historical production data.
    """
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            print("Successfully loaded historical data.")
            return data
    except Exception as e:
        print(f"Error loading historical data: {e}")
        return []

historical_production_data = load_historical_data()

# Simulate high-level goal parsing
def goal_management():
    while True:
        strategy_enactment_done.wait()  # Wait for the previous cycle to finish
        strategy_enactment_done.clear()

        # Set a new goal and proceed
        shared_context["goal"] = "Minimize plastic waste, ensure yield ≥ 0.9, and optimize electricity costs."
        goal = shared_context["goal"]
        
        # Retrieve the latest production data from the queue
        if historical_production_data:

            # Use LLM to analyze if the production data meets the goal
            prompt = (
                f"Here is the past production line data: {json.dumps(historical_production_data)}. "
                f"The goal is '{goal}'. "
                "From the historical data, determine the optimal ranges for time, temperature, and pressure "
                "that minimize plastic waste while maintaining yield ≥ 0.9 and minimizing electricity costs. "
                "Provide a concise summary in 100 words."
            )

            try:
                response = client.chat.completions.create(
                    #model="gpt-3.5-turbo",
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a production goal optimization assistant responsible for analyzing historical data and providing strategies."},
                        {"role": "user", "content": prompt}
                    ],
                )
                analysis = response.choices[0].message.content.strip()
                print("----------", end="\n")
                print(f"1. Goal Management Layer: Strategy -> {analysis}", end="\n")
                
                shared_context["historical_analysis"] = analysis

            except Exception as e:
                print(f"1. Goal Management Layer: Error occurred -> {e}", end="\n")

        time.sleep(1)
        goal_done.set()  
        

def strategy_management():
    while True:
        goal_done.wait()  
        goal_done.clear()
        
        goal = shared_context["goal"]
        historical_analysis = shared_context["historical_analysis"]
        current_data = shared_context["current_production_data"]
        previous_strategies = shared_context["previous_strategies"]
        
        # Use LLM to generate strategy based on goals and data
        prompt = (
            f"The goal is '{goal}'. "
            f"Historical analysis indicates the following optimal ranges: {historical_analysis}. "
            f"Current production line data: {json.dumps(current_data)}. "
            f"Previous strategies as reference: {json.dumps(previous_strategies)}. "
            "Suggest specific time, temperature, and pressure adjustments that meet the goal. "
            "Ensure your recommendation meet all criteria. "
            "Return the recommendations in JSON format without any Markdown syntax, and include an explanation in 100 words."
        )

        try:
            response = client.chat.completions.create(
                #model="gpt-3.5-turbo",
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a production line strategy optimization assistant responsible for generating strategies based on data and historical analysis."},
                    {"role": "user", "content": prompt}
                ],
            )
            strategy = response.choices[0].message.content.strip()
            print("----------", end="\n")
            print(f"2. Strategy Management Layer: Generated strategy -> \n{strategy}", end = "\n")
            shared_context["previous_strategies"].append(strategy)
        except Exception as e:
            print(f"2. Strategy Management Layer: Error occurred -> {e}")

        print("----------", end="\n")
        time.sleep(5)
        strategy_management_done.set() 

def strategy_enactment():
    """
    Ignore this part
    """
    strategy_management_done.wait()
    strategy_management_done.clear()
    
    if DEBUG_MODE:
        print("\n===== Shared Context Values =====")
        for key, value in shared_context.items():
            print(f"{key}: {json.dumps(value, indent=4, ensure_ascii=False)}")
        print("=================================")
    os._exit(0)


threads = [
    threading.Thread(target=goal_management),
    threading.Thread(target=strategy_management),
    threading.Thread(target=strategy_enactment),
]

for thread in threads:
    thread.start()