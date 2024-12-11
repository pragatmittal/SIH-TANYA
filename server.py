# from flask import Flask, render_template, request
# import socket
# import datetime

# app = Flask(__name__)

# # Global list to store all decrypted messages with additional info (MAC, IP, Timestamp)
# message_log = []

# # Example encryption and decryption functions (replace with actual logic)
# def encrypt_message(message):
#     return message[::-1]  # Reverse string for simplicity (encryption)

# def decrypt_message(message):
#     return message[::-1]  # Reverse string back to original (decryption)

# # Function to get MAC address by IP (Note: This might require administrative privileges on some systems)
# def get_mac_address(ip):
#     try:
#         # Get the MAC address from the system for the given IP address
#         # (This might work only for machines in the same local network)
#         host = socket.gethostbyaddr(ip)
#         return host[0]
#     except socket.herror:
#         return "Unknown"

# @app.route('/')
# def home():
#     # Render the page with the message log (all decrypted messages)
#     return render_template('server_display.html', message_log=message_log)

# @app.route('/receive_message', methods=['POST'])
# def receive_message():
#     # Get the encrypted message from the client
#     encrypted_message = request.form['encrypted_message']
    
#     # Get the client's IP address
#     client_ip = request.remote_addr

#     # Get the MAC address of the client (optional, this might not work in all environments)
#     client_mac = get_mac_address(client_ip)
    
#     # Decrypt the message on the server side
#     decrypted_message = decrypt_message(encrypted_message)
    
#     # Get the current time when the message is received
#     received_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
#     # Print the decrypted message and other details to the server terminal
#     print(f"Decrypted Message: {decrypted_message}")
#     print(f"From IP: {client_ip}, MAC: {client_mac}, Time: {received_time}")
    
#     # Add the decrypted message and other details to the message log
#     message_log.append({
#         'decrypted_message': decrypted_message,
#         'client_ip': client_ip,
#         'client_mac': client_mac,
#         'received_time': received_time
#     })

#     # Render the page with the updated message log
#     return render_template('server_display.html', message_log=message_log)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)


from flask import Flask, render_template, request
import socket
import datetime

app = Flask(__name__)

# Global list to store all decrypted messages with additional info (MAC, IP, Timestamp)
message_log = []

# Example encryption and decryption functions (replace with actual logic)
def encrypt_message(message):
    return message[::-1]  # Reverse string for simplicity (encryption)

def decrypt_message(message):
    return message[::-1]  # Reverse string back to original (decryption)

# Function to get MAC address by IP (Note: This might require administrative privileges on some systems)
def get_mac_address(ip):
    try:
        # Get the MAC address from the system for the given IP address
        # (This might work only for machines in the same local network)
        host = socket.gethostbyaddr(ip)
        return host[0]
    except socket.herror:
        return "Unknown"

@app.route('/')
def home():
    # Render the page with the message log (all decrypted messages)
    return render_template('server_display.html', message_log=message_log)

@app.route('/receive_message', methods=['POST'])
def receive_message():
    # Get the encrypted message from the client
    encrypted_message = request.form['encrypted_message']
    
    # Get the client's IP address
    client_ip = request.remote_addr

    # Get the MAC address of the client (optional, this might not work in all environments)
    client_mac = get_mac_address(client_ip)
    
    # Decrypt the message on the server side
    decrypted_message = decrypt_message(encrypted_message)
    
    # Get the current time when the message is received
    received_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Print the decrypted message and other details to the server terminal
    print(f"Decrypted Message: {decrypted_message}")
    print(f"From IP: {client_ip}, MAC: {client_mac}, Time: {received_time}")
    
    # Add the decrypted message and other details to the message log
    message_log.append({
        'decrypted_message': decrypted_message,
        'client_ip': client_ip,
        'client_mac': client_mac,
        'received_time': received_time
    })

    # Render the page with the updated message log
    return render_template('server_display.html', message_log=message_log)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
# from flask import Flask, render_template, request, jsonify
# import socket
# import datetime

# app = Flask(__name__)

# # Global list to store all decrypted messages with additional info (MAC, IP, Timestamp)
# message_log = []

# # Example encryption and decryption functions (replace with actual logic)
# def encrypt_message(message):
#     return message[::-1]  # Reverse string for simplicity (encryption)

# def decrypt_message(message):
#     return message[::-1]  # Reverse string back to original (decryption)

