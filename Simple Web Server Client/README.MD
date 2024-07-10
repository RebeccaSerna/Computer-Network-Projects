The project involves creating a simple web server and a corresponding web client. The web server listens for incoming HTTP requests and serves the requested files, while the web client sends HTTP GET requests to the server and handles the responses. This setup can be used to demonstrate essential client-server communication over HTTP.

Helloworld.html: This simple HTML file contains the text "This is a test." It's used for testing purposes as a simple web page to be served by a web server.

Webclient.py: This is a Python script that acts as a web client. It connects to a specified server and requests a file using the HTTP GET method. The script sends the request to the server and then receives and prints the response. Key features: Establishes a TCP connection to a server. Sends an HTTP GET request for a specified file. Receives the response and handles buffering of the data received.

Webclienttest.py: This script tests the functionality of the Webclient.py script. It automates making requests and validating responses to ensure the web client behaves as expected under different conditions. The content of this file was truncated, but it generally includes test cases for the client’s functionality.

Webserver.py: This Python script sets up a basic web server. It listens for incoming HTTP requests on a specified port, serves requested files if they exist, and returns appropriate HTTP responses. Key features: Creates and binds a server socket. Listens for and accepts incoming connections. Reads and parses HTTP GET requests. Serves the requested file or returns a 404 error if the file is not found.
