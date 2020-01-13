#!/usr/bin/env python
#-*-coding:utf-8-*-

'''客户端启动程序，启动前需要先启动服务端'''

from socket import *
import time

def creatTcpClientSocket(ADDR):
	tcpClientSocket = socket(AF_INET, SOCK_STREAM)
	tcpClientSocket.connect(ADDR)
	return tcpClientSocket

def creatTcpClient(PORT, HOST = "localhost", BFSIZE = 1024):
    ADDR = (HOST, PORT)
    tcpClientSocket = creatTcpClientSocket(ADDR)

    while True:
        data = input("> ")
        if not data:
            break
        string = "[%s]\nMe: %s" % (time.ctime(), data)
        print(string)
        data = bytes(data, 'utf-8')
        tcpClientSocket.send(data)

        data = tcpClientSocket.recv(BFSIZE)
        if not data:
            break
        data = data.decode('utf-8')
        data = "[%s]\nAlice: %s" % (time.ctime(), data)
        print(data)
    tcpClientSocket.close()

creatTcpClient(HOST = "localhost", PORT = 12567)