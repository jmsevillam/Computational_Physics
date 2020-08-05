#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pylab as plt
import matplotlib as mpl
mpl.rcParams['mathtext.fontset'] = 'cm'

def timestep(q1,p1):
    a3=[0.78451361047756, 0.23557321335936, -1.1776799841789, 1.3151863206839,-1.1776799841789,0.23557321335936,0.78451361047756,0.0]
    b3=[0.39225680523878, 0.51004341191846,-0.47105338540976, 0.068753168252520, 0.068753168252520, -0.47105338540976, 0.51004341191846, 0.39225680523878]
    for i in range(len(a3)):
        q1+=b3[i]*dt*dhdp(q1,p1)
        p1-=a3[i]*dt*dhdq(q1,p1)
    return q1,p1

D=15.
a=0.18
m=1.
dt=0.1
def H1(q1,p1):
    return (p1**2.)/(2.*m)+D*(1.-np.exp(-a*q1))**2
def V(q1,D1,a1):
    return D1*(1.-np.exp(-a1*q1))**2
#definition of dh/dp
def dhdp(q1,p1):
    #return 2.*p1
    return p1/m
#definition of dh/dq
def dhdq(q1,p1):
    #return -(-4.*q1+4.*q1**3.)
    return 2.*a*D*(1.-np.exp(-a*q1))*np.exp(-a*q1)

def Gauss(q,q0,p,p0,sigma):
    return np.exp(-0.5*((q-q0)**2+(p-p0)**2)/(sigma**2))

q0=np.linspace(-6,8,201)
p0=np.linspace(-6,6,201)
q0_bin=np.linspace(-6,8,101)
p0_bin=np.linspace(-6,6,101)

Q0,P0=np.meshgrid(q0,p0)
Q,P=np.meshgrid(q0,p0)

rho=Gauss(Q0,4,P0,0,1)
for i in range(100):
    print(i)
    Q,P=timestep(Q,P)

rho0=Gauss(Q,4,P,0,1)
fig=plt.figure(figsize=(9,4))
ax1=fig.add_subplot(121)
ax1.pcolormesh(Q0,P0,rho*0)
ax1.pcolormesh(Q,P,rho)
ax1.set_xlim(min(q0),max(q0))
ax1.set_ylim(min(p0),max(p0))
ax2=fig.add_subplot(122)
ax2.pcolormesh(Q0,P0,rho)
plt.show()
'''
H,a,b=np.histogram2d(Q.reshape(len(q0)*len(p0)),P.reshape(len(q0)*len(p0)),weights=rho.reshape(len(q0)*len(p0)),bins=(q0_bin,p0_bin))

Q,P=np.meshgrid(b[:-1],a[:-1])

rho0=Gauss(Q,4,P,0,1)
fig=plt.figure(figsize=(9,4))
ax1=fig.add_subplot(121)
ax1.pcolormesh(Q,P,H.T)
ax2=fig.add_subplot(122)
ax2.pcolormesh(Q0,P0,rho)
plt.show()
'''
