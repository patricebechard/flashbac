import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
	return 1. / (1 + np.exp(-x))

x = np.linspace(-10, 10)
y = sigmoid(x)

plt.figure(figsize=(6, 3))
plt.plot(x, y, 'b')	
plt.plot([0, 0], [0, 1], 'k:')	#hline

plt.axis([-6, 6, 0, 1])
plt.savefig('sigmoid.png')
plt.show()

