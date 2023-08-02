import http.server
import socketserver
import pandas as pd
import json

class ServerHandler(http.server.SimpleHTTPRequestHandler):
    """
    Custom request handler for the HTTP server.
    """

    def do_GET(self):
        """
        Handle GET requests.

        This method is called for each GET request received by the server. It handles requests to retrieve data
        and serves the appropriate response.
        """
        if self.path.startswith("/data"):
            # Remove the "/data" prefix from the path
            path = self.path.replace("/data", "")

            if path == "/all":
                # Retrieve all data

                # Why are you making a new DataProvider for each request?
                # You could also just make one in the initializer for this class,
                # as it is basically immutable. Also, you are making an object
                # independent of the `if`statement, so you could do it outside of the `if`.

                data = DataProvider().get_data()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(data.encode())

            elif path.startswith("/"):
                parts = path.split("/")
                if len(parts) == 2:
                    try:
                        year = int(parts[1])
                        # Retrieve data for a specific year
                        data = DataProvider().get_data(year)
                        self.send_response(200)
                        self.send_header("Content-Type", "application/json")
                        self.end_headers()
                        self.wfile.write(data.encode())
                    except ValueError:
                        self.send_error(400, "Illegal request")

                elif len(parts) == 3:
                    try:
                        from_year = int(parts[1])
                        to_year = int(parts[2])
                        # Retrieve data for a range of years
                        data = DataProvider().get_data((from_year, to_year))
                        self.send_response(200)
                        self.send_header("Content-Type", "application/json")
                        self.end_headers()
                        self.wfile.write(data.encode())
                    except ValueError:
                        self.send_error(400, "Illegal request")

                else:
                    self.send_error(400, "Illegal request")

        else:
            # Call the parent class's do_GET method for standard handling of other paths
            # Ok, but you could also issue a 404-error.
            super().do_GET()

class DataProvider:
    """
    Class responsible for providing data.
    """

    def get_data(self, year=None):
        """
        Get data based on the specified year or range of years.

        Args:
            year (int or tuple): Year or range of years to retrieve data for. If None, retrieve all data.

        Returns:
            str: JSON-encoded data.
        """
        df = pd.read_csv("C:/code/data.csv")  # Assuming data.csv is in the same directory as the script

        # You are kind of doing the same checks here as you did in the controller...
        if year is None:
            # Retrieve all data
            data = df.to_json(orient="records")
        elif isinstance(year, int):
            try:
                # Retrieve data for a specific year
                data = df[df["Year"] == year].to_json(orient="records")
            except ValueError:
                raise ValueError("Invalid parameter")
        elif isinstance(year, tuple) and len(year) == 2:
            from_year, to_year = year
            # Retrieve data for a range of years
            data = df[(df["Year"] >= from_year) & (df["Year"] <= to_year)].to_json(orient="records")
        else:
            raise ValueError("Invalid parameter")

        return data

PORT = 8080
Handler = ServerHandler

# Start the HTTP server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