# # Function to get MAC address by IP (Note: This might require administrative privileges on some systems)
# def get_mac_address(ip):
#     try:
#         # Get the MAC address from the system for the given IP address
#         host = socket.gethostbyaddr(ip)
#         return host[0]
#     except socket.herror:
#         return "Unknown"

# @app.route('/')
# def home():
#     # Render the page with the message log (all decrypted messages)
#     return render_template('server_display.html', message_log=message_log)

# @app.route('/receive_message', methods=['POST'])
# def receive_message():
#     # Get the encrypted message from the client
#     encrypted_message = request.form['encrypted_message']
    
#     # Get the client's IP address
#     client_ip = request.remote_addr

#     # Get the MAC address of the client (optional, this might not work in all environments)
#     client_mac = get_mac_address(client_ip)
    
#     # Decrypt the message on the server side
#     decrypted_message = decrypt_message(encrypted_message)
    
#     # Get the current time when the message is received
#     received_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
#     # Print the decrypted message and other details to the server terminal
#     print(f"Decrypted Message: {decrypted_message}")
#     print(f"From IP: {client_ip}, MAC: {client_mac}, Time: {received_time}")
    
#     # Add the decrypted message and other details to the message log
#     message_log.append({
#         'decrypted_message': decrypted_message,
#         'client_ip': client_ip,
#         'client_mac': client_mac,
#         'received_time': received_time
#     })

#     # Render the page with the updated message log
#     return render_template('server_display.html', message_log=message_log)

# @app.route('/messages')
# def get_messages():
#     return jsonify(message_log)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)


# from flask import Flask, render_template, request, jsonify
# import datetime
# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_OAEP
# import base64
# import os

# app = Flask(__name__)

# # Global list to store all decrypted messages with additional info (MAC, IP, Timestamp)
# message_log = []

# # Load the RSA private key for decryption
# def load_private_key():
#     try:
#         with open("private.pem", "rb") as f:
#             private_key = RSA.import_key(f.read())
#         return private_key
#     except Exception as e:
#         print(f"Error loading private key: {str(e)}")
#         return None

# # Function to decrypt the message using RSA
# def decrypt_message_rsa(encrypted_message):
#     try:
#         private_key = load_private_key()
#         if private_key is None:
#             return "Private key not loaded"
        
#         cipher = PKCS1_OAEP.new(private_key)
#         encrypted_message_bytes = base64.b64decode(encrypted_message)
#         decrypted_message = cipher.decrypt(encrypted_message_bytes)
#         return decrypted_message.decode()
#     except Exception as e:
#         print(f"Error during decryption: {e}")
#         return f"Decryption failed: {str(e)}"

# # Function to get MAC address by IP (using arp command on Unix-like systems)
# def get_mac_address(ip):
#     try:
#         # Run system command to fetch the MAC address
#         # On Unix/Linux/MacOS, using 'arp' command
#         result = os.popen(f"arp -n {ip}").read()
#         # Extract the MAC address from the result
#         for line in result.splitlines():
#             if ip in line:
#                 return line.split()[-1]
#         return "Unknown"
#     except Exception as e:
#         return "Unknown"

# @app.route('/')
# def home():
#     # Render the page with the message log (all decrypted messages)
#     return render_template('server_display.html', message_log=message_log)

# @app.route('/receive_message', methods=['POST'])
# def receive_message():
#     # Get the encrypted message from the client
#     encrypted_message = request.form['encrypted_message']
    
#     # Get the client's IP address
#     client_ip = request.remote_addr

#     # Get the MAC address of the client (optional, this might not work in all environments)
#     client_mac = get_mac_address(client_ip)
    
#     # Decrypt the message on the server side using RSA
#     decrypted_message = decrypt_message_rsa(encrypted_message)
    
#     # Get the current time when the message is received
#     received_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
#     # Print the decrypted message and other details to the server terminal
#     print(f"Decrypted Message: {decrypted_message}")
#     print(f"From IP: {client_ip}, MAC: {client_mac}, Time: {received_time}")
    
#     # Add the decrypted message and other details to the message log
#     message_log.append({
#         'decrypted_message': decrypted_message,
#         'client_ip': client_ip,
#         'client_mac': client_mac,
#         'received_time': received_time
#     })

#     # Render the page with the updated message log
#     return render_template('server_display.html', message_log=message_log)

# @app.route('/messages')
# def get_messages():
#     return jsonify(message_log)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)
