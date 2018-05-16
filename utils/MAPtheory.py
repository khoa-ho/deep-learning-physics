
# coding: utf-8

# In[1]:

#This is the code for a nonphysical DP i didnt use our real values
#(because i dont know them  heh)
from scipy import *
from pylab import*
import matplotlib.pyplot as plt
from scipy.integrate import quad, dblquad, tplquad,odeint,ode
g = 9.81
L1 = 0.2785
L2 = 0.251
m1 = 0.399
m2 = 0.276

def dx(x, t):
    """
    The right-hand side of the pendulum ODE
    """
    x1, x2, x3, x4 = x[0], x[1], x[2], x[3]
    
    dx1 = 6.0/(m1*L1**2) * (2 * x3 - 3 * cos(x1-x2) * x4)/(16 - 9 * cos(x1-x2)**2)
    dx2 = 6.0/(m2*L2**2) * (8 * x4 - 3 * cos(x1-x2) * x3)/(16 - 9 * cos(x1-x2)**2)
    dx3 = -0.5 * m1 * L1**2 * ( dx1 * dx2 * sin(x1-x2) + 3 * (g/L1) * sin(x1))
    dx4 = -0.5 * m2 * L2**2 * (-dx1 * dx2 * sin(x1-x2) + (g/L2) * sin(x2))
    
    return [dx1, dx2, dx3, dx4]


# In[2]:

# choose an initial state
x0 = [pi/4, pi/2, 0, 0]


# In[3]:

# time coordinate to solve the ODE for: from 0 to 40 seconds
t = linspace(0, 40, 100000)


# In[4]:

# solve the ODE problem
x = odeint(dx, x0, t)


# In[5]:

fig, axes = subplots(1,2, figsize=(12,4))
axes[0].plot(t, x[:, 0], 'r', label="theta1")
axes[0].plot(t, x[:, 1], 'b', label="theta2")


# In[6]:

x1 = + L1 * sin(x[:, 0])
y1 = - L1 * cos(x[:, 0])

x2 = x1 + L2 * sin(x[:, 1])
y2 = y1 - L2 * cos(x[:, 1])
    
axes[1].plot(x1, y1, 'r', label="pendulum1")
axes[1].plot(x2, y2, 'b', label="pendulum2")
axes[1].set_ylim([-1, 0.25])
axes[1].set_xlim([-1, 1]);
show()
plt.show()


# In[7]:

# Here are the velocities: You might want to check v2 becuse I just intgrated the momentum of the second
#arm and divided by the mass.
v1=(x[:,2])/m1
v2=(x[:,3])/m2


# In[8]:

#Phase space plot of the second arm 
plt.plot(x1,v1)
show()
plt.plot(x2,v2)
show()


# In[9]:

#theta2 v theta1
th1 = x[:, 0]
th2 = x[:, 1]
plt.plot(th1,th2)
show()


# In[ ]:



