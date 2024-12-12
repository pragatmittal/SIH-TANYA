# # from flask import Flask
# # from flask_socketio import SocketIO
# # import psutil
# # import time

# # # Initialize the Flask app and SocketIO
# # app = Flask(__name__)
# # socketio = SocketIO(app)

# # # Define the function that sends system stats periodically
# # def send_system_stats():
# #     while True:
# #         # Gather system stats using psutil
# #         cpu_usage = psutil.cpu_percent(interval=1)  # 1-second interval
# #         memory_info = psutil.virtual_memory()
# #         disk_info = psutil.disk_usage('/')

# #         system_stats = {
# #             'cpu_usage': cpu_usage,
# #             'memory_usage': memory_info.percent,
# #             'disk_usage': disk_info.percent
# #         }

# #         # Emit the stats to all connected clients
# #         socketio.emit('system_stats', system_stats)
        
# #         # Wait for 5 seconds before sending the next update
# #         time.sleep(5)

# # # Route for serving the web app (you can customize the HTML or use a template)
# # @app.route('/')
# # def index():
# #     return "WebSocket Server is running"

# # # Event handler for new WebSocket connections
# # @socketio.on('connect')
# # def handle_connect():
# #     print("A client connected")
# #     # Start sending stats in the background when a client connects
# #     socketio.start_background_task(target=send_system_stats)

# # # Start the Flask app
# # if __name__ == '__main__':
# #     socketio.run(app, debug=True)


# from flask import Flask, request
# from cryptography.hazmat.primitives.asymmetric import rsa, padding
# from cryptography.hazmat.primitives import serialization, hashes

# app = Flask(__name__)

# # Load private key for RSA decryption
# with open("private.pem", "rb") as key_file:
#     private_key = serialization.load_pem_private_key(
#         key_file.read(),
#         password=None
#     )

# @app.route('/')
# def home():
#     return "Secure Messaging System"

# @app.route('/encrypt', methods=['POST'])
# def encrypt():
#     encrypted_message = request.form['message']
#     algorithm = request.form['algorithm']

#     if algorithm == "rsa":
#         # Decrypt the message using RSA private key
#         try:
#             encrypted_bytes = bytes.fromhex(encrypted_message)
#             decrypted_message = private_key.decrypt(
#                 encrypted_bytes,
#                 padding.OAEP(
#                     mgf=padding.MGF1(algorithm=hashes.SHA256()),
#                     algorithm=hashes.SHA256(),
#                     label=None
#                 )
#             )
#             return f"Decrypted message: {decrypted_message.decode()}"
#         except Exception as e:
#             return f"Error decrypting RSA message: {str(e)}"

#     return "Unsupported encryption algorithm!"

# if __name__ == "_main_":
#     app.run(host="0.0.0.0", port=5000, debug=True)




from flask import Flask, render_template, request, redirect, url_for, session
import datetime
from encryption import encrypt_data, decrypt_data
from key_management import load_key
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Global list to store all decrypted messages with additional info
message_log = []

# Load the encryption key
key = load_key("key.key")

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Mock credentials
    if username == 'admin' and password == 'password':
        session['username'] = username
        return redirect(url_for('dashboard'))
    return render_template('index.html', error='Invalid credentials')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('home'))
    return render_template('server_display.html', message_log=message_log)

@app.route('/receive_message', methods=['POST'])
def receive_message():
    if 'username' not in session:
        return redirect(url_for('home'))

    encrypted_message = request.form['encrypted_message']
    client_ip = request.remote_addr
    client_mac = "00:00:00:00:00:00"  # Placeholder for MAC address

    # Decrypt the message
    decrypted_message = decrypt_data(encrypted_message, key)

    # Get the current time when the message is received
    received_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Add the decrypted message and other details to the message log
    message_log.append({
        'decrypted_message': decrypted_message.decode(),
        'client_ip': client_ip,
        'client_mac': client_mac,
        'received_time': received_time
    })

    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)