#1D Heat Equation Numerical Simulation
import numpy as np
import matplotlib.pyplot as plt


#Defining the properties of rod

a = 110
length = 50 #mm
time = 4 #seconds
nodes = 20

# Initialization 

dx = length / (nodes-1)
dt = 0.5 * dx**2 / a
t_nodes = int(time/dt) + 1

u = np.zeros(nodes) + 20  #20 degree celcius of all points of a node to make inital temeprature of rod constant

u[0] = 100
u[-1] = 100


# Visualization

fig, axis = plt.subplots()

pcm = axis.pcolormesh([u], cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=axis)
axis.set_ylim([-2, 3])

# Simulation

counter = 0
#frame = 0

while counter < time :

    w = u.copy()

    for i in range(1, nodes - 1):

        u[i] = dt * a * (w[i - 1] - 2 * w[i] + w[i + 1]) / dx ** 2 + w[i]
        #w[i - 1] - 2 * w[i] + w[i + 1], its a mathematical tricks this tells us that how bent(u or ∩) the temperature is at that w[i] point
        #dt * a * (....)/dx**2, this tells us how much heat moves in one time step or How sensitive your system is to this imbalance
        #+w[i] adds the current temperature to the temperature change to get a new updated temperature

    counter += dt

    print("t: {:.3f} [s], Average temperature: {:.2f} Celcius".format(counter, np.average(u)))

    # Updating the plot

    pcm.set_array([u])
    axis.set_title("Distribution at t: {:.3f} [s].".format(counter))
    plt.pause(0.001)
    #plt.savefig(f"heat_sim_{frame:04d}.png", dpi=300)  # zero‑pad for easy sorting
    #frame += 1

plt.show()