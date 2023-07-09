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



Step 1: Producing data
- Created the `CsvConverter` class to convert CSV data to JSON format.
- Implemented the `csv_to_json` method to convert a list of CSV lines to a JSON list of dictionaries.
- Separated concerns by encapsulating the conversion logic in the `CsvConverter` class.

Step 2: Consuming the data
- Created the `Reader` class to read CSV data in strides and notify observers.
- Implemented the `add_observer` and `remove_observer` methods to manage observers.
- Refactored the consuming classes (`AverageYear` and `AverageMonth`) to act as observers and update their visualizations based on new data from the `Reader`.
- Utilized libraries such as `matplotlib` for data processing and visualization.

Step 3: The observer pattern
- Extended the `Reader` class with methods to add and remove observers, allowing for dynamic registration and removal of observers.
- Implemented the `notify_observers` method to notify all registered observers with new data.
- Modified the consuming classes to become observers and react to updates from the `Reader`.
- Utilized the observer pattern to decouple the classes and create a more robust and versatile system.
- Improved code modularity and maintainability by separating the responsibilities of reading data and processing it.

Challenges faced:
- Ensuring proper synchronization and handling of data updates between the `Reader` and observer classes.
- Addressing potential performance issues, such as efficiently handling large datasets and visualizations.

Potential solutions and further improvements:
- Implementing concurrency techniques like multi-threading or asyncio to improve the responsiveness and efficiency of data processing and visualization.
- Optimizing the code for handling large datasets, such as using streaming techniques or chunked data processing.
- Refactoring the code to enhance modularity and reusability, such as separating visualization logic into separate classes or functions.
- Implementing error handling and robustness measures to handle various edge cases and unexpected scenarios.

