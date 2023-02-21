from lazypredict.Supervised import LazyClassifier, LazyRegressor
from sklearn.model_selection import train_test_split
from sklearn import datasets


if __name__ == "__main__":
    # load data
    data = datasets.load_breast_cancer()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=42)
    # fit all models
    clf = LazyClassifier(predictions=True)
    models, predictions = clf.fit(X_train, X_test, y_train, y_test)
    print("Classification models")
    print(models)

    boston = datasets.load_boston()
    X, y = boston.data, boston.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=42)
    # fit all models
    reg = LazyRegressor(predictions=True)
    models, predictions = reg.fit(X_train, X_test, y_train, y_test)
    print("Regressor Models")
    print(models)