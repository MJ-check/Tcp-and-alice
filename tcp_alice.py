#!/usr/bin/env python

#-*-coding:utf-8-*-

from socket import *
import time
import alice

def creatTcpServerSocket(ADDR):
	tcpServerSocket = socket(AF_INET, SOCK_STREAM)
	tcpServerSocket.bind(ADDR)
	tcpServerSocket.listen(5)
	return tcpServerSocket


def creatTcpClientSocket(ADDR):
	tcpClientSocket = socket(AF_INET, SOCK_STREAM)
	tcpClientSocket.connect(ADDR)
	return tcpClientSocket


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
