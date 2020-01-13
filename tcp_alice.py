#!/usr/bin/env python
#-*-coding:utf-8-*-

'''服务器使用的服务器模块，提供服务器可以使用的功能
   目前包含使用asml库实现简单的人机对话以及实现服务器程序简单的函数使用
'''

from socket import *
import time
import alice

def creatTcpServerSocket(ADDR):
	tcpServerSocket = socket(AF_INET, SOCK_STREAM)
	tcpServerSocket.bind(ADDR)
	tcpServerSocket.listen(5)
	return tcpServerSocket

def creatTcpServer(PORT, HOST = "", BFSIZE = 1024):
    ADDR = (HOST, PORT)
    tcpServerSocket = creatTcpServerSocket(ADDR)

    while True:
        print("wait for connect")
        tcpClientSocket, addr = tcpServerSocket.accept()
        print("connectted from:", addr)

        while True:
            data = tcpClientSocket.recv(BFSIZE)
            if not data:
                break
            data = data.decode("utf-8")
            data = alice.aliceRespond(data)
            data = bytes(data, "utf-8")
            tcpClientSocket.send(data)
        tcpClientSocket.close()
    tcpServerSocket.close()