# Load Frequency Control (LFC) Simulators

This repository contains four modular Python simulators for Load Frequency Control (LFC) systems using different control strategies. All simulators use fixed-step ODE4 (Runge-Kutta 4th order) integration and are organized into separate folders for clarity.

---

## Included Simulators

### 1. `simulator_PrimaryControl/`  
**Single-area LFC** with only **primary control (droop response)**.  
No secondary (AGC) or PID controller is used.

### 2. `simulator_IntegralController/`  
**Single-area LFC** with a simple **integral controller (AGC)**.  
This helps eliminate steady-state error after load disturbances.

### 3. `simulator_PIDController/`  
**Single-area LFC** using a full **PID controller** for faster, more stable responses.  
All PID terms (P, I, D) are tunable in `config.py`.

### 4. `simulator_2area_PID/`  
**Two-area LFC** system with inter-area tie-line and separate **PID controllers for each area**.  
Load disturbances can be applied independently to each area.

---

##  Features

- RK4-based numerical integration
- Customizable load disturbances (step-based)
- Modular controllers and system dynamics
- Separate plotting for each signal (Δf, ΔPm, ΔPload, ΔPtie, control)
- Easily adjustable controller gains in `config.py`

---

##  Output

Each simulation produces time-series plots including:

- Frequency deviations (Δf)
- Load disturbances (ΔPload)
- Mechanical power (ΔPm)
- Control signal output
- Tie-line power (in 2-area system)

---

##  Folder Structure

simulator_PrimaryControl/n
simulator_IntegralController/n
simulator_PIDController/n
simulator_2area_PID/n

Each folder contains:

- main.py (entry point)
- config.py (parameters & gains)
- controller.py or controller_pid.py
- system_model.py
- disturbance.py
- plot_utils.py

---

##   License & Contributions

This project is open-source and available under the MIT License.
Feel free to fork, modify, and contribute!

---

##  Research Context

This simulator collection is part of an ongoing research project on cyber-resilient control in power systems. It serves as a foundational tool for evaluating classical control strategies prior to the deployment of advanced AI-based solutions.

Specifically, this work is a **natural continuation of the research presented in the paper**:

**DRL²FC: An Attack-Resilient Controller for Load Frequency Control Based on Reinforcement Learning**  
(*PowerTech 2025, IEEE*)  
[arXiv:2404.16974](https://arxiv.org/abs/2404.16974)

In that work, a Double DQN-based reinforcement learning agent replaces the conventional AGC in a two-area LFC system and maintains frequency stability even under false data injection attacks (FDIAs). 

The simulators in this repository provide classical PID-based baselines and testbeds to validate and benchmark the performance of the DRL²FC framework. They are designed for transparency, reproducibility, and as a stepping stone for researchers moving from classical to AI-based LFC solutions.

---

##  How to Run

Each folder is self-contained.

Example:

```bash
cd simulator_PIDController
python main.py








