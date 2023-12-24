import socket
import threading

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            broadcast(message, client_socket)
        except:
            index = clients.index(client_socket)
            clients.remove(client_socket)
            client_socket.close()
            print(f"Client {index} disconnected")
            break

def broadcast(message, sender):
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
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()
