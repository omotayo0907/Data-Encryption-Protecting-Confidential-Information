# Data-Encryption-Protecting-Confidential-Information
### Project Overview: Data-Encryption-Protecting-Confidential-Information
#### Project Summary
This project aimed to enhance data security through encryption both at rest and in transit. It featured a two-part system:

1. **Data at Rest**: Encrypting and decrypting files stored on disk to protect sensitive information when not in use.
2. **Data in Transit**: Securing communication between a client and server to ensure that transmitted data remains confidential and intact.

## Requirements
- Python 3.x
- `cryptography` library
- `tkinter` library (usually included with Python)

#### Implementation Details

##### Data at Rest
For protecting files at rest, the project used AES (Advanced Encryption Standard) encryption. A Python GUI application was developed to facilitate the encryption and decryption of files:

- **Encryption**: The application encrypts user-selected files using AES. Encrypted files are saved with a `.enc` extension.
- **Decryption**: The application allows decryption of encrypted files back to their original form.

A key file, `secret.key`, was utilized to perform these operations. A "Generate Key" button was included in the GUI to create this key if it was not present.

##### Data in Transit
To secure data transmitted over a network, RSA (Rivest-Shamir-Adleman) encryption was used. This part of the project involved:

- **Client Application**: Provides a GUI to select and send encrypted files to a server. The file is encrypted using the server’s public RSA key before transmission.
- **Server Application**: Automatically listens for incoming connections, receives encrypted files, and saves them. The server includes an option to manually decrypt received files using its private RSA key.

### How the Project Was Implemented

1. **File Encryption and Decryption**: Implemented using Python and the `cryptography` library, with a `Tkinter` GUI for user interaction.
2. **Network Communication Security**: Utilized RSA encryption for securing messages between client and server, with separate GUIs for each.
3. **Key Management**: Key generation and management were integrated into the project, including options to generate encryption keys via the GUI or command line.

## How to Run the Program

### Cloning the Repository
1. Clone the repository:
2. 
   git clone https://github.com/omotayo0907/Data-Encryption-Protecting-Confidential-Information.git
```bash
   cd File_encryption_project
```

### Generating Keys
1. Generate RSA keys if not already present:
   ```bash
   python3 keygen.py
   ```

### Running the Server
1. Start the server to listen for incoming connections:
   ```bash
   python3 server.py
   ```

### Running the Client
1. Open a new terminal window and run the client:
   ```bash
   python3 client.py
   ```

### Using the Applications
- **Server**: Click "Receive Encrypted File" to wait for files from the client. After receiving a file, use the "Decrypt Received File" button to manually decrypt it.
- **Client**: Click "Send Encrypted File" to select and send a file to the server.

