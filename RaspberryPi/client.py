import socket
from sense_emu import SenseHat
sense=SenseHat()
'''
HOST = '10.21.12.164'
PORT = 8000
'''
HOST,PORT = '10.21.12.164',8000
clientMessage = str(round(sense.pressure,1))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(clientMessage.encode())
    serverMessage = str(client.recv(1024), encoding='utf-8')
    print('Server:', serverMessage)