from Crypto.PublicKey import RSA

# Generate RSA keys for server
key = RSA.generate(2048)
private_key = key.export_key()
with open("private.pem", "wb") as private_file:
    private_file.write(private_key)

public_key = key.publickey().export_key()
with open("public.pem", "wb") as public_file:
    public_file.write(public_key)

print("RSA Keys generated and saved as private.pem and public.pem")



