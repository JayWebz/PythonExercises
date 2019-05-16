#! /usr/bin/python
# Exercise No.   2
# File Name:     hw14server.py
# Programmer:    Jon Weber
# Date:          Dec. 3, 2017
#
# Problem Statement: 
#
# Overall Plan:
# 1.  
#
# import the necessary python libraries
# echo_client.py
import socket

host = socket.gethostname()    
port = 12345                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(b'This string is reversed!')
data = s.recv(1024)
s.close()
print('Received', repr(data))