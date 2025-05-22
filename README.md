# simLFC

This repository provides a single-area load frequency control system simulator integrated in Python:

1. Only with primary control (simulator_PrimaryOnly)
2. With Integral secondary control (simulator_IntegralController)
3. With PID secondary control (simulator_PIDController)

There is also a two-area load frequency control system simulator integrated in Python:

4. With PID secondary control in each area (simulator_2area_PID)


# How to run the simulator
1. Clone the repository folder corresponding to the simulator you want to your local device.
2. Open in terminal and run python main.py

# Parameter tuning
1. Change system attributes in config.py file.
2. Tune controller in config.py file
3. Edit disturbance in main.py file
