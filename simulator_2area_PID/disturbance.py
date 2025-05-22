import numpy as np

def generate_disturbance(t_eval, times, magnitudes):
    disturbance = np.zeros_like(t_eval)
    for time, mag in zip(times, magnitudes):
        idx = np.searchsorted(t_eval, time)
        disturbance[idx:] += mag
    return disturbance
