# ai-drone-controller


AI-augmented flight controller to improve drone stability under wind disturbances.  
This project simulates drone hover using a classical PID controller and trains an AI agent to improve stability under variable wind.

## Project Milestones

- ✅ 3/27 – Project setup & GitHub repo created
- 🔲 3/28 – Simulate PID hover with wind
- 🔲 3/30 – Train simple AI controller (PPO)
- 🔲 3/31 – Compare AI + PID vs PID-only

## To Run

```bash
python hover_pid.py
python plot_results.py