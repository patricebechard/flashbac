import numpy as np 
import matplotlib.pyplot as plt 

n_pts = 100

#class 1
datapts1 = np.random.uniform(-1, 0, (n_pts,2))
datapts2 = np.random.uniform(0, 1, (n_pts,2))

#class 2
datapts3 = np.zeros((n_pts, 2))
datapts4 = np.zeros((n_pts, 2))
datapts3[:,0] = np.random.uniform(0, 1, n_pts)
datapts3[:,1] = np.random.uniform(-1, 0, n_pts)
datapts4[:,0] = np.random.uniform(-1, 0, n_pts)
datapts4[:,1] = np.random.uniform(0, 1, n_pts)

plt.figure(figsize=(6, 6))
plt.plot(datapts1[:,0], datapts1[:,1], 'rs')
plt.plot(datapts2[:,0], datapts2[:,1], 'rs')
plt.plot(datapts3[:,0], datapts3[:,1], 'bv')
plt.plot(datapts4[:,0], datapts4[:,1], 'bv')
plt.axis([-1, 1, -1, 1])

plt.savefig('xor.png')
plt.clf()

def change_coord(datapts):
	newdatapts = np.zeros((n_pts, 2))
	temp = datapts[:,0] * datapts[:,1]
	newdatapts[:,0] = temp
	newdatapts[:,1] = temp
	return newdatapts

datapts1 = change_coord(datapts1)
datapts2 = change_coord(datapts2)
datapts3 = change_coord(datapts3)
datapts4 = change_coord(datapts4)

plt.figure(figsize=(6, 6))
plt.plot(datapts1[:,0], datapts1[:,1], 'rs')
plt.plot(datapts2[:,0], datapts2[:,1], 'rs')
plt.plot(datapts3[:,0], datapts3[:,1], 'bv')
plt.plot(datapts4[:,0], datapts4[:,1], 'bv')
plt.axis([-1, 1, -1, 1])
plt.savefig('xor_transform.png')
