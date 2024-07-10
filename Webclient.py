from socket import * # Import socket module
import sys, os, errno
import time

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

clientSocket = socket(AF_INET, SOCK_STREAM)
receive_buffer_size = 4098
clientSocket.setsockopt(SOL_SOCKET, SO_RCVBUF, receive_buffer_size)

# Assign a port number
# serverPort = 6789

if len(sys.argv) < 4:
    print("Usage: python3 " + sys.argv[0] + " serverAddr serverPort filename")
    sys.exit(1)
serverAddr = sys.argv[1]
serverPort = int(sys.argv[2])
fileName = sys.argv[3]

# Connect to the server
try:
    clientSocket.connect((serverAddr,serverPort))
    
except error as e:
    print("Connection to server failed. " + str(e))
    sys.exit(1)
print('------The client is ready to send--------')
print(str(clientSocket.getsockname()) + '-->' + str(clientSocket.getpeername()))

try:
    #getRequest = "GET /" + fileName + " HTTP/1.1\r\nHost: " + serverAddr + "\r\n"
    #getRequest = getRequest + "Accept: text/html\r\nConnection: keep-alive\r\n"
    getRequest = "GET /{} HTTP/1.1\r\nHost: {}\r\nAccept: text/html\r\nConnection: keep-alive\r\n\r\n".format(fileName, serverAddr)

    clientSocket.send(getRequest.encode())

    time.sleep(1)
except error as e:
    print("Error sending GET request: " + str(e))
    clientSocket.close()
    sys.exit(1)
    
message = ""
while True:
    try:
        newPart = clientSocket.recv(receive_buffer_size)
        if not newPart:
            break
        message += newPart.decode()
        print("Object size: ", len(message), flush=True)
        time.sleep(0.1)
        
        if len(message) >= receive_buffer_size:
            print("buffer full...")
            time.sleep(1)
            message = ""
        #if message[len(message)-1] != "\n":
            #continue
        #else:
           # print(message, flush=True)
            #message = ""
        message = message + newPart.decode()

    except error as e:
        print('Error reading socket: ' + str(e))
        sys.exit(1)

clientSocket.close()
sys.exit(0)
