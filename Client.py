#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
客户端启动程序，启动前需要先启动服务端
'''

from socket import *
import time
import truling_machine as truling

def creatTcpClientSocket(ADDR):
	tcpClientSocket = socket(AF_INET, SOCK_STREAM)
	tcpClientSocket.connect(ADDR)
	return tcpClientSocket


def creatTcpClient(PORT, HOST = "localhost", BFSIZE = 1024):
    ADDR = (HOST, PORT)
    tcpClientSocket = creatTcpClientSocket(ADDR)

    while True:
        data = input(">>>")
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
    
def main():
    print("Hello! You can choose automatic reply machines below:")
    print("1.Alice")
    print("2.Turling machine")
    while True:
        try:
            choose = int(input(">>>input number: "))
            if choose == 1:
                input("Please open the Server.py first")
                creatTcpClient(HOST = "localhost", PORT = 12567)
                break
            elif choose == 2:
                truling.trulingServer()
                break
            else:
                continue
        except:
            continue

main()