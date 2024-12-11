# from flask import Flask
# from flask_socketio import SocketIO
# import psutil
# import time

# # Initialize the Flask app and SocketIO
# app = Flask(__name__)
# socketio = SocketIO(app)

# # Define the function that sends system stats periodically
# def send_system_stats():
#     while True:
#         # Gather system stats using psutil
#         cpu_usage = psutil.cpu_percent(interval=1)  # 1-second interval
#         memory_info = psutil.virtual_memory()
#         disk_info = psutil.disk_usage('/')

#         system_stats = {
#             'cpu_usage': cpu_usage,
#             'memory_usage': memory_info.percent,
#             'disk_usage': disk_info.percent
#         }

#         # Emit the stats to all connected clients
#         socketio.emit('system_stats', system_stats)
        
#         # Wait for 5 seconds before sending the next update
#         time.sleep(5)

# # Route for serving the web app (you can customize the HTML or use a template)
# @app.route('/')
# def index():
#     return "WebSocket Server is running"

# # Event handler for new WebSocket connections
# @socketio.on('connect')
# def handle_connect():
#     print("A client connected")
#     # Start sending stats in the background when a client connects
#     socketio.start_background_task(target=send_system_stats)

# # Start the Flask app
# if __name__ == '__main__':
#     socketio.run(app, debug=True)


from flask import Flask, request
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

app = Flask(__name__)

# Load private key for RSA decryption
with open("private.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None
    )

@app.route('/')
def home():
    return "Secure Messaging System"

@app.route('/encrypt', methods=['POST'])
def encrypt():
    encrypted_message = request.form['message']
    algorithm = request.form['algorithm']

    if algorithm == "rsa":
        # Decrypt the message using RSA private key
        try:
            encrypted_bytes = bytes.fromhex(encrypted_message)
            decrypted_message = private_key.decrypt(
                encrypted_bytes,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return f"Decrypted message: {decrypted_message.decode()}"
        except Exception as e:
            return f"Error decrypting RSA message: {str(e)}"

    return "Unsupported encryption algorithm!"

if __name__ == "_main_":
    app.run(host="0.0.0.0", port=5000, debug=True)