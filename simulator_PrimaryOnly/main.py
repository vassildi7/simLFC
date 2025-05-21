import numpy as np
from scipy.integrate import solve_ivp
from config import time_step, default_duration
from disturbance import generate_disturbance
from system_model import lfc_ode
from plot_utils import plot_results

def simulate(duration=default_duration, disturbance_times=[10, 30], disturbance_mags=[0.01, -0.015]):
    t_eval = np.arange(0, duration, time_step)

    # Create load disturbance signal
    disturbance_array = generate_disturbance(t_eval, disturbance_times, disturbance_mags)
    disturbance_func = lambda t: np.interp(t, t_eval, disturbance_array)

    # Initial state: Δf=0, ΔPm=0, ΔPt=0
    y0 = [0.0, 0.0, 0.0]

    # Solve ODEs
    sol = solve_ivp(fun=lambda t, y: lfc_ode(t, y, disturbance_func),
                    t_span=(0, duration),
                    y0=y0, t_eval=t_eval, method='RK45')

    delta_f = sol.y[0]
    delta_P_m = sol.y[1]
    delta_P_load = disturbance_array

    # Plot results
    plot_results(sol.t, delta_f, delta_P_load, delta_P_m)

if __name__ == '__main__':
    simulate()