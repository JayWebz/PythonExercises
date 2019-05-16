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
import socket

host = ''        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(1024)
    data = data[::-1]
    if not data: break
    conn.sendall(data)
conn.close()