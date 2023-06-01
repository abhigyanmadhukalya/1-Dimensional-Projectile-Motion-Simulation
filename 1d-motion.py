import numpy as np 
import matplotlib.pylab as plot
from math import pi

# Initialise Constants and Variables
initial_velocity = float(input("Enter the velocity of particle (in m/s): "))
G = 9.81
theta = np.arange(pi/6, pi/3, pi/36)
t = np.linspace(0, 5, num=100) # Set time as a 'continous' parameter

for i in theta:
    x1 = []
    y1 = []
    for k in  t:
        x = ((initial_velocity*k)*np.cos(i)) # get positions at every point in time
        y = ((initial_velocity*k)*np.sin(i))-((0.5*G)*(k**2))
        x1.append(x)
        y1.append(y)
    p = [i for i, j in enumerate(y1) if j < 0] # Don't fall through the floor                          
    for i in sorted(p, reverse = True):
        del x1[i]
        del y1[i]
    plot.plot(x1, y1)

plot.show()

