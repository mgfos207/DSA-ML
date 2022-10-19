import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import mpl_toolkits.mplot3d 
from sklearn import datasets
from sklearn.model_selection import train_test_split

from LinearRegression.LinearReg import LinearReg

def main():
    diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(diabetes_X, diabetes_y, test_size=0.25, random_state=43)
    
    # lin_reg_obj = LinearReg()
    # lin_reg_obj.fit(X_train, y_train)

if __name__ == "__main__":
    main()