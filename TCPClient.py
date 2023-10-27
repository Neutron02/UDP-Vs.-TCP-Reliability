import socket
import time

def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 12345

    client_socket.connect((host, port))

    num_packets = 1000
    times = []

    for i in range(num_packets):
        start_time = time.time()
        client_socket.send(b'Hello, Server!')
        client_socket.recv(1024)
        end_time = time.time()

        times.append(end_time - start_time)

    with open('times.txt', 'w') as f:
        for t in times:
            f.write(f"{t}\n")

    client_socket.close()

if __name__ == "__main__":
    connect_to_server()

