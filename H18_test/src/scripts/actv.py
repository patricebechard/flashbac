import numpy as np 
import matplotlib.pyplot as plt 


x = np.linspace(-6, 6, 1000)

#linear
y1 = x
plt.plot(x, y1)
plt.plot([-6, 6], [0, 0], 'k:')
plt.plot([0, 0], [-6, 6], 'k:')
plt.axis([-6, 6, -6, 6])
plt.xlabel('x')
plt.ylabel('g(x)')
plt.savefig('linear.png')
plt.clf()

#sigmoid
y2 = 1 / (1 + np.exp(-x))
plt.plot(x, y2)
plt.plot([-6, 6], [0, 0], 'k:')
plt.plot([0, 0], [-6, 6], 'k:')
plt.axis([-6, 6, -0.5, 1.5])
plt.xlabel('x')
plt.ylabel('g(x)')
plt.savefig('sigmoid.png')
plt.clf()

#tanh
y3 = np.tanh(x)
plt.plot(x, y3)
plt.plot([-6, 6], [0, 0], 'k:')
plt.plot([0, 0], [-6, 6], 'k:')
plt.axis([-6, 6, -1.5, 1.5])
plt.xlabel('x')
plt.ylabel('g(x)')
plt.savefig('tanh.png')
plt.clf()

#relu
y4 = np.maximum(np.zeros_like(x), x)
plt.plot(x, y4)
plt.plot([-6, 6], [0, 0], 'k:')
plt.plot([0, 0], [-6, 6], 'k:')
plt.axis([-6, 6, -1, 6])
plt.xlabel('x')
plt.ylabel('g(x)')
plt.savefig('relu.png')
plt.clf()
