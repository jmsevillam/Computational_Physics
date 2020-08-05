#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pylab as plt

def std_map(theta,p,K):
    p=((p+K*np.sin(theta)))
    theta=(theta+p)%(2.0*np.pi)
    return theta,p

N=2000

for K in np.linspace(0,20,51):
    print(int(K*100))
    theta=np.random.random(N)*2*np.pi
    p=2.*np.random.random(N)-1
    for t in range(1000):
        theta,p=std_map(theta,p,K*0.3)
        if K%1==0:
            plt.plot(theta,(p+np.pi)%(2.*np.pi),'.',color='k',markersize=0.01)
    if K%1==0:  
        plt.savefig(str(int(K*100)).zfill(4)+'.png')
        plt.close()
