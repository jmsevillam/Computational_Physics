import numpy as np
import matplotlib.pylab as plt
import matplotlib as mpl
mpl.rcParams['mathtext.fontset'] = 'cm'
import sys

def H(q,p,t):
    return (p**2)/(2.*m)+(m*omega_0**2/2)*q**2
def dHdp(q,p,t):
    return p/m
def dHdq(q,p,t):
    return m*omega_0**2.*q

def analytic_solution(p0,q0,t):
    return np.cos(omega_0*t),-np.sin(omega_0*t)

def time_step_Euler(q,p,t,dt):

    dq=dHdp(q,p,t)*dt
    dp=-dHdq(q,p,t)*dt

    p+=dp
    q+=dq
    return q,p,t+dt

def time_step_Euler_Cromer(q,p,t,dt):
    q+=dHdp(q,p,t)*dt
    p+=-dHdq(q,p,t)*dt
    return q,p,t+dt

m=1.0
omega_0=1.
dt=0.01
names=['Euler', 'Euler-Cromer']
methods=[time_step_Euler,time_step_Euler_Cromer]
line_styles=['-','--']

fig=plt.figure(figsize=(5.4,5))
fig.subplots_adjust(right=1,top=1)
ax=fig.add_subplot(111)
ax.set_aspect('equal')

ax.set_xlabel('Position $q$')
ax.set_ylabel('Momentum $p$')
for name,method,style in zip(names,methods,line_styles):
    p=np.array([0.])
    q=np.array([1.])
    t=np.array([0.])

    for i in range(int(2.*np.pi*omega_0/dt)):
        q0,p0,t0=method(q[-1],p[-1],t[-1],dt)
        q=np.append(q,q0)
        p=np.append(p,p0)
        t=np.append(t,t0)

    ax.plot(q,p,style,label=name)

plt.plot(*analytic_solution(0,1,t[::10]),'.',marker='x',label='analytic')
plt.legend()
plt.savefig('Harmonic_Oscillator_python.png')
plt.savefig('Harmonic_Oscillator_python.pdf')
plt.show()
