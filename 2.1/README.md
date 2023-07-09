# Programming2
The purpose of this assignment is to implement a client-server architecture and explore asynchronous programming concepts. The exercises focus on creating a server that serves weather data and a client that consumes the data from the server. Here's a summary of each exercise:

Exercise 1: Create a server
- Use Python's http server module to create a server that serves weather data.
- The server should have an endpoint "/data" with different options for retrieving data: "/all", "/{year}", or "/{from-year}/{to-year}".
- Implement a custom class that extends SimpleHTTPRequestHandler to handle the requests.
- Create a method called go_GET that gets called for GET requests to the "/data" endpoint.
- In the go_GET method, check the request path and respond with appropriate status codes (404 or 400) for invalid requests.
- Create a separate DataProvider class responsible for providing the weather data based on the request parameters.
- The DataProvider class should have a method that returns the requested data as a JSON string.
- Transpose the DataFrame before converting it to JSON to make the structure more logical.
- Use the DataProvider in the request handler to call its method based on the request format.
- Ensure the server responds with a status code of 200 and a Content-Type header of "application/json".

Exercise 2: Create an async client
- Create a client class, NetworkClient, that takes the base URL of the server on initialization.
- Implement a method in NetworkClient that receives an endpoint to fetch data from the server and a function to be called when the data is received.
- Make the function non-blocking by making it an async def and using awaits where necessary.
- The function should process the received data and return a result.
- Create multiple calls to the method in NetworkClient and use asyncio.gather to run them concurrently.
- Use the return values of the function calls for visualization or display purposes.
- Use asyncio.run() to run the main asyncio function.

