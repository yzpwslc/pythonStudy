#coding=utf-8
import socket

HOST = '127.0.0.1'
PORT = 8000
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect((HOST,PORT))
data = "hello"
while data:
    s.sendall(data.encode('utf-8'))
    data = s.recv(512)
    print("Receive from server:\n",data.decode('utf-8'))
    data = input('please input a info:\n')
s.close()