import numpy as np

class LinearRegression:

    def __init__(self, learning_rate=0.001, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape

        # init parameters
        self.weights = np.zeros(n_features)
        self.bias = 0

        # gradient descent
        for _ in range(self.n_iters):
            y_predicted = np.dot(X, self.weights) + self.bias
            # compute gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            # update parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
 

    def predict(self, X):
        y_approximated = np.dot(X, self.weights) + self.bias
        return y_approximated


class LinearReg:
    def __init(self, lr, weights, bias, iterations=1000):
        self.lr = lr
        self.weights = weights
        self.bias = bias
        self.iterations = iterations

    def fit(self, X, y):
        n_samples, n_features = X.shape

        #initialize weight and bias
        self.weights = np.zeroes(n_features)
        self.bias = 0

        #iterative process
        for _ in range(0, self.iterations):
        
            y_pred = np.dot(X, self.weights) + self.bias

            dw = (1/n_samples) * np.dot(X.T * (y_pred - y))
            bias = (1/n_samples) * np.sum(y_pred - y)

            self.bias -= bias * self.lr
            self.dw -= dw * self.lr

    def predict(self, X):
        y_infer = np.dot(X, self.weights) + self.bias
        return y_infer