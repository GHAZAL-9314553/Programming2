# Programming2
The purpose of this assignment is to build a relatively complex system that involves multiple classes working together to process and analyze temperature anomaly data. The assignment is divided into three steps:

Step 1: Producing data
- Implement a class called CsvConverter to convert temperature anomaly data from CSV format to JSON format.
- Create a class called Reader to read the temperature data from a CSV file in strides and return it as JSON.
- The Reader class will utilize the CsvConverter class to convert the data.

Step 2: Consuming the data
- Create two consuming classes, AverageYear and AverageMonth, to analyze the temperature anomaly data provided by the Reader class.
- Use the data returned by the Reader class to calculate and visualize the average temperature anomalies over a set of years and months.
- Make use of libraries such as pandas, numpy, and matplotlib for data processing and visualization.

Step 3: The observer pattern
- Refactor the classes from Step 2 to implement the observer pattern.
- Extend the Reader class with methods to add and remove observers.
- Modify the consuming classes to become observers and react to updates from the Reader class.
- Implement a mechanism for the Reader class to periodically notify observers of new data.
- Visualizations should be updated when new data is received.

The goal of this step is to decouple the classes and create a more robust and versatile system using the observer pattern. The architecture involves the Reader class as the subject, with the consuming classes acting as observers.

Throughout the assignment, the codebase is continuously improved, taking into consideration separation of concerns, modularity, and code organization. The README.md file should document the progress made, including improvements, challenges, and potential solutions for the architecture.

