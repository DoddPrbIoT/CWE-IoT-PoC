# Insecure
# import socket

# SERVER_IP = "0.0.0.0"
# SERVER_PORT = 3000  

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind((SERVER_IP, SERVER_PORT))
# server_socket.listen(5)

# print(f"[*] Servidor escuchando en {SERVER_IP}:{SERVER_PORT} (INSEGURO)")

# while True:
#     client_socket, addr = server_socket.accept()
#     print(f"[+] Conexión recibida desde {addr}")

#     data = client_socket.recv(1024).decode()
#     print(f"[+] Datos recibidos: {data}")

#     client_socket.close()

## Secure
import ssl
import socket

SERVER_IP = "0.0.0.0"
SERVER_PORT = 3000 

CERT_FILE = "cert.pem"
KEY_FILE = "key.pem"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(5)

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)

print(f"[*] Servidor seguro escuchando en {SERVER_IP}:{SERVER_PORT}")

while True:
    client_socket, addr = server_socket.accept()
    secure_socket = context.wrap_socket(client_socket, server_side=True)

    print(f"[+] Conexión segura recibida desde {addr}")

    data = secure_socket.recv(1024).decode()
    print(f"[+] Datos recibidos de manera segura: {data}")

    secure_socket.close()
