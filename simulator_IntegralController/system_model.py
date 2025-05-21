import numpy as np
from config import Tg, Tt, Tp, Kp, R

def lfc_ode(t, y, disturbance_func, controller):
    """
    State vector y = [Δf, ΔPm, ΔPt, integral of Δf]
    """
    delta_f, delta_Pm, delta_Pt, integral_error = y
    delta_Pload = disturbance_func(t)

    # Secondary control (integral)
    control_signal = controller.update(-delta_f)

    # Governor with secondary control input
    dPm_dt = (-delta_Pm + (-delta_f / R) + control_signal) / Tg

    # Turbine dynamics
    dPt_dt = (-delta_Pt + delta_Pm) / Tt

    # Power system frequency response
    df_dt = (Kp / Tp) * (delta_Pt - delta_Pload) - (delta_f / Tp)

    # Integral of frequency error for info/logging
    dintegral_error_dt = -delta_f

    return [df_dt, dPm_dt, dPt_dt, dintegral_error_dt], control_signal