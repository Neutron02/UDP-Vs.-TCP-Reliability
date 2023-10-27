import socket
import time

def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = 'localhost'
    port = 12346

    num_packets = 1000
    times = []

    for i in range(num_packets):
        start_time = time.time()
        client_socket.sendto(b'Hello, Server!', (host, port))
        client_socket.recvfrom(1024)
        end_time = time.time()

        times.append(end_time - start_time)

    with open('udp_times.txt', 'w') as f:
        for t in times:
            f.write(f"{t}\n")

    client_socket.close()

if __name__ == "__main__":
    connect_to_server()

