import numpy as np

class LinReg:
    def __init__(self, n_iterations=1000, learning_rate=0.001):
        self.n_iters = n_iterations
        self.lr = learning_rate
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_rows, n_cols = X.shape
        self.bias = 0
        self.weights = np.zeros(n_cols)

        for _ in range(self.n_iters):
            y_pred = np.dot(X, self.weights) + self.bias
            cost = (y_pred - y)

            dw = 1/n_rows * np.dot(X.T, cost)
            db = 1/n_rows * np.sum(cost)

            #Need to check gradient
            self.bias -= self.lr * db
            self.weights -= self.lr * dw

        print(f"Completed training for Linear Regrssion model Weights: {self.weights}, Bias: {self.bias}")

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias


class Metrics:
    def __init__(self):
        pass
    
    #Review the r_squared
    def r_squared(y, y_pred):
        y_mean = np.mean(y)

        return 1 - (np.mean(y - y_pred / (y_mean - y_pred)) ** 2)