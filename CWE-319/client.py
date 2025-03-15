import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 3000

temperature = "28.5°C"
data = f"TEMP:{temperature}"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((SERVER_IP, SERVER_PORT))
    print(f"Enviando datos: {data}")

    client_socket.sendall(data.encode())

finally:
    client_socket.close()
