# Insecure
import socket

SERVER_IP = "0.0.0.0"
SERVER_PORT = 3000  

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(5)

print(f"[*] Servidor escuchando en {SERVER_IP}:{SERVER_PORT} (INSEGURO)")

while True:
    client_socket, addr = server_socket.accept()
    print(f"[+] Conexión recibida desde {addr}")

    data = client_socket.recv(1024).decode()
    print(f"[+] Datos recibidos: {data}")

    client_socket.close()

