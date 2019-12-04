#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import matplotlib.pylab as plt


# In[8]:


N= 10**5
xk=np.loadtxt("valores.txt")


# In[9]:


def f(xk,sigma):
    return np.exp((-xk**2)/(2*sigma**2))/(sigma*np.sqrt(2*np.pi))
def mh(N,xk,sigma):
    x1=np.random.random()*np.mean(xk)
    data= np.array([])
    data= np.append(data,x1)
    for i in range(N-1):
        x2=  x1+(sigma*(np.random.random()-0.5))
        r= min(1,f(x2,1.0)/f(x1,1.0))
        alpha= np.random.random()
        if(alpha<r):
            data= np.append(data,x2)
        else:
            data= np.append(data,x1)
    return data


# In[10]:


data= mh(N,xk,1.0)


# In[11]:


_=plt.hist(data,density=True,color="green")
plt.title("$X_k$= "+ str(round(np.mean(xk),2))+"      $\sigma$= "+str(1.0))
plt.savefig("sigma.png")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




