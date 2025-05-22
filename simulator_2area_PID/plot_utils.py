import matplotlib.pyplot as plt

def plot_results(time, delta_f1, delta_f2, delta_Ptie, u1, u2, dPload1, dPload2):
    plt.figure(figsize=(12, 14))

    plt.subplot(7, 1, 1)
    plt.plot(time, delta_f1, label='Δf1 (pu)', color='blue')
    plt.grid()
    plt.legend()

    plt.subplot(7, 1, 2)
    plt.plot(time, delta_f2, label='Δf2 (pu)', color='green')
    plt.grid()
    plt.legend()

    plt.subplot(7, 1, 3)
    plt.plot(time, dPload1, label='ΔPload1 (pu)', color='darkorange')
    plt.grid()
    plt.legend()

    plt.subplot(7, 1, 4)
    plt.plot(time, dPload2, label='ΔPload2 (pu)', color='orangered')
    plt.grid()
    plt.legend()

    plt.subplot(7, 1, 5)
    plt.plot(time, delta_Ptie, label='ΔPtie (pu)', color='red')
    plt.grid()
    plt.legend()

    plt.subplot(7, 1, 6)
    plt.plot(time, u1, label='Control Area 1', color='purple')
    plt.grid()
    plt.legend()

    plt.subplot(7, 1, 7)
    plt.plot(time, u2, label='Control Area 2', color='orange')
    plt.grid()
    plt.legend()

    plt.xlabel('Time (s)')
    plt.suptitle('Two-Area LFC with PID Controllers and Load Disturbances')
    plt.tight_layout()
    plt.show()
