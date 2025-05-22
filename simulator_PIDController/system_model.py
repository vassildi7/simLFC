from config import Tg, Tt, Tp, Kp, R

def lfc_ode(t, y, disturbance_func, controller):
    delta_f, delta_Pm, delta_Pt, _ = y
    delta_Pload = disturbance_func(t)

    control_signal = controller.update(-delta_f)

    dPm_dt = (-delta_Pm + (-delta_f / R) + control_signal) / Tg
    dPt_dt = (-delta_Pt + delta_Pm) / Tt
    df_dt = (Kp / Tp) * (delta_Pt - delta_Pload) - (delta_f / Tp)
    d_dummy = 0.0  # Placeholder to preserve 4th state (unused)

    return [df_dt, dPm_dt, dPt_dt, d_dummy], control_signal
