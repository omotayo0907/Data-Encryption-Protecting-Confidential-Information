import tkinter as tk
from tkinter import messagebox
import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

# Load the server's private key
def load_private_key():
    with open("private.pem", "rb") as f:
        private_key = RSA.import_key(f.read())
    return private_key

# Function to receive and save the encrypted file
def receive_file():
    try:
        # Start server socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("localhost", 9999))
        server_socket.listen(1)
        status_label.config(text="Waiting for connection...")

        conn, addr = server_socket.accept()
        status_label.config(text=f"Connection from {addr}")

        # Receive encrypted data
        encrypted_data = conn.recv(1024)
        conn.close()

        # Save the encrypted file
        with open("received_encrypted_file.enc", "wb") as file:
            file.write(encrypted_data)

        status_label.config(text="File received successfully")
        messagebox.showinfo("Success", "File received successfully")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to manually decrypt the received file
def decrypt_file():
    try:
        if not os.path.exists("received_encrypted_file.enc"):
            messagebox.showerror("Error", "No encrypted file found to decrypt")
            return

        # Load the private key
        private_key = load_private_key()
        cipher_rsa = PKCS1_OAEP.new(private_key)

        # Read the encrypted file
        with open("received_encrypted_file.enc", "rb") as file:
            encrypted_data = file.read()

        # Decrypt the data
        decrypted_data = cipher_rsa.decrypt(encrypted_data)

        # Save the decrypted file
        with open("received_decrypted_file", "wb") as file:
            file.write(decrypted_data)

        status_label.config(text="File decrypted successfully")
        messagebox.showinfo("Success", "File decrypted successfully")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Server: Receive and Decrypt File")
root.geometry("400x300")

# Receive button
receive_button = tk.Button(root, text="Receive Encrypted File", command=receive_file)
receive_button.pack(pady=10)

# Decrypt button
decrypt_button = tk.Button(root, text="Decrypt Received File", command=decrypt_file)
decrypt_button.pack(pady=10)

# Status label
status_label = tk.Label(root, text="")
status_label.pack(pady=20)

# Run the server in a loop
def run_server():
    while True:
        receive_file()

# Start the server in a separate thread to keep GUI responsive
import threading
server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()

root.mainloop()



