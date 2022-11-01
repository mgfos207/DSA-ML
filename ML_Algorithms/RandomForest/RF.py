import numpy as np
from collections import Counter

from DecisionTree.DecisionTree import DecisionTree

""""
ovefit param - max-depth (decrease for overfitting)
underfit param - max-depth (increase for underfitting)
"""
class RandomForest:
    def __init__(self, n_trees=100, max_depth=100, min_samples=2, num_feats=10):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_samples = min_samples
        self.trees = list()
        self.n_feats = num_feats

    def _bootstrap(self, X, y):
        idxes = np.random.choice(X.shape[0], X.shape[0], replace=True)
        return X[idxes], y[idxes]

    def fit(self, X, y):
        self.trees = list()

        for _ in range(self.n_trees):
            tree = DecisionTree(self.min_samples, self.max_depth, self.n_feats)
            X_data, y_data = self._bootstrap(X, y)
            tree.fit(X_data, y_data)
            self.trees.append(tree)
        
        print("Completed the training of random forest")

    def _most_common_label(y):
        counter = Counter(y)
        most_common = counter.most_common(1)[0][0]
        
        return most_common

    def predict(self, X):
        y_pred = [tree.predict(X) for tree in self.trees]
        """
        [[1, 1, 1, 1], [1, 0, 1, 1], [0,0,0,0], [1,1,1,1]]
        """
        y_pred = y_pred.T
        most_common = self._most_commmon_label(y_pred)
        return most_common