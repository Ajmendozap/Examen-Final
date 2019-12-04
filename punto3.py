import numpy as np
import matplotlib.pylab as plt


data2= np.loadtxt("ci.dat")

plt.figure(figsize=(15,15))
plt.subplot(2,2,1)

plt.subplot(2,2,2)
plt.plot(data2[:,0],data2[:,1],label="condiciones iniciales")
plt.legend()
plt.savefig("resultado.png")