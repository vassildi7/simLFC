import matplotlib.pyplot as plt

def plot_results(time, delta_f, delta_P_load, delta_P_m, control_signal):
    plt.figure(figsize=(10, 10))

    plt.subplot(4, 1, 1)
    plt.plot(time, delta_f, label='Δf (pu)')
    plt.ylabel('Δf (pu)')
    plt.grid(True)
    plt.legend()

    plt.subplot(4, 1, 2)
    plt.plot(time, delta_P_load, label='ΔPload (pu)', color='orange')
    plt.ylabel('ΔPload (pu)')
    plt.grid(True)
    plt.legend()

    plt.subplot(4, 1, 3)
    plt.plot(time, delta_P_m, label='ΔPm (pu)', color='green')
    plt.ylabel('ΔPm (pu)')
    plt.grid(True)
    plt.legend()

    plt.subplot(4, 1, 4)
    plt.plot(time, control_signal, label='Control Signal (pu)', color='purple')
    plt.xlabel('Time (s)')
    plt.ylabel('Control (pu)')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()