import numpy as np
from collections import defaultdict
class LogReg:
    def __init__(self, n_iters=1000, alpha=0.001):
        self.n_iters = n_iters
        self.lr = alpha
        self.weights = None
        self.bias = None
        self.loss_dict = defaultdict(dict())
    
    def fit(self, X, y):
        n_samples, n_features = X.shape

        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            lin_model = np.dot(X, self.weights) + self.bias
            
            y_pred = self._sigmoid(lin_model)
            loss = self.bce_loss(y_pred, y)
            self.loss_dict[(self.n_iters, self.bias)] = loss
            #perform grad descent
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)

            self.weights -= dw * self.lr
            self.bias -= db * self.lr

    def predict(self, X):
        return self._sigmoid(np.dot(X, self.weights) + self.bias)

    def bce_loss(y_pred, y):
        return (-y * np.log(y_pred) - (1 - y)* np.log(1 - y_pred)).mean()

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))


class LogisiticRegression:
    def __init__(self, n_iters=1000, lr=0.001):
        self.n_iters = n_iters
        self.lr = lr
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape

        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            z = np.dot(X, self.weights) + self.bias
            y_pred = self._sigmoid(z)
            """Implement the loss funciton (binary cross entropy"""

            #Calc the gradients
            dw = 1/n_samples * np.dot(X.T, (y_pred - y))
            db = 1/n_samples * np.sum(y_pred - y)

            #Update the weights and bias
            self.weights -= dw * self.lr
            self.bias -= db * self.lr

        print("Completed training cycle")

        pass
    def _sigmoid(self, z):
        return 1 / 1 + np.exp(-z)

    def predict(self, X):
        z = np.dot(X, self.weights) + self.bias
        y_pred = self._sigmoid(z)
        return y_pred

    def bce_loss_fn(self, y_pred, y):
        return (- y * np.log(y_pred) - (1 - y) * np.log(1 - y_pred)).mean()



    class LogReg:
        def __init__(self, n_iters=1000, lr=0.001):
            self.n_iters = n_iters
            self.lr = lr
            self.weights = None
            self.bias = None

        def fit(self, X, y):
            n_samples, n_features = X.shape
            self.weights = np.zeros(n_features)
            self.bias = 0

            for _ in range(self.n_iters):
                z = np.dot(X, self.weights) + self.bias
                y_pred = self._sigmoid(z)
                """
                Loss function Binary Cross Entropy
                """
                #gradient descent
                dw = 1/n_samples * np.dot(X.T, (y_pred - y))
                db = 1/n_samples * np.sum(y_pred - y)

                self.weights -= dw * self.lr
                self.bias -= db * self.lr

            print("completion of training for logistic regression model")
            pass

        def predict(self, X):
            z = np.dot(X, self.weights) + self.bias
            y_pred = self._sigmoid(z)
            return y_pred

        
        def _sigmoid(self, z):
            return 1/1 + np.exp(-z)
            pass

        def bce_loss(self, y, y_pred):
            return (-y * np.log(y_pred) - (1 - y) * np.log(1 - y_pred))