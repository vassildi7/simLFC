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

simulator_PrimaryControl/
simulator_IntegralController/
simulator_PIDController/
simulator_2area_PID/

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

##  How to Run

Each folder is self-contained.

Example:

```bash
cd simulator_PIDController
python main.py

---






