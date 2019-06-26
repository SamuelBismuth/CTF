import requests


def download_file_from_server_endpoint(server_endpoint, local_file_path):
    # Send HTTP GET request to server and attempt to receive a response
    response = requests.get(server_endpoint)
    # If the HTTP GET request can be served
    if response.status_code == 200:

        # Write the file contents in the response to a file specified by local_file_path
        with open(local_file_path, 'wb') as local_file:
            for chunk in response.iter_content(chunk_size=128):
                local_file.write(chunk)

download_file_from_server_endpoint("http://csa.bet/", "secret.py")