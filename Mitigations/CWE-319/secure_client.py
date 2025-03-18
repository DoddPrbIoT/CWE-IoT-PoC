import ssl
import socket

SERVER_IP = "127.0.0.1"  
SERVER_PORT = 3000          


context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE  


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


secure_socket = context.wrap_socket(client_socket, server_hostname=SERVER_IP)

try:
    secure_socket.connect((SERVER_IP, SERVER_PORT))
    print(f"🔒 Conectado de manera segura a {SERVER_IP}:{SERVER_PORT}")

    # Enviar datos
    temperature = "25.5°C"
    data = f"TEMP:{temperature}"
    secure_socket.sendall(data.encode())

    response = secure_socket.recv(1024).decode()
    print(f"📩 Respuesta del servidor: {response}")

finally:
    secure_socket.close()

