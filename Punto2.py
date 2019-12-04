#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pylab as plt


# In[4]:


data= np.loadtxt("monthrg.dat")
años= data[:,0]
mes= data[:,1]
n_dia= data[:,2]
manchas= data[:,3]


# In[34]:


icrit=0
for i in range(len(años)):
    if(años[i]==1940):
        icrit= i
print(icrit)

i_1900= 3491
i_1930= 3851
i_1940= 3971
i_1950= 4091
#se busca un intervalo en el cual haya solo dos mínimos, en este caso entre 1930 y 1940


# In[56]:


mp= manchas[i_1930:i_1940]
ap= años[i_1930:i_1940]
vmin=10000
for i in range(len(mp)):
    if(vmin>mp[i]):
        vmin= mp[i]
        print(ap[i])
# en 1933 coomienza un período porque hay un punto mínimo


# In[57]:


mp= manchas[i_1930:i_1950]
ap= años[i_1930:i_1950]
vmin=10000
for i in range(len(mp)):
    if(vmin>mp[i]):
        vmin= mp[i]
        print(ap[i])
# en 1944 comienza otro período porque hay un punto máximo


# In[55]:


plt.plot(años[3491:],manchas[3491:],c="green")
plt.plot(años[3491:],(np.sin(años[3491:]*2*np.pi/11)*75)+75,label="Seno con período de 11 años",c="blue")
plt.title("Manchas solares desde 1900")
plt.xlabel("tiempo $(yr)$")
plt.ylabel("Número de manchas solares")
plt.legend()
plt.savefig("solar.png")
plt.show()


# In[ ]:




