import numpy as np
from config import time_step, default_duration, Kp_pid, Ki_pid, Kd_pid
from disturbance import generate_disturbance
from system_model import lfc_ode
from controller import PIDController
from plot_utils import plot_results

# Fixed-step RK4
def rk4_step(f, t, y, h):
    y = np.asarray(y)
    k1 = np.asarray(f(t, y))
    k2 = np.asarray(f(t + h/2, y + h/2 * k1))
    k3 = np.asarray(f(t + h/2, y + h/2 * k2))
    k4 = np.asarray(f(t + h, y + h * k3))
    return y + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)

def simulate(duration=default_duration, disturbance_times=[20], disturbance_mags=[0.02]):
    t_vals = np.arange(0, duration, time_step)
    n_steps = len(t_vals)

    disturbance_array = generate_disturbance(t_vals, disturbance_times, disturbance_mags)
    disturbance_func = lambda t: np.interp(t, t_vals, disturbance_array)

    y = np.zeros((n_steps, 4))  # [Δf, ΔPm, ΔPt, integral_error]
    y[0] = [0.0, 0.0, 0.0, 0.0]

    controller = PIDController(Kp_pid, Ki_pid, Kd_pid, time_step)
    controller.reset()

    control_signal_log = np.zeros(n_steps)

    for i in range(1, n_steps):
        t = t_vals[i-1]
        y_prev = y[i-1]
        dydt_func = lambda t, y: lfc_ode(t, y, disturbance_func, controller)[0]
        y[i] = rk4_step(dydt_func, t, y_prev, time_step)
        _, control_signal = lfc_ode(t, y_prev, disturbance_func, controller)
        control_signal_log[i] = control_signal

    delta_f = y[:, 0]
    delta_P_m = y[:, 1]
    delta_P_load = disturbance_array

    plot_results(t_vals, delta_f, delta_P_load, delta_P_m, control_signal_log, title='LFC with PID Controller')

if __name__ == '__main__':
    simulate()
