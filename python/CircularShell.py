
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Reads the number of points from the user
N = int(input("Enter the number of points to sample: "))
# The x, y, x components of the points as arrays of uniform random numbers
x = np.random.rand(1,N)
y = np.random.rand(1,N)
z = np.random.rand(1,N)
# Defines empty arrays for points that pass the criteria
xa = []
ya = []
za = []
# Defines empty arrays for points that do not pass the criteria
xm = []
ym = []
zm = []
# Evaluate the Spherical shell condition 
for i in range(0,N):
	if 0.4 < x[0,i]*x[0,i]+y[0,i]*y[0,i] + z[0,i]*z[0,i] < 0.95:
		xa.append(x[0,i])
		ya.append(y[0,i])
		za.append(z[0,i])
	else:
		xm.append(x[0,i])
		ym.append(y[0,i])
		zm.append(z[0,i])
print("The efficiency was: ", len(xa)/N)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xa,ya,za)
ax.scatter(xm,ym,zm)
plt.show()

