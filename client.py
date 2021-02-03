#!/usr/bin/python3
import socket
import threading
from cryptography.fernet import Fernet

clientName = input(str('Enter your name: '))
name = input(str('Enter the Ip to connect: '))
x=socket.socket()
h_name= '192.168.194.129'
Port = 1024
key = b'ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg='
f = Fernet(key)
def CreateThreadforSendingMessage(serverSocket):
    while True:
        in_message= input(str('>>'))
        message = clientName + '_' + name + '_' + in_message
        message=  message.encode()
        encrypted_Message = f.encrypt(message)
        serverSocket.send(encrypted_Message)


x.connect((h_name, Port))
print("Connected to chat server")

t = threading.Thread(target=CreateThreadforSendingMessage, args=(x,))
t.start()

while True:
   try:
        incoming_message = x.recv(1024)
        decrypted_message = f.decrypt(incoming_message)
        decode = decrypted_message.decode('utf-8')
        print(decode)
   except:
        print('Exception caught')
