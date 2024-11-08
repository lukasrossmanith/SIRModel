import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# tkinter application of everything before 

def run_simulation():
    beta = float(beta_entry.get())
    gamma = float(gamma_entry.get())
    N = float(N_entry.get())
    I0 = float(I0_entry.get())
    T = float(T_entry.get())
    Nt = int(Nt_entry.get())

    # time steps
    dt = T / Nt
    t = np.linspace(0, T, Nt + 1)

    # initializing arrays
    S = np.zeros(Nt + 1)
    I = np.zeros(Nt + 1)
    R = np.zeros(Nt + 1)

    # starting values
    S[0] = N - I0
    I[0] = I0
    R[0] = 0

    # simulation of SIR model
    for n in range(Nt):
        S[n + 1] = S[n] - dt * (beta * I[n] * S[n]) / N
        I[n + 1] = I[n] + dt * ((beta * I[n] * S[n]) / N - gamma * I[n])
        R[n + 1] = R[n] + dt * gamma * I[n]
        
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(t, S, label='S(t) - Susceptible')
    ax.plot(t, I, label='I(t) - Infectious')
    ax.plot(t, R, label='R(t) - Removed')
    ax.set_xlabel('Time (days)')
    ax.set_ylabel('Population')
    ax.set_title('SIR Model Simulation')
    ax.legend()
    ax.grid()

    for widget in plot_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# create tkinter window
root = tk.Tk()
root.title("SIR Model Simulation")

tk.Label(root, text="Beta:").grid(row=0, column=0)
beta_entry = tk.Entry(root)
beta_entry.grid(row=0, column=1)
beta_entry.insert(0, "0.2")

tk.Label(root, text="Gamma:").grid(row=1, column=0)
gamma_entry = tk.Entry(root)
gamma_entry.grid(row=1, column=1)
gamma_entry.insert(0, "0.05")

tk.Label(root, text="N:").grid(row=2, column=0)
N_entry = tk.Entry(root)
N_entry.grid(row=2, column=1)
N_entry.insert(0, "80000000")

tk.Label(root, text="I0:").grid(row=3, column=0)
I0_entry = tk.Entry(root)
I0_entry.grid(row=3, column=1)
I0_entry.insert(0, "1")

tk.Label(root, text="T:").grid(row=4, column=0)
T_entry = tk.Entry(root)
T_entry.grid(row=4, column=1)
T_entry.insert(0, "730")

tk.Label(root, text="Nt:").grid(row=5, column=0)
Nt_entry = tk.Entry(root)
Nt_entry.grid(row=5, column=1)
Nt_entry.insert(0, "1000")

simulate_button = tk.Button(root, text="Run Simulation", command=run_simulation)
simulate_button.grid(row=6, column=0, columnspan=2)

plot_frame = tk.Frame(root)
plot_frame.grid(row=7, column=0, columnspan=2)

root.mainloop()
