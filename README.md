# Self-Adaptive-Production-Line-Simulator

This project simulates a self-adaptive production line using an LLM (Language Model) to optimize temperature, pressure, and minimize plastic waste. Follow the steps below to set up and run the system.

## Table of Contents
- [Self-Adaptive-Production-Line-Simulator](#self-adaptive-production-line-simulator)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Setup Instructions](#setup-instructions)
  - [Running the System](#running-the-system)
  - [How it Works](#how-it-works)
  - [Example Output](#example-output)
  - [License](#license)

---

## Prerequisites
Before starting, ensure you have the following installed:

**1. Python 3.8 or higher**  
   You can check the version with:
   ```bash
   python3 --version
   ```
**2. Virtualenv**  
   Install virtualenv if it's not already installed:
   ```bash
   pip install virtualenv
   ```
**3. Git**  
   Install Git for version control:
   ```bash
   sudo apt install git   # For Linux 
   brew install git       # For macOS
   ```
**4. OpenAI API Key**  
   - Obtain your API key from the [OpenAI Platform](https://platform.openai.com/docs/overview).
   - Keep it ready for setup.
   
---

## Setup Instructions

**1. Clone the Repository**
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/ChenLiangChi/Self-Adaptive-Production-Line-Simulator.git
   cd self-adaptive-production-line-simulator
   ```

**2. Create a Virtual Environment**
   Run the following command to create a virtual environment:
   ```bash
   virtualenv -p python3.8 venv
   ```
   Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source venv/bin/active
     ```
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

**3. Install Dependencies**
Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

**4. Set Up OpenAI API Key**
Export your OpenAI API key:
   - On macOS/Linux:
     ```bash
     export OPENAI_API_KEY="your-api-key-here"
     ```
   - On Windows:
     ```bash
     $env:OPENAI_API_KEY="your-api-key-here"
     ```

---

## Running the System
To start the simulation, run the following command:

```bash
python abstract_goal_management.py
```

The system will: 
1. Phrase high-level goals
2. Collect production data
3. Use an LLM to generate optimization strategies
4. Update production setting to meet the goals

---

## How it Works
**1. Goal Management Layer**
    Set the abstract production goals (e.g., "Optimize the production cost") \
**2. Strategy Management Layer**
    Leverages OpenAI's GPT model to suggest optimal strategies \
**3. Strategy Execution Layer**
    Update the control parameters (e.g. temperature, pressure) on the target system \
**4. Shared Context**
    Sharing the context (strategies) between layers 

---

## Example Output

```bash
----------
1. Goal Management Layer: Strategy -> ...
----------
2. Strategy Management Layer: Generated strategy ->
{
    "recommendations": {
    "time": "night",
    "temperature": "180 °C",
    "pressure": "68 bar"
},
"explanation": ...
----------
```

---

## License

This project is licensed under the Apache-2.0 license. See  the [LICENSE](https://github.com/ChenLiangChi/Self-Adaptive-Production-Line-Simulator?tab=Apache-2.0-1-ov-file#readme) file for details.

