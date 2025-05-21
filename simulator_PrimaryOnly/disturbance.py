import numpy as np

def generate_disturbance(time_array, times, magnitudes):
    """
    Create a disturbance signal over the simulation time.
    Args:
        time_array: full simulation time array
        times: list of times when disturbances occur
        magnitudes: list of disturbance magnitudes (same length as times)
    Returns:
        disturbance array (same length as time_array)
    """
    disturbance = np.zeros_like(time_array)
    for t, m in zip(times, magnitudes):
        disturbance[time_array >= t] += m
    return disturbance