# Programming2

The purpose of this assignment is to apply the lessons learned in software engineering to develop a small pipeline with interacting components. The assignment integrates concepts from machine learning and programming. The specific tasks include:

Getting and transforming the data: we can either use the anomaly detection study case dataset provided in the unsupervised part of DS3 or choose our own dataset that meets certain requirements. The data should have a logical reason for growing over time, and we should be able to split it into training and testing sets. Additionally, the data should require non-trivial transformations. The dataset provided contains sensor data from April to August 2018, and you need to split it accordingly.

Creating the model and the drawer: Train a machine learning model using the training data from the previous step. Perform necessary data transformations on the training data only. Evaluate the model's performance and use scikit-learn or similar techniques to persist the model on your local file system. Refactor the plotting method to be independent of global variables and return the plot instead of displaying it.

Implementing a class to listen for new data: Create a class that monitors a specific directory for new data files. When a new file is uploaded, the class should load the data, apply the necessary transformations, use the trained model to make predictions, and save the transformed data and predictions in different directories. It should also generate images for specific sensors and save them in an img directory. The entire process should be logged in a log-file.

The assignment emphasizes the following technical requirements:

Independence of files and classes following the SOLID principles.
Configuration settings specified in an application.json file, including the locations of input, output, and img directories, sensor names for drawing, and the interval for checking the input directory.
By completing this assignment, we will gain practical experience in developing a software pipeline, integrating machine learning models, and implementing logging and file handling functionalities.
