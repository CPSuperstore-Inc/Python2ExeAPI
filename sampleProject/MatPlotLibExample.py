import numpy as np
import matplotlib.pylab as plot
import math as m

v = 10
g = -9.8
a = np.arange(0, 90, 15).tolist()

angles = []

for i in a:
    angles.append(m.radians(i))

t = np.linspace(0, 5, num=100)

for i in angles:
    x1 = []
    y1 = []
    for k in t:
        x = ((v*k)*np.cos(i))
        y = ((v*k)*np.sin(i))+((0.5*g)*(k**2))
        x1.append(x)
        y1.append(y)
    p = [i for i, j in enumerate(y1) if j < 0]
    for j in sorted(p, reverse=True):
        del x1[j]
        del y1[j]

    plot.plot(x1, y1)

plot.show()
