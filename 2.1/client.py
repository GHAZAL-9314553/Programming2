import aiohttp
import asyncio
import json

class NetworkClient:
    """
    Client for making network requests.
    """

    def __init__(self, base_url):
        """
        Initialize the NetworkClient.

        Args:
            base_url (str): The base URL for the requests.
        """
        self.base_url = base_url

    async def fetch_data(self, endpoint, callback):
        """
        Fetch data from the specified endpoint and process it using the provided callback.

        Args:
            endpoint (str): The endpoint to fetch data from.
            callback (coroutine function): The callback function to process the fetched data.

        Returns:
            The result of the callback function.
        """
        async with aiohttp.ClientSession() as session:
            url = self.base_url + endpoint
            async with session.get(url) as response:
                data = await response.text()
                try:
                    json_data = json.loads(data)
                    return await callback(json_data)
                except json.JSONDecodeError:
                    print("Error decoding JSON data.")
                    return None

# Example callback functions
async def process_data_all(data):
    """
    Process all data.

    Args:
        data (dict): The data to process.

    Returns:
        The processed data.
    """
    if not data:
        print("Data not available for the given period.")
        return None
    result = data  # Return the entire data object
    return result

async def process_data_1881_to_1885(data):
    """
    Process data for the period 1881 to 1885.

    Args:
        data (list): The data to process.

    Returns:
        The processed data.
    """
    if not data or not isinstance(data, list):
        print("Data not available for the given period (1881 to 1885).")
        return None
    return data  # Return the data as it is

async def main():
    """
    Main entry point of the program.
    """
    base_url = 'http://localhost:8080/data/'
    client = NetworkClient(base_url)

    tasks = [
        client.fetch_data('all', process_data_all),
        client.fetch_data('1881', process_data_1881_to_1885),
        client.fetch_data('1881/1883', process_data_1881_to_1885),
    ]

    results = await asyncio.gather(*tasks)

    for result in results:
        if result is not None:
            print(f'{result}\n\n')
           

if __name__ == '__main__':
    asyncio.run(main())
