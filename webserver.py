from socket import * #import socket module
import sys # In order to terminate the program
import errno
import os

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#serverPort = 80
try:
    if len(sys.argv) < 2:
        print ("Usage: python3 " + sys.argv[0] + " serverPort")
        sys.exit(1)
    serverPort = int(sys.argv[1])
   #Fill in start
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
   #Fill in end
except error as e:
    print("Server takes a few minutes to close, try again." + str(e))
    sys.exit(1)


while True:
    try:
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, serverAddr = serverSocket.accept() #Fill in start #Fill in end
    except KeyboardInterrupt:
        print("Server closed" + str(KeyboardInterrupt))
        sys.exit(1)

    try:
        message =  connectionSocket.recv(1024).decode() #Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() #Fill in start #Fill in end
        
        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
        #sys.exit(1)
    except IOError:
        #Send response message for file not found
        #Fill in start
        connectionSocket.send("HTTP/1.1 ERROR 404\r\n\r\n".encode())
        connectionSocket.send("404 Not Found\r\n\r\n".encode())
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        sys.exit(1)
        #Fill in 
    
    serverSocket.close()
    sys.exit(0) #Terminate the program after sending data
