import socket
from encryption import encrypt_data
from key_management import load_key

# Load the key
key = load_key()

# Start a TCP client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("", 12345))

data_to_send = b"Hello, secure server!"  # Data to send
encrypted_data = encrypt_data(data_to_send, key)  # Encrypt the data
client_socket.send(encrypted_data)  # Send encrypted data to the server
print("Encrypted data sent.")
client_socket.close()  # Close the connection after sending the data
