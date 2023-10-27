import subprocess
import os
import signal
import time
import matplotlib.pyplot as plt

def run_scripts():
    server_process = subprocess.Popen(["python3", "TCPServer.py"], preexec_fn=os.setsid)
    time.sleep(1)
    
    client_process = subprocess.Popen(["python3", "TCPClient.py"], preexec_fn=os.setsid)

    client_process.wait()  # Wait for the client to finish

    # if server_process.poll() is None:  # Check if the process is still running
        # os.killpg(os.getpgid(server_process.pid), signal.SIGTERM)

    plot_times()

def plot_times():
    with open('times.txt', 'r') as f:
        times = [float(line.strip()) for line in f]

    plt.plot(times)
    plt.xlabel('Packet Number')
    plt.ylabel('Round Trip Time (s)')
    plt.title('Round Trip Times per Packet')
    plt.show()

if __name__ == "__main__":
    run_scripts()

