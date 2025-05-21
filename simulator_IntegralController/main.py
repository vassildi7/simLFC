import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
from config import time_step, default_duration, Ki
from disturbance import generate_disturbance
from system_model import lfc_ode
from controller import IntegralController
from plot_utils import plot_results

def simulate(duration=default_duration, disturbance_times=[10, 30], disturbance_mags=[0.01, -0.015]):
    t_eval = np.arange(0, duration, time_step)
    disturbance_array = generate_disturbance(t_eval, disturbance_times, disturbance_mags)
    disturbance_func = lambda t: np.interp(t, t_eval, disturbance_array)

    # Initial state: Δf=0, ΔPm=0, ΔPt=0, integral error=0
    y0 = [0.0, 0.0, 0.0, 0.0]

    controller = IntegralController(Ki, time_step)
    control_signal_log = []
    time_log = []

    def ode_wrapped(t, y):
        dydt, u = lfc_ode(t, y, disturbance_func, controller)
        control_signal_log.append(u)
        time_log.append(t)
        return dydt

    sol = solve_ivp(fun=ode_wrapped, t_span=(0, duration), y0=y0, t_eval=t_eval, method='RK45')

    delta_f = sol.y[0]
    delta_P_m = sol.y[1]
    delta_P_load = disturbance_array

    # Interpolate control signal to match sol.t
    raw_times = np.array(time_log)
    raw_control = np.array(control_signal_log)
    interp_func = interp1d(raw_times, raw_control, kind='linear', fill_value='extrapolate')
    control_signal = interp_func(sol.t)

    plot_results(sol.t, delta_f, delta_P_load, delta_P_m, control_signal)

if __name__ == '__main__':
    simulate()