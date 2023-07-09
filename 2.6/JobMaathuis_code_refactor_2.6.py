"""Code Description:
The given code is an HTTP server that handles GET requests and responds with JSON data. It uses the DataProvider
class to retrieve data based on the requested path.

Code Organization and Maintainability:
Overall, the code is well-organized and follows a modular approach by separating the server logic into the 
RequestHandler class.
The do_GET method handles the GET requests and follows a conditional branching structure based on the requested
path components.
The DataProvider class seems to be separate and should be reviewed separately."""
"""Short Units of Code: The do_GET method is divided into small units of code within different if conditions,
which improves readability and maintainability.

Simple Units of Code: The code within each if condition is simple and easy to understand.

Write Code Once: The code reuses the DataProvider class to fetch data based on different requests.

Keep Unit Interfaces Small: The do_GET method handles the GET request and delegates the data retrieval to
the DataProvider class, keeping the unit interfaces focused.

*************
Suggestions for Refactor:

One potential refactor that can improve the code base is to encapsulate the data retrieval logic within
the DataProvider class. This can be done by creating separate methods for retrieving all data, data by year, 
and data within a range of years. This will improve code modularity and reduce duplication in the do_GET
method.

Refactor Proposal:

Modify the DataProvider class to include separate methods for data retrieval based on different criteria.
Create methods like get_all_data(), get_data_by_year(year), and get_data_within_range(start_year, end_year) in 
the DataProvider class.
In the do_GET method, replace the current code blocks with calls to the appropriate methods of the DataProvider
class.
This refactor will centralize the data retrieval logic, making it easier to maintain and scale.
Benefits of Refactor:

Improved Code Organization: The code will be more organized with a clear separation of responsibilities between
the RequestHandler and DataProvider classes.
Elimination of Code Duplication: By encapsulating the data retrieval logic, duplicate code blocks can be removed, reducing the risk of errors and making the code more maintainable.
Better Scalability: The refactor allows for easier addition of new data retrieval methods or modifications in
the future, enabling scalability as the project grows.
code does not include the implementation of the DataProvider class.
A more comprehensive review can be provided once the code for the DataProvider class is
available for analysis."""


import http.server
import socketserver
from dataprovider_class import DataProvider

class RequestHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        data_provider = DataProvider()
        if self.path.startswith('/data/'):
            path_components = self.path.split('/')
            
            if len(path_components) == 3:
                # get all the data
                if path_components[2] == 'all':
                    data = data_provider.get_data()
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(data.encode('UTF-8'))
                
                
                # check if it is a year
                try:
                    int(path_components[2])
                except:
                    self.send_response(404,message='illegal request')
                    self.end_headers()
                    return # stop

                
                # get data of a certain year
                else:
                    data = data_provider.get_data(path_components[2])
                    # if we obtained datta
                    if data != '{}':
                        self.send_response(200)
                        self.send_header('Content-type', 'application/json')
                        self.end_headers()
                        self.wfile.write(data.encode('UTF-8'))
                    # if there is no data
                    else:
                        self.send_response(404,message='Not Found')
                        self.end_headers()
                
            # range of years
            if len(path_components) == 4:
                # check if it is a year
                try:
                    int(path_components[2])
                    int(path_components[3])
                except:
                    self.send_response(404,message='illegal request')
                    self.end_headers()
                    return  # stop 
                
                data = data_provider.get_data([path_components[2], path_components[3]])
                data = data[0] + data[1]
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(data.encode('UTF-8'))
           
        else:
            # Call the parent class's implementation of do_GET for paths that aren't '/data'
            super().do_GET()

if __name__ == '__main__':
    PORT = 8000 
    http = socketserver.TCPServer(("", PORT), RequestHandler)
    print("serving at port", PORT)
    http.serve_forever()
    

