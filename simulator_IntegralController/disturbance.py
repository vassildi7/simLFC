import numpy as np

def generate_disturbance(time_array, times, magnitudes):
    disturbance = np.zeros_like(time_array)
    for t, m in zip(times, magnitudes):
        disturbance[time_array >= t] += m
    return disturbance
