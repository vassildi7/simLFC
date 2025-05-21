import numpy as np
from config import Tg, Tt, Tp, Kp, R

def lfc_ode(t, y, disturbance_func):
    """
    Differential equations for single-area LFC with primary control only.
    State vector y = [Δf, ΔPm, ΔPt]
    """
    delta_f, delta_Pm, delta_Pt = y
    delta_Pload = disturbance_func(t)

    # Governor: d(ΔPm)/dt = (-ΔPm + (-Δf / R)) / Tg
    dPm_dt = (-delta_Pm + (-delta_f / R)) / Tg

    # Turbine: d(ΔPt)/dt = (-ΔPt + ΔPm) / Tt
    dPt_dt = (-delta_Pt + delta_Pm) / Tt

    # Power system: d(Δf)/dt = (Kp/Tp) * (ΔPt - ΔPload) - (Δf / Tp)
    df_dt = (Kp / Tp) * (delta_Pt - delta_Pload) - (delta_f / Tp)

    return [df_dt, dPm_dt, dPt_dt]