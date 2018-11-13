import numpy as np 
import matplotlib.pyplot as plt 
from numpy.random import uniform
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

np.random.seed(69)

dom = np.arange(11)

training = 1 / dom
test = 0.05 * (dom-5)**2 + 0.5
training[0] = test[0]

training /= 2 *np.max(training)
test /= 2 * np.max(test)

noise_training = uniform(0.9, 1.1, len(training))
noise_test = uniform(0.9, 1.1, len(test))

training = training * noise_training
test = test * noise_test

min_test = np.argmin(test)

plt.figure(figsize=(8,3))
plt.plot(dom, training, 'rs-', label="Ensemble d'entraînement")
plt.plot(dom, test, 'bv-', label="Ensemble de test")
plt.plot([min_test, min_test], [0, 1], 'k:')	#h line

plt.axis([0, len(dom), 0, 0.6])
plt.xlabel("Temps d'entraînement")
plt.ylabel('Perte')

text_pos_x_under = min_test * 0.25
text_pos_y_under = 0.55
text_pos_x_over = min_test + min_test * 0.33
text_pos_y_over = 0.55
plt.text(text_pos_x_under, text_pos_y_under, 'Sous-entraînement', color='r')
plt.text(text_pos_x_over, text_pos_y_over, 'Sur-entraînement', color='r')
plt.legend(fancybox=True, loc=5)

plt.savefig('learning_curve.png')

plt.show()