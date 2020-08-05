"""This code solves the lorentz system"""
import numpy as np

class Lorentz:
    """This is the Lorentz Class"""
    def __init__(self,x,y,z,sigma,beta,rho):
        self.x=np.array([x])
        self.y=np.array([y])
        self.z=np.array([z])
        self.sigma=sigma
        self.beta=beta
        self.rho=rho
    def time_step(self,dt):
        """This calculate the next step"""
        x1=self.x[-1]
        y1=self.y[-1]
        z1=self.z[-1]

        dx=self.sigma*(y1-x1)
        dy=x1*(self.rho-z1)-y1
        dz=x1*y1-self.beta*z1

        self.x=np.append(self.x,x1+dx*dt)
        self.y=np.append(self.y,y1+dy*dt)
        self.z=np.append(self.z,z1+dz*dt)
