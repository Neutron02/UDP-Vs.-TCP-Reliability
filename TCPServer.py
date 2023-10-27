import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 12345
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server started on {host}:{port}. Waiting for clients...")

    client_socket, addr = server_socket.accept()
    print(f"Got a connection from {addr}")

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            client_socket.send(b'ACK')  # Send acknowledgment
    except:
        pass

    client_socket.close()

if __name__ == "__main__":
    start_server()

