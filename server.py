# server.py

import socket
import threading

def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")

    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received from {address}: {message}")
            broadcast(message, client_socket)

    except (ConnectionResetError, BrokenPipeError):
        print(f"Client {address} disconnected.")
    finally:
        client_socket.close()
        clients.remove(client_socket)
        print(f"Connection with {address} closed.")


def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.sendall(message.encode('utf-8'))
            except (ConnectionResetError, BrokenPipeError):
                print(f"Error sending to a client.")


def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, address = server_socket.accept()
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket, address)).start()

clients = []

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 12345
    start_server(HOST, PORT)