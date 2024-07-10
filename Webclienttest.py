import socket
import sys

# Function to send an HTTP GET request to the server
def send_get_request(server_address, server_port, filename):
    try:
        # Create a socket to connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set the receive buffer size to control flow
        receive_buffer_size = 4096  # Adjust this as needed
        client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, receive_buffer_size)

        client_socket.connect((server_address, server_port))

        # Send the HTTP GET request to the server
        request = f"GET /{filename} HTTP/1.1\r\nHost: {server_address}:{server_port}\r\n\r\n"
        client_socket.send(request.encode())

        # Receive and display the server's response
        response = b""
        while True:
            new_part = client_socket.recv(receive_buffer_size)
            if not new_part:
                break
            response += new_part

        print(response.decode())

    except KeyboardInterrupt:
        print("Client terminated by user (Ctrl+C)")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the client socket
        client_socket.close()

# Main function to start the web client
def main():
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python3 Webclient.py serverAddress serverPort filename")
        sys.exit(1)

    # Get the server address, server port, and filename from command line arguments
    server_address = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

    # Send an HTTP GET request to the server
    send_get_request(server_address, server_port, filename)

if __name__ == "__main__":
    main()