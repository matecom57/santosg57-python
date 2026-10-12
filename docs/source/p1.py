import numpy as np
import matplotlib.pyplot as plt

mu = 0
var = .2

x = np.arange(-5,5,.1)

e = (x-mu)**2/(2*var)

f = np.exp(-e) / np.sqrt(2*np.pi*var)
cf = np.cumsum(f)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(x,f)
ax2.plot(x,cf) 

plt.show()





