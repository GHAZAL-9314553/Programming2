import matplotlib.pyplot as plt
import linecache
import time

class CsvConverter:
    def __init__(self, file_path):
        """
        Converts a CSV file to a JSON list of dictionaries.

        Args:
            file_path (str): The path to the CSV file.
        """
        self.file_path = file_path
        self.header_line = linecache.getline(self.file_path, 1).strip('\n').split(',')

    def csv_to_json(self, list_lines):
        """
        Converts a list of CSV lines to a JSON list of dictionaries.

        Args:
            list_lines (list[str]): The list of CSV lines.

        Returns:
            list[dict]: The JSON list of dictionaries.
        """
        return [
            dict(zip(self.header_line, line.strip('\n').split(',')))
            for line in list_lines
            if len(line.strip('\n').split(',')) == len(self.header_line)
        ]

    def __str__(self):
        """
        Returns a string representation of the CsvConverter object.

        Returns:
            str: The string representation.
        """
        return f'CSV file: {self.file_path}'


class Reader:
    def __init__(self, file_path='dSST.csv', stride=5):
        """
        Reads a CSV file and notifies observers with the data.

        Args:
            file_path (str, optional): The path to the CSV file. Defaults to 'dSST.csv'.
            stride (int, optional): The number of lines to read at a time. Defaults to 5.
        """
        self.file_path = file_path
        self.stride = stride
        # Why does the reader needs this header_line? Isn' that something for the convertor?
        self.header_line = linecache.getline(self.file_path, 1).strip('\n').split(',')
        self.start_line = 2
        self.observers = set()

    def add_observer(self, observer):
        """
        Adds an observer to the Reader object.

        Args:
            observer (object): The observer object.
        """
        self.observers.add(observer)

    def remove_observer(self, observer):
        """
        Removes an observer from the Reader object.

        Args:
            observer (object): The observer object.
        """
        self.observers.remove(observer)

    def notify_observers(self, data):
        """
        Notifies all observers with the provided data.

        Args:
            data (list[dict]): The data to be passed to the observers.
        """
        for observer in self.observers:
            observer.update(data)

    def get_lines(self):
        """
        Retrieves a list of lines from the CSV file.

        Returns:
            list[str]: The list of lines.
        """
        line_list = [
            linecache.getline(self.file_path, self.start_line + i)
            for i in range(self.stride)
        ]
        line_list = [
            line for line in line_list if line.strip() != ''
        ]
        if line_list:
            result = CsvConverter(self.file_path).csv_to_json(line_list)
            self.start_line += self.stride
            # Notify observers with the new data
            self.notify_observers(result)
            # who are you returning this new data to?
            # Normally, a observable keeps its state internal and only
            # uses `notify` to let the observers know that state has changed.
            return result
        else:
            return ''

    def start_reading(self):
        """
        Starts reading the CSV file and notifying observers with the data.
        """

        # Here you're basically hanging the main thread. The responsibility of 
        # propagating the observable should not be within the observable itself
        while True:
            lines = self.get_lines()
            if lines == '':
                break
            time.sleep(5)


class AverageYear:
    def __init__(self):
        """
        Represents an observer that calculates and plots average yearly temperatures.
        """
        self.years = []
        self.temperatures = []
        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(111)

    def update(self, data):
        """
        Updates the observer with new data and plots the average yearly temperature.

        Args:
            data (list[dict]): The data to be processed.
        """
        avg = self.calculate_average_temperature(data)
        if avg:
            self.years.append(len(self.years) + 1)
            self.temperatures.append(avg)
            self.plot_average_temperature()

    def calculate_average_temperature(self, data):
        """
        Calculates the average temperature from the provided data.

        Args:
            data (list[dict]): The data to calculate the average temperature from.

        Returns:
            float: The average temperature.
        """
        count = len(data)
        sum_temp = sum(float(line['J-D']) for line in data)
        if count == 0:
            return None
        avg = sum_temp / count
        return avg

    def plot_average_temperature(self):
        """
        Plots the average yearly temperature.
        """
        self.ax.clear()
        self.ax.plot(self.years, self.temperatures, 'bo-')
        self.ax.set_xlabel('Year')
        self.ax.set_ylabel('Average Temperature')
        self.ax.set_title('Average Yearly Temperature')
        self.ax.grid(True)
        plt.pause(0.01)
        plt.show()


class AverageMonth:
    def __init__(self):
        """
        Represents an observer that calculates and plots average monthly temperatures.

        Initializes the AverageMonth object with the following attributes:
        - months: A list of month names.
        - monthly_averages: A dictionary that stores the average temperatures for each month.
        - years: A list to track the years.
        - yearly_averages: A list to store the average temperatures for each year.
        - monthly_figure, monthly_ax: Matplotlib figure and axes for the monthly plot.
        - yearly_figure, yearly_ax: Matplotlib figure and axes for the yearly plot.
        """

        self.months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.monthly_averages = {month: [] for month in self.months}
        self.years = []
        self.yearly_averages = []
        self.monthly_figure, self.monthly_ax = plt.subplots()
        self.yearly_figure, self.yearly_ax = plt.subplots()

    def update(self, data):
        """
        Updates the observer with new data and plots the average monthly and yearly temperatures.

        Args:
            data (list[dict]): The data to be processed.
        """

        self.calculate_average_temperature(data)
        self.plot_average_monthly_temperature()
        self.plot_average_yearly_temperature()

    def calculate_average_temperature(self, data):
        """
        Calculates the average monthly and yearly temperatures from the provided data.

        Args:
            data (list[dict]): The data to calculate the average temperatures from.
        """

        count = len(data)
        sum_temp = sum(float(line['J-D']) for line in data)
        if count == 0:
            return None
        avg = sum_temp / count
        self.years.append(len(self.years) + 1)
        self.yearly_averages.append(avg)
        for month in self.months:
            self.monthly_averages[month].append(float(data[0][month]))

    def plot_average_monthly_temperature(self):
        """
        Plots the average monthly temperatures.
        """

        self.monthly_ax.clear()
        for month, temps in self.monthly_averages.items():
            self.monthly_ax.plot(range(1, len(temps) + 1), temps, label=month)

        self.monthly_ax.set_xlabel('Data Point')
        self.monthly_ax.set_ylabel('Average Temperature')
        self.monthly_ax.set_title('Average Monthly Temperatures')
        self.monthly_ax.legend()
        self.monthly_ax.grid(True)
        plt.pause(0.01)

    def plot_average_yearly_temperature(self):
        """
        Plots the average yearly temperature.
        """

        self.yearly_ax.clear()
        self.yearly_ax.plot(self.years, self.yearly_averages, 'bo-')
        self.yearly_ax.set_xlabel('Year')
        self.yearly_ax.set_ylabel('Average Temperature')
        self.yearly_ax.set_title('Average Yearly Temperature')
        self.yearly_ax.grid(True)
        plt.pause(0.01)

# Usage example
prod = Reader('dSST.csv')
cons2 = AverageMonth()
prod.add_observer(cons2)
prod.start_reading()
