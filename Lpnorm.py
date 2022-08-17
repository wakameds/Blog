import numpy as np
import matplotlib.pyplot as plt

# data object
np.random.seed(123)
X = np.random.randint(50,100,size=500)
Y = np.random.randint(50,100,size=500)

# dimension
P = np.arange(1,501)

# list
L1s = []
L2s = []
Linfs = []

for p in P:
    # set features
    X_dim = X[:p]
    Y_dim = Y[:p]

    # compute distance
    L1 = sum(abs(X_dim-Y_dim))
    L2 = np.sqrt(sum(np.power((X_dim-Y_dim),2)))
    Linf = np.max(abs(X_dim-Y_dim))

    # save result
    L1s.append(L1)
    L2s.append(L2)
    Linfs.append(Linf)

# visualization
plt.plot(P,L1s,'-',label='Manhattan')
plt.plot(P,L2s,'-',label='Euclidean')
plt.plot(P,Linfs,'-',label='Chebyshev')
plt.ylabel(r'$Dist (X,Y)$')
plt.xlabel(r'$p:Dimension$')
plt.legend()
plt.show()


#%%
import numpy as np

def cos_sim(X,Y):
    return np.dot(X,Y)/(np.linalg.norm(X)*np.linalg.norm(Y))

X = np.array([2,5])
Y = np.array([4,3])

cos_sim(X,Y)

#%%
def jaccard_sim(A,B):
    return len(np.intersect1d(A,B))/len(np.union1d(A,B))

A = ['cat','dog','lion','bird']
B = ['lion','bird','rabbit','rat','tiger']

jaccard_sim(A,B)

#%%
def dice_sim(A,B):
    return 2*len(np.intersect1d(A,B))/(len(A)+len(B))

A = ['cat','dog','lion','bird']
B = ['lion','bird','rabbit','rat','tiger']

dice_sim(A,B)