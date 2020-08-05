import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import curve_fit
from mpl_toolkits.mplot3d import Axes3D
import lorentz as lo

sis1=lo.Lorentz(1.0,1.0,1.0,10.0,8.0/3.0,28.0)
sis2=lo.Lorentz(1.1,1.0,1.0,10.0,8.0/3.0,28.0)

time=np.array([0])
for i in range(10000):
    sis1.time_step(0.01)
    sis2.time_step(0.01)
    time=np.append(time,(i+1)*0.01)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(sis1.x,sis1.y,sis1.z,'ok',markersize=.1)
ax.plot(sis2.x,sis2.y,sis2.z,'or',markersize=.1)
plt.show()

dis=np.sqrt((sis1.x-sis2.x)**2+(sis1.y-sis2.y)**2+(sis1.z-sis2.z)**2)

def f(x,a,b):
    return a*np.exp(b*x)

popt,pcov=curve_fit(f,time[300:800],dis[300:800])

plt.plot(time,dis)
plt.plot(time,f(time,*popt))
plt.yscale('log')
plt.show()
