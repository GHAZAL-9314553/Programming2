import pandas as pd
import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from dask.distributed import Client
from dask_ml.linear_model import LogisticRegression as DaskLogisticRegression
import matplotlib.pyplot as plt
import multiprocessing

def main():
    """
    This function demonstrates the comparison between scikit-learn logistic regression and dask-ml logistic regression
    on a moons dataset. It generates the dataset, splits it into train and test sets, trains both models, makes predictions,
    and plots the test data with the actual classes, Dask-ML predicted classes, and scikit-learn predicted classes.
    """
    # Create a Dask client
    client = Client()

    # Generate the moons dataset
    X, y = make_moons(n_samples=1000, noise=0.3, random_state=0)

    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Train scikit-learn logistic regression
    sklearn_model = LogisticRegression()
    sklearn_model.fit(X_train, y_train)

    # Train dask-ml logistic regression
    dask_model = DaskLogisticRegression()
    dask_model.fit(X_train, y_train)

    # Predict classes using both models
    sklearn_pred = sklearn_model.predict(X_test)
    dask_pred = dask_model.predict(X_test)

    # Plot the test data with actual classes
    plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
    plt.title("Actual Classes")
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.show()

    # Plot the test data with Dask-ML predicted classes
    plt.scatter(X_test[:, 0], X_test[:, 1], c=dask_pred)
    plt.title("Dask-ML Predicted Classes")
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.show()

    # Plot the test data with scikit-learn predicted classes
    plt.scatter(X_test[:, 0], X_test[:, 1], c=sklearn_pred)
    plt.title("Scikit-Learn Predicted Classes")
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.show()

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
