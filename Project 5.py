import socket
import threading
HOST = '127.0.0.1' 
PORT = 65432       
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Connection closed")
            break
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()
while True:
    message = input()
    client_socket.send(message.encode('utf-8'))
