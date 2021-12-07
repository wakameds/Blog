import numpy as np
import matplotlib.pyplot as plt

#plot the lines definition
a = 30
d = -0.2
t = np.linspace(0,30,500)
conc = a*np.exp(d*t)

#make plot
plt.plot(t, conc, color='b')
plt.fill_between(t,conc,0, where=(t <= 5), facecolor='blue', alpha=0.2)
plt.xlim(0,30)
plt.ylim(0,35)
plt.xlabel(r'$t_{min}$')
plt.ylabel(r'$Concentrate_{mol}$')
plt.annotate(r'$\Delta t$', xy=(2.5,5))
plt.annotate('$a\cdot exp(d\cdot t)$', xy=(4,15), xytext=(10,15), fontsize=18,
            arrowprops=dict(arrowstyle='->'))
plt.show()
