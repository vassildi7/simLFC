from config import Tg, Tt, Tp, Kp, R, T12

def lfc_ode_2area(t, y, disturbance1, disturbance2, ctrl1, ctrl2):
    delta_f1, delta_Pm1, delta_Pt1, delta_f2, delta_Pm2, delta_Pt2, delta_Ptie = y

    dPload1 = disturbance1(t)
    dPload2 = disturbance2(t)

    # Control signals
    u1 = ctrl1.update(-delta_f1)
    u2 = ctrl2.update(-delta_f2)

    # Tie-line power flow: positive when power flows from area 1 to 2
    dPtie_dt = T12 * (delta_f1 - delta_f2)

    # Area 1 dynamics
    dPm1_dt = (-delta_Pm1 + (-delta_f1 / R) + u1) / Tg
    dPt1_dt = (-delta_Pt1 + delta_Pm1) / Tt
    df1_dt = (Kp / Tp) * (delta_Pt1 - dPload1 - delta_Ptie) - (delta_f1 / Tp)

    # Area 2 dynamics
    dPm2_dt = (-delta_Pm2 + (-delta_f2 / R) + u2) / Tg
    dPt2_dt = (-delta_Pt2 + delta_Pm2) / Tt
    df2_dt = (Kp / Tp) * (delta_Pt2 - dPload2 + delta_Ptie) - (delta_f2 / Tp)

    dydt = [df1_dt, dPm1_dt, dPt1_dt, df2_dt, dPm2_dt, dPt2_dt, dPtie_dt]
    return dydt, u1, u2
