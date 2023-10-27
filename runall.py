import subprocess
import os
import signal
import time
import matplotlib.pyplot as plt

def run_scripts():
    # Start TCP Server and Client
    tcp_server_process = subprocess.Popen(["python3", "TCPServer.py"], preexec_fn=os.setsid)
    time.sleep(1)  
    tcp_client_process = subprocess.Popen(["python3", "TCPClient.py"], preexec_fn=os.setsid)
    tcp_client_process.wait()

    # Start UDP Server and Client
    udp_server_process = subprocess.Popen(["python3", "UDPServer.py"], preexec_fn=os.setsid)
    time.sleep(1)
    udp_client_process = subprocess.Popen(["python3", "UDPClient.py"], preexec_fn=os.setsid)
    udp_client_process.wait()

    plot_times()

def plot_times():
    # TCP times
    with open('times.txt', 'r') as f:
        tcp_times = [float(line.strip()) for line in f]

    # UDP times
    with open('udp_times.txt', 'r') as f:
        udp_times = [float(line.strip()) for line in f]

    plt.plot(tcp_times, label='TCP')
    plt.plot(udp_times, label='UDP')
    plt.xlabel('Packet Number')
    plt.ylabel('Round Trip Time (s)')
    plt.title('Round Trip Times per Packet (TCP vs. UDP)')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    run_scripts()
