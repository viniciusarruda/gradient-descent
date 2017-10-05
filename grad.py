
import matplotlib.pyplot as plt
import numpy as np
import random

plt.ion()

E = lambda x: x*x
dE = lambda x: 2*x

x = np.linspace(-10.0, 10.0, num=100)
y = [E(e) for e in x]
dy = [dE(e) for e in x]

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'r-') # Returns a tuple of line objects, thus the comma

t = 9.0 #random.uniform(-10.0, 10.0)
eta = 0.2

# plt.plot(x, dy, 'b')
# plt.show()

y1 = y2 = 0.0
x1 = x2 = 0.0


for i in xrange(10):
    ax.clear()
    e = E(t)
    print 'it#{} ploting ({}, {})'.format(i, t, e)
    plt.plot(x, y, 'r')
    plt.plot(t, e, 'bo')
    fig.canvas.draw()
    plt.pause(2)

    y1 = e
    x1 = t
    b = t
    a = dE(t)
    t -= eta * a
    y2  = E(t)
    x2 = t

    tmpx = np.linspace(x1, x2, num = 100)
    tmpy = [i * ((y2 - y1) / (x2 - x1)) - y2 for i in tmpx]
    print y1, y2
    plt.plot(tmpx, tmpy, 'g');
    fig.canvas.draw()
    plt.pause(2)


plt.pause(1000)
