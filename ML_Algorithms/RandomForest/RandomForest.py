import numpy as np
from collections import Counter
from DecisionTree.DecisionTree import DecisionTree

def bootstrap_sample(X, y):
    n_samples = np.shape[0]
    idxs = np.random.choice(n_samples, size=n_samples, replace=True)
    return X[idxs], y[idxs]

def most_common_label(y):
    counter = Counter(y)
    most_common = counter.most_common(1)[0][0]
    return most_common

class RandomForest:
    def __init__(self, n_feats, max_tree_depth=2, min_node_split=2, num_trees=100):
        self.n_feats = n_feats
        self.max_tree_depth = max_tree_depth
        self.min_samples = min_node_split
        self.num_trees = num_trees
        self.trees = list()
    
    def fit(self, X, y):
        self.trees = list()
        for _ in range(self.num_trees):
            tree = DecisionTree(self.min_samples,self.max_tree_depth, self.n_feats)
            X_data, y_data = bootstrap_sample(X, y)
            tree.fit(X_data, y_data)
            self.trees.append(tree)
    
    def predict(self, X):
        tree_preds = np.array([tree.predict(X) for tree in self.trees])
        tree_preds = tree_preds.T
        # tree_preds = np.swapaxes(tree_preds, 0, 1)
        y_pred = [most_common_label(pred) for pred in tree_preds]
        return np.array(y_pred)