import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

#set data
X, y = make_blobs(n_samples=300, centers=4, random_state=77)

#plot the data points
plt.scatter(X[:, 0], X[:,1], marker='.')
plt.show()

#Euclidean distance
def euclidean_dist(x1,x2):
    """
    function to compute L2 norm
    :param x1: instance A
    :param x2: instance B
    :return: distance
    """
    return np.linalg.norm(x1-x2)


def plot(X1, X2, cluster_assignments, centroid, num_iter):
    """
    function to visualize the cluster and centroid at iteration number
    :param X1: dimension1
    :param X2: dimension2
    :param cluster_assignments: assigned cluster based on centroid
    :param centroid: centroid coordinates
    :param num_iter: iteration number
    :return: plot graph
    """

    # color
    color = ['r', 'g', 'c']
    CPallet = [color[i] for i in cluster_assignments]

    # plot scatter
    plt.scatter(X1, X2, c=CPallet)
    plt.scatter(centroid[:,0], centroid[:, 1], marker='x', s=150, c='k')
    plt.text(0, 0, 'iter: {}'.format(num_iter), fontsize=18)
    return plt.show()


#K-means
class k_means():
    """
    class for k_kean
    """
    def __init__(self, k, data, n_iter, centroid_init = None):
        """
        :param k: k
        :param data: dataset
        :param n_iter: max iteration of k-mean procedure
        :param centroid_init: centroid
        """
        self.k = k
        self.data = data
        self.iter = n_iter
        self.centroid_init = centroid_init

    def initialise_centroid(self, centroid_init, k, data):
        """
        function to decide the initial centroids by k
        :param centroid_init(str): 'random' or 'other'
        :param k(int): the parameter with k
        :param data(array): dataset
        :return: initial centroid sample
        """
        #1. random case
        if self.centroid_init == 'random':
            #shuffle data and decide k points as initial centroid points
            initial_centroids = np.random.permutation(data.shape[0])[:self.k]
            self.centroids = data[initial_centroids]
        #2. not shuffle case. Decide the centroid pints from the top row
        elif self.centroid_init == 'other':
            self.centroids = data[:k]

        return self.centroids

    def fit(self, data, vis=False):
        #make matrix for class
        sample_num = np.shape(data)[0]
        cluster_assignments = np.mat(np.zeros((sample_num,2)))

        #set initial centroids
        cents = self.initialise_centroid(self.centroid_init, self.k, data)

        #preserve original centroids
        cents_orig = cents.copy()
        changed = True
        num_iter = 0

        #iterate update until num_iter reachs set num count
        while changed and num_iter < self.iter:
            changed = False
            #for each row in the dataset
            for i in range(sample_num):
                # Track minimum distance and vector index of associated cluster
                min_dist = np.inf
                min_index = -1
                #calculate distance between centroid and data point
                for j in range(self.k):
                    dist_ji = euclidean_dist(cents[j,:], data[i,:])
                    # update class index if distance is shorter than min_dist
                    if dist_ji < min_dist:
                        min_dist = dist_ji
                        min_index = j
                    #check if cluster assignment of instance has changed
                    if cluster_assignments[i,0] != min_index:
                        changed = True

                #Record class index and distance to appropriate cluster
                cluster_assignments[i, :] = min_index, min_dist**2

            #Update centroid location by computing mean
            for cent in range(self.k):
                points = data[np.nonzero(cluster_assignments[:,0].A==cent)[0]]
                cents[cent, :] = np.mean(points, axis=0)

            #Count iterations
            num_iter += 1


            #plot
            if vis == True:
                plot(X[:,0],X[:,1],np.concatenate(cluster_assignments[:,0].A.astype(int)),cents,num_iter)

        #Return
        return cents, cluster_assignments


#Perform k-means clustering with centroids initialize='random'
kmeans = k_means(k=3, data= X, n_iter=5, centroid_init='random')
centroids, cluster_assignments = kmeans.fit(X)


#%%


COST = []
for i in range(1,9):
    kmeans = k_means(k=i, data=X, n_iter=5, centroid_init='random')
    centroids, cluster_assignments = kmeans.fit(X)
    cost = np.sum(cluster_assignments[:,1])
    COST.append(cost)

l = np.arange(1,9)

plt.plot(l,COST,'.-')
plt.xlabel('k')
plt.ylabel('cost')
plt.title('Elbow Method')
plt.show()