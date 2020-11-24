import socket
from sense_emu import SenseHat
sense=SenseHat()

HOST,PORT = '10.21.12.164',8000
#10.21.12.164

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)
try:
    while True:
        conn, addr = server.accept()
        clientMessage = str(conn.recv(1024), encoding='utf-8')
        print('Client message is:', clientMessage)
        serverMessage = "I'm here!"
        conn.sendall(serverMessage.encode())
        sense.show_message(clientMessage)
        conn.close()
except KeyboardInterrupt as e:
    print('server close')
finally:
    server.close()