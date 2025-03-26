import numpy as np
import matplotlib.pyplot as plt

# Sim parameters
dt = 0.05
T = 10
steps = int(T / dt)

# Drone state
z = 0      # vertical position
v = 0      # vertical velocity

# PID parameters
Kp = 3.0
Ki = 1.0
Kd = 2.0

target_z = 1.0
error_sum = 0
last_error = 0

# Data storage
z_log = []
t_log = []

for step in range(steps):
    t = step * dt

    # Wind disturbance (simulate upward gusts)
    wind = np.random.normal(0, 0.2)

    # PID control
    error = target_z - z
    error_sum += error * dt
    d_error = (error - last_error) / dt
    u = Kp * error + Ki * error_sum + Kd * d_error
    last_error = error

    # Physics update
    a = u + wind - 9.81  # thrust + wind - gravity
    v += a * dt
    z += v * dt

    # Log
    z_log.append(z)
    t_log.append(t)

# Save data for plotting
np.savez("results/hover_data.npz", t=t_log, z=z_log)

