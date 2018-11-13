import numpy as np 
from sklearn import linear_model
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt



boston = load_boston()
reg = linear_model.LinearRegression()

features = np.expand_dims(boston.data[:,5], axis=1)
labels = boston.target

reg.fit(features, labels)

plt.figure(figsize=(4, 6))
plt.plot(features, labels, '.')
plt.plot(np.arange(11), reg.coef_ * np.arange(11) + reg.intercept_, 'r')

plt.xlabel('Nb. moyen de chambres par habitation')
plt.ylabel('Prix médian des maisons (en 1000$)')
plt.axis([0.9*np.min(features), 1.1*np.max(features), 0, 1.1*np.max(labels)])
plt.savefig('boston.png')
plt.show()
