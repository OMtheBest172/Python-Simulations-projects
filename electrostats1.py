import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


k = 9e9
q1, q2, q3 = 1e-6, -1e-6, 1e-6
m1, m2, m3 = 1e-3, 1e-3, 1e-3

r1 = np.array([0.0, 0.0])
r2 = np.array([0.1, 0.1])

v1, v2 = np.array([1.4, 0.0]), np.array([0.0, 1.4])

dt = 1e-5
steps = 10000

r1_list, r2_list = [], []

for i in range(steps):
    r_vec = r1- r2
    distance = np.linalg.norm(r_vec)
    
    r_hat = r_vec/distance
    
    f_mag = k*q1*q2/distance**2
    F = f_mag * r_hat
    
    a1 = F/m1
    a2 = -F/m2
    
    v1 = v1 + a1*dt
    v2 = v2 + a2*dt
    
    r1 = r1 + v1*dt
    r2 = r2 + v2*dt
    if distance < 1e-9:
        break 
    
    r1_list.append(r1.copy())
    r2_list.append(r2.copy())
   
r1_array = np.array(r1_list)
r2_array = np.array(r2_list)

fig, ax = plt.subplots()
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_title('2D Electrostatic Interaction Animation')
ax.grid(True)
ax.axis('equal')


x_vals = np.concatenate((r1_array[:, 0], r2_array[:, 0]))
y_vals = np.concatenate((r1_array[:, 1], r2_array[:, 1]))
ax.set_xlim(x_vals.min() - 0.01, x_vals.max() + 0.01)
ax.set_ylim(y_vals.min() - 0.01, y_vals.max() + 0.01)

line1, = ax.plot([], [], 'b-', label='Particle 1 Path')
line2, = ax.plot([], [], 'r-', label='Particle 2 Path')
point1, = ax.plot([], [], 'bo')  # Current position of Particle 1
point2, = ax.plot([], [], 'ro')  # Current position of Particle 2

ax.legend()

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    point1.set_data([], [])
    point2.set_data([], [])
    return line1, line2, point1, point2

def update(frame):
    line1.set_data(r1_array[:frame, 0], r1_array[:frame, 1])
    line2.set_data(r2_array[:frame, 0], r2_array[:frame, 1])
    point1.set_data([r1_array[frame, 0]], [r1_array[frame, 1]])
    point2.set_data([r2_array[frame, 0]], [r2_array[frame, 1]])
    return line1, line2, point1, point2

anim = FuncAnimation(fig, update, frames=len(r1_array), init_func=init, blit=True, interval=1)
plt.show()