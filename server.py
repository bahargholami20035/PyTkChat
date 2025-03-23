import socket
import threading

clients = {}
lock = threading.Lock()

def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")
    
    try:
        username = client_socket.recv(1024).decode('utf-8').strip()
        if not username.startswith("USERNAME:"):
            client_socket.close()
            return
        
        username = username.split(":", 1)[1]
        with lock:
            clients[client_socket] = username
        
        broadcast(f"{username} has joined the chat!", client_socket)
        
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"{username} ({address}): {message}")
            broadcast(f"{username}: {message}", client_socket)

    except (ConnectionResetError, BrokenPipeError):
        print(f"Client {address} disconnected.")

    finally:
        with lock:
            del clients[client_socket]
        client_socket.close()
        broadcast(f"{username} has left the chat.", None)
        print(f"Connection with {address} closed.")

def broadcast(message, sender_socket):
    with lock:
        for client in list(clients.keys()):
            if client != sender_socket:
                try:
                    client.sendall(message.encode('utf-8'))
                except (ConnectionResetError, BrokenPipeError):
                    client.close()
                    del clients[client]

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, address = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_socket, address), daemon=True).start()

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 12345
    start_server(HOST, PORT)
