import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.stats as st

#making dataset
np.random.seed(123)
n_sample = 150
xs = np.random.randint(1000,100000,n_sample)

#visualize dataset
plt.hist(xs,alpha=.5)
plt.xlabel('¥_bill')
plt.ylabel('count')
plt.title('Money in Wallet')
plt.show()


#bootstrap sampling
#sampling
N = len(xs)
Bs = 300
vars = []
means = []

#loop for bootstrap sampling by b=1,2...,B
np.random.seed(123)
mean_B = []
var_B = []

#check bootstrap mean and variance by B
for B in np.arange(1,Bs+1):
    means = []
    vars = []
    for b in range(1,B+1):
        #making subsets
        boot_sample = np.random.choice(xs, size=N, replace=True)
        #mean and variance of the subset at b in B subsets
        means.append(np.mean(boot_sample))
        vars.append((np.var(boot_sample,ddof=1)))
    #record bootstrap means and variances by B
    mean_B.append(np.mean(means))
    var_B.append(np.mean((vars)))

#visualize
fig, axs = plt.subplots(1,2,figsize=(8,4))
axs[0].plot(np.arange(1,B+1),mean_B,'.',alpha=.5)
axs[0].set_xlabel('B')
axs[0].set_ylabel('mean')
axs[0].set_title('Bootstrap Mean')
axs[1].plot(np.arange(1,B+1),var_B,'.',alpha=.5)
axs[1].set_xlabel('B')
axs[1].set_ylabel('var')
axs[1].set_title('Bootstrap Variance')
plt.show()


#Visualzation the estimated population mean by B
#update function
def update(B):
    means = []
    for b in range(B+1):
        #making subset from 1 to B
        boot_sample = np.random.choice(xs, size=N, replace=True)
        #record subset mean at b in B bootstrap
        means.append(np.mean(boot_sample))
    #record bootstrap mean at B
    means_B.append(np.mean(means))

    plt.cla()
    #confidencial interval
    CI95 = st.t.interval(alpha=0.95, df=len(means_B) - 1, loc=np.mean(means_B), scale=st.sem(means_B))
    #estimated population mean
    mean = np.mean(means_B)
    bins = np.arange(40000, 60000, 200)

    plt.hist(means_B,bins=bins,range=(45000,55000),alpha=.5)
    plt.title(f'Distribution of Bootstrap Sample Mean, B={B}')
    plt.ylim(0,100)
    plt.text(mean, 15, 'Mean:{:.0f}'.format(mean))
    plt.text(mean, 10, 'CI95: {:.0f} - {:.0f}'.format(CI95[0], CI95[1]))
    plt.xlabel('estimated population mean from bootstrap')
    plt.ylabel('count')
    plt.vlines(mean, 0, 100, linestyles='dashed', colors='gray')

means_B = []
fig = plt.figure()
ani = animation.FuncAnimation(fig,update,interval=300, save_count=300)
ani.save('boot_dist.gif', writer='imagemagick', fps=10)
plt.show()