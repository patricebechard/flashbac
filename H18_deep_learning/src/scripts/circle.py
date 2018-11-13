import numpy as np 
import matplotlib.pyplot as plt 

n_pts = 100

#class 1 :
radius_1 = np.random.uniform(0, 0.45, n_pts)
angle_1 = np.random.uniform(0, 2*np.pi, n_pts)

pts_1 = np.zeros((n_pts, 2))
pts_1[:,0] = radius_1 * np.cos(angle_1)
pts_1[:,1] = radius_1 * np.sin(angle_1)

#class 2 
radius_2 = np.random.uniform(0.55, 1, n_pts)
angle_2 = np.random.uniform(0, 2*np.pi, n_pts)

pts_2 = np.zeros((n_pts, 2))
pts_2[:,0] = radius_2 * np.cos(angle_2)
pts_2[:,1] = radius_2 * np.sin(angle_2)

plt.tight_layout()

plt.figure(figsize=(6, 6))
plt.plot(pts_1[:,0], pts_1[:,1], 'rs')
plt.plot(pts_2[:,0], pts_2[:,1], 'bv')

plt.axis([-1, 1, -1, 1],)
plt.savefig('circle.png')

def change_coord(datapts):
	newdatapts = np.zeros((n_pts, 2))
	newdatapts[:,0] = np.sqrt(datapts[:,0]**2 + datapts[:,1]**2)
	newdatapts[:,1] = np.arctan(datapts[:,1] / datapts[:,0])
	return newdatapts

pts_1 = change_coord(pts_1)
pts_2 = change_coord(pts_2)

plt.figure(figsize=(6, 6))
plt.plot(pts_1[:,0], pts_1[:,1], 'rs')
plt.plot(pts_2[:,0], pts_2[:,1], 'bv')

#plt.axis([0, np.sqrt(2), 0, 2*np.pi],)
plt.savefig('circle_transform.png')


		