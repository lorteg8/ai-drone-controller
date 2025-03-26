import numpy as np
import matplotlib.pyplot as plt

data = np.load("results/hover_data.npz")
t = data["t"]
z = data["z"]

plt.figure()
plt.plot(t, z, label="Altitude (PID + Wind)")
plt.axhline(1.0, color='r', linestyle='--', label="Target")
plt.xlabel("Time [s]")
plt.ylabel("Altitude [m]")
plt.title("PID Controller Hover Under Wind Disturbance")
plt.legend()
plt.grid(True)
plt.savefig("results/hover_pid_vs_wind.png")
plt.show()

