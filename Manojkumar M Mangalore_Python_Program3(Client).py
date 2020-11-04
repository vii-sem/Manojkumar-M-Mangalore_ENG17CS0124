import socket # Import socket module
s =socket.socket() # Create a socket object
host=socket.gethostname() # Get local machine name
port=50000# Reserve a port for your service.
s.connect((host, port))
s.recv(1024)
s.close() # Close the socket when don
                                    