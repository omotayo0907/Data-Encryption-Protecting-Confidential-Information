import tkinter as tk
from tkinter import filedialog, messagebox
import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Load the server's public key
def load_public_key():
    with open("public.pem", "rb") as f:
        public_key = RSA.import_key(f.read())
    return public_key

# Function to send encrypted file to server
def send_file():
    file_path = filedialog.askopenfilename(title="Select File to Send")
    if not file_path:
        messagebox.showerror("Error", "No file selected")
        return

    try:
        with open(file_path, "rb") as file:
            file_data = file.read()

        # Encrypt the file data using RSA public key
        public_key = load_public_key()
        cipher_rsa = PKCS1_OAEP.new(public_key)
        encrypted_data = cipher_rsa.encrypt(file_data[:245])  # RSA limit per chunk

        # Send the encrypted data to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", 9999))
        client_socket.send(encrypted_data)
        client_socket.close()

        messagebox.showinfo("Success", "File sent successfully")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Client: Send Encrypted File")
root.geometry("400x200")

# Send button
send_button = tk.Button(root, text="Send Encrypted File", command=send_file)
send_button.pack(pady=50)

# Status label
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()



