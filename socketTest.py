"""
# socketTest.py
# Copyright (C) 2019 ...
# Author : Huangtao
# Version: V1.0.0  2019-09-30 Create
# Description: threading, time, socket, 
#
"""
import threading
import time
import socket

def myServer():
    print("Server:")
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    ss.bind((host, port))
    ss.listen(4)
    while True:
        client, addr = ss.accept()
        print("new client, addr: %s" % str(addr))
        times = 10
        while(times > 0):
            msg = client.recv(10)
            print(msg)
            time.sleep(1)
            times -= 1
        client.close()
        break
    ss.close()

def myClient():
    print("Client:")
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    sc.connect((host, port))
    index = 1
    sendMsg = "Hello!"
    while True:
        sc.send(sendMsg.encode(encoding='UTF-8'))
        index += 1
        if (index > 5):
            break
        time.sleep(1)
    sc.close()

thread1 = threading.Thread(target=myServer)
thread2 = threading.Thread(target=myClient)
thread1.start()
thread2.start()

