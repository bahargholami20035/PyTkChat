# client_gui.py

import socket
import threading
import sys
import tkinter as tk
from tkinter import scrolledtext, simpledialog

class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.username = ""

        self.root = tk.Tk()
        self.root.title("Chat Client")

        self.chat_log = scrolledtext.ScrolledText(self.root, state='disabled', width=50, height=20)
        self.chat_log.pack(padx=10, pady=10)

        self.message_entry = tk.Entry(self.root, width=40)
        self.message_entry.pack(padx=10, pady=5)
        self.message_entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

        self.connect_to_server()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def connect_to_server(self):
        try:
            self.client_socket.connect((self.host, self.port))
            self.get_username()
            self.display_message(f"Connected to {self.host}:{self.port}")

            self.receive_thread = threading.Thread(target=self.receive_messages)
            self.receive_thread.daemon = True
            self.receive_thread.start()

        except (ConnectionRefusedError, Exception) as e:
            self.display_message(f"Connection failed: {e}")
            sys.exit(1)

    def get_username(self):
        self.username = simpledialog.askstring("Username", "Enter username:", parent=self.root)
        self.username = self.username or "Anonymous"
        self.client_socket.sendall(f"USERNAME:{self.username}".encode('utf-8'))

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if not message:
                    self.display_message("Disconnected from server.")
                    self.client_socket.close()
                    break
                self.display_message(message)
            except (ConnectionResetError, OSError):
                self.display_message("Connection lost.")
                self.client_socket.close()
                break

    def send_message(self, event=None):
        message = self.message_entry.get().strip()
        if message:
            try:
                self.client_socket.sendall(f"{self.username}: {message}".encode('utf-8'))
                self.message_entry.delete(0, tk.END)
            except (ConnectionResetError, OSError, BrokenPipeError):
                self.display_message("Send failed.")
                self.client_socket.close()

    def display_message(self, message):
        self.chat_log.configure(state='normal')
        self.chat_log.insert(tk.END, message + "\n")
        self.chat_log.configure(state='disabled')
        self.chat_log.see(tk.END)

    def on_closing(self):
        try:
            self.client_socket.close()
        except:
            pass
        self.root.destroy()
        sys.exit(0)

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 12345
    ChatClient(HOST, PORT)