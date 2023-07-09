import linecache
import time
import matplotlib
matplotlib.rcParams['backend'] = 'TkAgg'
import matplotlib.pyplot as plt

class CsvConverter:
    def __init__(self, file_path):
        """
        Converts a CSV file to a list of JSON objects.
        """
        self.file_path = file_path
        self.header_line = linecache.getline(self.file_path, 1).strip('\n').split(',')

    def csv_to_json(self, list_lines):
        """
        Converts a list of CSV lines to a list of JSON objects.
        """
        return [
            dict(zip(self.header_line, line.strip('\n').split(',')))
            for line in list_lines
            if len(line.strip('\n').split(',')) == len(self.header_line)
        ]

    def __str__(self):
        """
        Returns a string representation of the CsvConverter object.
        """
        return f'CSV file: {self.file_path}'

class Reader:
    def __init__(self, file_path='dSST.csv', stride=5):
        """
        Reads a CSV file and notifies observers with data updates.
        """
        self.file_path = file_path
        self.stride = stride
        self.header_line = linecache.getline(self.file_path, 1).strip('\n').split(',')
        self.start_line = 2
        self.observers = set()

    def add_observer(self, observer):
        """
        Adds an observer to the set of observers.
        """
        self.observers.add(observer)

    def remove_observer(self, observer):
        """
        Removes an observer from the set of observers.
        """
        self.observers.remove(observer)

    def notify_observers(self, data):
        """
        Notifies all observers with the updated data.
        """
        for observer in self.observers:
            observer.update(data)

    def get_lines(self):
        """
        Reads a batch of lines from the CSV file and converts them to JSON.
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
            return result
        else:
            return ''

    def start_reading(self, max_lines=None):
        """
        Starts reading the CSV file and notifies observers with data updates.
        """
        lines_read = 0
        while True:
            lines = self.get_lines()
            if lines == '' or (max_lines is not None and lines_read >= max_lines):
                break
            time.sleep(5)
            lines_read += 1

class AverageMonth:
    def __init__(self):
        """
        Represents an observer that calculates and plots average monthly temperatures.
        """
        self.months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.monthly_averages = {month: [] for month in self.months}
        self.years = []
        self.yearly_averages = []
        self.monthly_figure, self.monthly_ax = plt.subplots()
        self.yearly_figure, self.yearly_ax = plt.subplots()

    def update(self, data):
        """
        Updates the average monthly and yearly temperatures based on the received data.
        """
        self.calculate_average_temperature(data)
        self.plot_average_monthly_temperature()
        self.plot_average_yearly_temperature()

    def calculate_average_temperature(self, data):
        """
        Calculates the average temperature for each month and the yearly average temperature.
        """
        count = len(data)
        sum_temp = sum(float(line['J-D']) for line in data)
        assert count > 0, "No data available for calculating average temperature"
        avg = sum_temp / count
        self.years.append(len(self.years) + 1)
        self.yearly_averages.append(avg)
        for month in self.months:
            self.monthly_averages[month].append(float(data[0][month]))

    def plot_average_monthly_temperature(self):
        """
        Plots the average monthly temperature.
        """
        self.monthly_ax.clear()
        for month, temps in self.monthly_averages.items():
            self.monthly_ax.plot(range(1, len(temps) + 1), temps, label=month)

        self.monthly_ax.set_xlabel('Data Point')
        self.monthly_ax.set_ylabel('Average Temperature')
        self.monthly_ax.set_title('Average Monthly Temperatures')
        self.monthly_ax.legend()
        self.monthly_ax.grid(True)
        plt.savefig('average_monthly_temperature.png')
        plt.pause(0.01)

    def plot_average_yearly_temperature(self):
        """
        Plots the average yearly temperature.
        """
        self.yearly_ax.clear()
        self.yearly_ax.plot(self.years, self.yearly_averages, label='Yearly Average')

        self.yearly_ax.set_xlabel('Year')
        self.yearly_ax.set_ylabel('Average Temperature')
        self.yearly_ax.set_title('Average Yearly Temperatures')
        self.yearly_ax.legend()
        self.yearly_ax.grid(True)
        plt.savefig('average_yearly_temperature.png')
        plt.pause(0.01)

plt.ion()

# Usage example
prod = Reader('dSST.csv', stride=5)  # Set the stride to 5
cons2 = AverageMonth()
prod.add_observer(cons2)
prod.start_reading(max_lines=20)

# Keep the figures displayed
plt.show(block=False)

