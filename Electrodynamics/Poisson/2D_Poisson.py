#!/usr/bin/env python
# coding: utf-8
import numpy as np
import matplotlib.pylab as plt

Tolerance=0.
size=200
positive_charges=8
negative_charges=7


x_pos=np.random.randint(.05*size,.95*size,positive_charges)
y_pos=np.random.randint(.05*size,.95*size,positive_charges)

x_neg=np.random.randint(.05*size,.95*size,negative_charges)
y_neg=np.random.randint(.05*size,.95*size,negative_charges)

def geometry(mat):
    mat[:,0]=0
    mat[:,-1]=0
    mat[0,:]=0
    mat[-1,:]=0
    mat[x_pos,y_pos]=1
    mat[x_neg,y_neg]=-1

def time_step(mat):
    copia=np.zeros(mat.shape)
    copia[1:-1,1:-1]=(mat[2:,1:-1]+mat[0:-2,1:-1]+mat[1:-1,2:]+mat[1:-1,:-2])/4.
    geometry(copia)
    diff=(np.sqrt((mat-copia)**2).sum()/(100*100))
    return diff,copia

mat=2*np.random.random((size,size))-1
for t in range(1000000):
    diff,mat=time_step(mat)
    if t%5000==0:
        print(t,diff)
    if diff<=Tolerance:
        print(t,diff)
        break

pl=plt.imshow(mat,cmap='RdBu',vmin=-1,vmax=1)
plt.colorbar(pl)
plt.show()
