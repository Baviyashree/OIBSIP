import socket
import threading
HOST = '127.0.0.1'  
PORT = 65432       
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
clients = []
def handle(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            broad(message, client_socket)
        except:
            index = clients.index(client_socket)
            clients.remove(client_socket)
            client_socket.close()
            print(f"Client {index} disconnected")
            break
def broad(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)
while True:
    client_socket, address = server.accept()
    print(f"Client {len(clients)} connected")
    clients.append(client_socket)
    thread = threading.Thread(target=handle, args=(client_socket,))
    thread.start()
