import select
import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Never block on read/write operations
server.setblocking(0)

# Bind the socket to the port
server.bind(('localhost', 10_000))
server.listen(8)

while True:
    # select() returns 3 arrays containing the object (sockets, files...)
    # that are ready to be read, written to or raised an error
inputs, outputs, excepts = select.select([server], [], [server])
if server in inputs:
    connection, client_address = server.accept()
    connection.send("hello!\n")