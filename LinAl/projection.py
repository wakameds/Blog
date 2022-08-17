import numpy as np
import matplotlib.pyplot as plt

np.random.seed((123))
size = 50

#data
ones = np.ones(size)
xs = np.random.randn(size)
noise = np.random.randn(size)
ys = xs*3 + noise
X = np.array((ones,xs)).T

#projection
XT = np.transpose(X)
beta_hat = np.linalg.inv(XT@X)@XT@ys
X_pseudo = np.linalg.inv(XT@X)@XT
P = X@X_pseudo
y_hat = P@ys

#plot
res = np.sum(np.square(ys-y_hat))
plt.plot(xs,ys,'.',markersize=12, label = r'$y$')
plt.plot(xs,y_hat,'.',markersize=12, c='orange', label=r'$\hat{y}$')
plt.plot(xs,y_hat,'-',c='orange',alpha=.4)
plt.vlines(xs,ys,y_hat,linestyles='dashed',colors='gray')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.text(-2.5,2,r"$f(x)=\beta_0+\beta_1x$",color='orange',size=16)
plt.text(1,-6,r"$\sum_{i=1}^{50}e_i^2$ = ",color='red',size=12)
plt.text(1.8,-6,"{:.2f}".format(res),color='red', size=12)
plt.text(-2.5,-8,r"$e_{2}^{2}=(y_2-\hat{y}_{2})^2$",color='gray')
plt.text(0,-2,r"$e_{30}^{2}=(y_{30}-\hat{y}_{30})^2$",color='gray')
plt.legend()
plt.show()
