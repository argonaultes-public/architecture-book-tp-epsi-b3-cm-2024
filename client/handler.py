import socket
import jsonpickle
from modeldto.Book import Book

data = "hello world"

# Create a socket (SOCK_STREAM means a TCP socket)
def handle_request(request):
    HOST, PORT = "localhost", 9998
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(request + "\n", "utf-8"))

        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        print("Sent:     {}".format(request))
        print("Received: {}".format(received))
        decode_response = jsonpickle.decode(received, classes=Book)
        return decode_response


