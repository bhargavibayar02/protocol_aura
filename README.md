# Protocol Aura (Protocol Analyzer & Attack Simulator)

A **Flask web application** that combines protocol analysis, attack simulation, and AI-driven explanations.  
It provides interactive pages for analyzing protocols, simulating attacks across layers, and querying an AI engine for deeper insights.

---

##  System Overview

- **Protocol Analysis**
  - Users select a protocol (e.g., HTTP, TCP, UDP).
  - The system calls `analyze_protocol()` to return structured details.
  - Results are displayed on a dedicated protocol page.

- **Attack Simulation**
  - `/attack` page introduces attack scenarios.
  - `/get_attack` API returns simulated attack data for a given OSI layer.
  - Useful for educational demonstrations of network security threats.

- **AI Chat**
  - `/ai_chat` endpoint allows users to ask questions about a protocol.
  - Uses `explain()` from the AI engine to generate contextual answers.
  - Combines protocol data with user queries for intelligent responses.

- **Error Handling**
  - Custom 404 handler returns a simple "Page not found" message.

---

---

##  Technology Stack

- **Backend:** Flask (Python)
- **AI Engine:** Custom `explain()` function for contextual answers
- **Simulation:** Attack data generator for OSI layers
- **Frontend:** Jinja2 templates for rendering pages
- **API:** JSON endpoints for attack data and AI chat

---

##  Key Functionalities

- **Home Page (`/`)**
  - Entry point with navigation to analysis and attack modules.

- **Protocol Analysis (`/analyze`)**
  - Accepts POST requests with a protocol name.
  - Returns structured analysis results.

- **Attack Simulation (`/attack`, `/get_attack`)**
  - Displays attack scenarios.
  - Provides JSON attack data for a given layer.

- **AI Chat (`/ai_chat`)**
  - Accepts protocol + user question.
  - Returns AI-generated explanation based on protocol data.

---

## Minimal Setup Commands

```bash
# Install dependencies
pip install flask

# Run the application
python app.py

```
The app runs locally at:
http://127.0.0.1:5000

## 📂 Project Structure
