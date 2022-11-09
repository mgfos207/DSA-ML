import numpy as np
import matplotlib.pyplot as plt

def euclidean_distance(vec1, vec2):
    return np.sqrt(np.sum((vec1 - vec2) ** 2))

class KMeans:
    def __init__(self, k=3, max_iters=1000):
        self.k = k
        self.max_iters = max_iters
        self.clusters = [[] for _ in k]
        self.centroids = [None for i in k]
    
    def predict(self, X):
        n_samples, n_features = X.shape
        #initialize the randomization of the k clusters
        k_idices = np.random.choice(self.k, n_samples, replace=False)
        
        #initialize the centroids
        self.centroids = [X[i] for i in k_idices]

        #start the convergence of the centroids
        for _ in range(self.max_iters):
            #generate clusters based on centroids
            self.clusters = self._generate_clusters(X)
            #create new centroids
            old_centroids = self.centroids
            self.centroids = self._generate_centroids()
            
            #check if there has been any difference between the two centroids
            if self._converged_points(old_centroids):
                break
        #return cluster labels
        cluster_labels = self._get_labels(n_samples)
        return cluster_labels

    def _get_labels(self, n_samples):
        cluster_labels = np.zeros(n_samples)
        for idx, cluster in enumerate(self.clusters):
            for sample_idx in cluster:
                cluster_labels[sample_idx] = idx

        return cluster_labels

    def _converged_points(self, old_centroids):
        distances = [euclidean_distance(old_centroids[i], self.centroids[i]) for i in range(self.centroids)]
        return sum(distances) == 0

    def _generate_centroids(self):
        centroids = []
        for idx, cluster in enumerate(self.clusters):
            new_centroid = np.mean(cluster)
            centroids[idx] = new_centroid
        return centroids

    def _generate_clusters(self, X):
        clusters = [[] for _ in self.k]
        for idx, x in enumerate(X):
            #get closest centroid to point
            centroid = self._get_closest_centroid(x)
            clusters[centroid].append(idx)

        return clusters


    def _get_closest_centroid(self, x):
        distances = [euclidean_distance(x, centroid) for centroid in self.centroids]
        return np.argmin(distances)
        

