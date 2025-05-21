import matplotlib.pyplot as plt

def plot_results(time, delta_f, delta_P_load, delta_P_m):
    plt.figure(figsize=(10, 8))

    plt.subplot(3, 1, 1)
    plt.plot(time, delta_f, label='Δf (pu)')
    plt.ylabel('Δf (pu)')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(time, delta_P_load, label='ΔPload (pu)', color='orange')
    plt.ylabel('ΔPload (pu)')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(time, delta_P_m, label='ΔPm (pu)', color='green')
    plt.xlabel('Time (s)')
    plt.ylabel('ΔPm (pu)')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()