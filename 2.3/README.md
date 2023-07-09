# Programming2
The purpose of this assignment is to introduce Dask, a flexible library for parallel computing in Python. The exercises aim to provide hands-on experience with Dask and Dask-ML. Here's a summary of each exercise:

Exercise 1: From Pandas to Dask DataFrame
- Download and run the prep.py script to obtain the New York City Airline data, consisting of multiple CSV files.
- Set up a local Dask cluster using the Client class from dask.distributed.
- Read the downloaded CSV files into a Dask DataFrame using the read_csv function.
- Explore the Dask DataFrame using head(), visualise(), and compute().
- Answer several questions about the data using Dask operations and compute().

Exercise 2: Dask-ML
Step 1: Use Dask as a Backend
- Create a new Dask client and open it in a new window.
- Use GridSearchCV from scikit-learn to find the best parameters for a Support Vector Classifier (SVC) on random data.
- Utilize joblib's parallel_backend to enable single-machine parallelism with Dask.
- Investigate the results of the GridSearchCV using the cv_results_ property.

Step 2: Classify with Dask-ML
- Download the moons-data.csv file and load it into a Pandas DataFrame.
- Split the data into training and test sets using train_test_split from sklearn.model_selection.
- Create two logistic regressors, one from scikit-learn and one from Dask-ML.
- Train both regressors on the training data and evaluate their performance on the test data.
- Experiment with different hyperparameter values and compare the results.
- Plot a scatter plot of the test data, including the predicted or actual classes.

