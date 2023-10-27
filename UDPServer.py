import socket
import time
def check_port_available(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) != 0

while not check_port_available(12346):
    time.sleep(1)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    host = 'localhost'
    port = 12346
    server_socket.bind((host, port))

    print(f"UDP Server started on {host}:{port}. Waiting for packets...")

    try:
        while True:
            data, addr = server_socket.recvfrom(1024)
            if not data:
                break
            server_socket.sendto(b'ACK', addr)
    except KeyboardInterrupt:
        pass

    server_socket.close()

if __name__ == "__main__":
    start_server()

