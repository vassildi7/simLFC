import matplotlib.pyplot as plt

def plot_results(time, delta_f, delta_P_load, delta_P_m, control_signal=None, title=''):
    num_plots = 3 if control_signal is None else 4
    plt.figure(figsize=(12, 2.5 * num_plots))

    plt.subplot(num_plots, 1, 1)
    plt.plot(time, delta_f, label='Δf (pu)', color='blue')
    plt.grid()
    plt.legend()

    plt.subplot(num_plots, 1, 2)
    plt.plot(time, delta_P_load, label='ΔPload (pu)', color='orange')
    plt.grid()
    plt.legend()

    plt.subplot(num_plots, 1, 3)
    plt.plot(time, delta_P_m, label='ΔPm (pu)', color='green')
    plt.grid()
    plt.legend()

    if control_signal is not None:
        plt.subplot(num_plots, 1, 4)
        plt.plot(time, control_signal, label='Control Signal (pu)', color='purple')
        plt.grid()
        plt.legend()

    plt.suptitle(title)
    plt.xlabel('Time (s)')
    plt.tight_layout()
    plt.show()
