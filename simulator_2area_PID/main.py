import numpy as np
from config import time_step, default_duration, Kp1, Ki1, Kd1, Kp2, Ki2, Kd2
from disturbance import generate_disturbance
from system_model import lfc_ode_2area
from controller import PIDController
from plot_utils import plot_results

def rk4_step(f, t, y, h):
    y = np.asarray(y)
    k1 = np.asarray(f(t, y))
    k2 = np.asarray(f(t + h/2, y + h/2 * k1))
    k3 = np.asarray(f(t + h/2, y + h/2 * k2))
    k4 = np.asarray(f(t + h, y + h * k3))
    return y + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)

def simulate(duration=default_duration, disturbance_times=[20, 50], disturbance_mags1=[0.02, 0.00], disturbance_mags2=[0.0, -0.03]):
    t_vals = np.arange(0, duration, time_step)
    n_steps = len(t_vals)

    disturbance1 = generate_disturbance(t_vals, disturbance_times, disturbance_mags1)
    disturbance2 = generate_disturbance(t_vals, disturbance_times, disturbance_mags2)
    disturbance_func1 = lambda t: np.interp(t, t_vals, disturbance1)
    disturbance_func2 = lambda t: np.interp(t, t_vals, disturbance2)

    # Initial state: [Δf1, ΔPm1, ΔPt1, Δf2, ΔPm2, ΔPt2, ΔPtie]
    y = np.zeros((n_steps, 7))
    y[0] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    # Controllers for each area
    ctrl1 = PIDController(Kp1, Ki1, Kd1, time_step)
    ctrl2 = PIDController(Kp2, Ki2, Kd2, time_step)
    ctrl1.reset()
    ctrl2.reset()

    control_log_1 = np.zeros(n_steps)
    control_log_2 = np.zeros(n_steps)

    for i in range(1, n_steps):
        t = t_vals[i-1]
        y_prev = y[i-1]
        dydt_func = lambda t, y: lfc_ode_2area(t, y, disturbance_func1, disturbance_func2, ctrl1, ctrl2)[0]
        y[i] = rk4_step(dydt_func, t, y_prev, time_step)
        _, u1, u2 = lfc_ode_2area(t, y_prev, disturbance_func1, disturbance_func2, ctrl1, ctrl2)
        control_log_1[i] = u1
        control_log_2[i] = u2

    delta_f1 = y[:, 0]
    delta_f2 = y[:, 3]
    delta_Ptie = y[:, 6]

    plot_results(t_vals, delta_f1, delta_f2, delta_Ptie, control_log_1, control_log_2, disturbance1, disturbance2)


if __name__ == '__main__':
    simulate()
