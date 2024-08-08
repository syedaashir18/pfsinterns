import tkinter as tk
from tkinter import filedialog
import socket
import threading
import os

# Function to send file
def send_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        s = socket.socket()
        s.connect((receiver_ip.get(), int(receiver_port.get())))
        with open(file_path, 'rb') as file:
            s.sendfile(file)
        s.close()

# Function to receive file
def receive_file():
    s = socket.socket()
    s.bind((receiver_ip.get(), int(receiver_port.get())))
    s.listen(1)
    conn, addr = s.accept()
    with open('received_file', 'wb') as file:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)
    conn.close()
    s.close()

# Function to start receiving in a new thread
def start_receiving():
    threading.Thread(target=receive_file).start()

# GUI setup
root = tk.Tk()
root.title("File Sharing App")

tk.Label(root, text="Receiver IP:").grid(row=0, column=0)
receiver_ip = tk.Entry(root)
receiver_ip.grid(row=0, column=1)

tk.Label(root, text="Receiver Port:").grid(row=1, column=0)
receiver_port = tk.Entry(root)
receiver_port.grid(row=1, column=1)

tk.Button(root, text="Send File", command=send_file).grid(row=2, column=0)
tk.Button(root, text="Receive File", command=start_receiving).grid(row=2, column=1)

root.mainloop()
