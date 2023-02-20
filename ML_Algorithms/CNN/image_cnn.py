import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    (X_train, y_train), (X_test, y_test) = datasets.cifar10.load_data()
    y_train = y_train.reshape(-1, )
    y_test = y_test.reshape(-1, )

    classes = ["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]

    #normalization
    X_train = X_train / float(255)
    X_test = X_test / float(255)

    #cnn model
    cnn = models.Sequential([
        layers.Conv2D(filters=32, kernel_size=(3,3), activation='relu', input_shape=(32,32,3)),
        layers.MaxPooling2D((2,2)),

        layers.Conv2D(filters=64, kernel_size=(3,3), activation='relu'),
        layers.MaxPooling2D((2,2)),

        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])

    cnn.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # cnn.summary()
    cnn.fit(X_train, y_train, epochs=10)

    cnn.evaluate(X_test, y_test)