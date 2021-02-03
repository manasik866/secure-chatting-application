import socket

serverScoket = socket.socket()
serverIP = '127.0.0.1'
serverPort = 8080

print("Server IP: " + str(serverIP) + "\tPort Number: " + str(serverPort))

serverScoket.bind((serverIP, serverPort))
print('server done binding to host and port successfully')
print('server is waiting for incoming connections')

serverScoket.listen(1)

clientsocket, address = serverScoket.accept()
print(address, " Has connected to the server and is now online...")

def CreateThreadforSendingMessage(serverSocket):
   while True: 
      display_mess = input(str('>>'))
      display_mess = display_mess.encode()
      clientsocket.send(display_mess)
      print(' message has been sent...')
      in_message = clientsocket.recv(1024)
   _  messagge = in_message.decode('utf-8')
      print(" Client:", _messagge)
