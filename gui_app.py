import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet
import os

# Generate a key and save it
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    status_label.config(text="Key Generated Successfully!")

# Load the previously generated key
def load_key():
    if not os.path.exists("secret.key"):
        status_label.config(text="Error: No secret.key found. Generate the key first.")
        return None
    return open("secret.key", "rb").read()

# Encrypt the file
def encrypt_file():
    file_name = filedialog.askopenfilename()
    key = load_key()
    if key is None:
        return
    fernet = Fernet(key)

    with open(file_name, "rb") as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    with open(file_name + ".enc", "wb") as file:
        file.write(encrypted_data)
    
    status_label.config(text="File Encrypted Successfully!")

# Decrypt the file
def decrypt_file():
    file_name = filedialog.askopenfilename()
    key = load_key()
    if key is None:
        return
    fernet = Fernet(key)

    with open(file_name, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(file_name[:-4], "wb") as file:
        file.write(decrypted_data)
    
    status_label.config(text="File Decrypted Successfully!")

# GUI setup
root = tk.Tk()
root.title("File Encryptor/Decryptor")
root.geometry("400x300")

# Generate key button
generate_key_button = tk.Button(root, text="Generate Key", command=generate_key)
generate_key_button.pack(pady=10)

# Encrypt button
encrypt_button = tk.Button(root, text="Encrypt File", command=encrypt_file)
encrypt_button.pack(pady=10)

# Decrypt button
decrypt_button = tk.Button(root, text="Decrypt File", command=decrypt_file)
decrypt_button.pack(pady=10)

# Status label
status_label = tk.Label(root, text="")
status_label.pack(pady=20)

root.mainloop()

NA






