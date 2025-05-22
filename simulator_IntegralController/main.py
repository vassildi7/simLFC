import numpy as np
from config import time_step, default_duration, Ki
from disturbance import generate_disturbance
from system_model import lfc_ode
from controller import IntegralController
from plot_utils import plot_results

# Runge-Kutta 4th-order fixed-step integrator (ODE4)
def rk4_step(f, t, y, h):
    y = np.asarray(y)
    k1 = np.asarray(f(t, y))
    k2 = np.asarray(f(t + h/2, y + h/2 * k1))
    k3 = np.asarray(f(t + h/2, y + h/2 * k2))
    k4 = np.asarray(f(t + h, y + h * k3))
    return y + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)


def simulate(duration=default_duration, disturbance_times=[20, 60], disturbance_mags=[0.02, -0.03]):
    t_vals = np.arange(0, duration, time_step)
    n_steps = len(t_vals)

    # Generate disturbance over time
    disturbance_array = generate_disturbance(t_vals, disturbance_times, disturbance_mags)
    disturbance_func = lambda t: np.interp(t, t_vals, disturbance_array)

    # Initialize state: [Δf, ΔPm, ΔPt, integral_error]
    y = np.zeros((n_steps, 4))
    y[0] = [0.0, 0.0, 0.0, 0.0]

    # Controller setup
    controller = IntegralController(Ki, time_step)
    controller.reset()
    print("Initial controller output:", controller.update(0.0))  # Debug

    # Control signal logging
    control_signal_log = np.zeros(n_steps)

    # Simulation loop using RK4
    for i in range(1, n_steps):
        t = t_vals[i-1]
        y_prev = y[i-1]

        # Define function for RK4 step (returns dy/dt)
        dydt_func = lambda t, y: lfc_ode(t, y, disturbance_func, controller)[0]

        # RK4 step
        y[i] = rk4_step(dydt_func, t, y_prev, time_step)

        # Log control signal
        _, control_signal = lfc_ode(t, y_prev, disturbance_func, controller)
        control_signal_log[i] = control_signal

    # Extract results
    delta_f = y[:, 0]
    delta_P_m = y[:, 1]
    delta_P_load = disturbance_array
    control_signal = control_signal_log

    # Plot results
    plot_results(t_vals, delta_f, delta_P_load, delta_P_m, control_signal)

if __name__ == '__main__':
    simulate()
