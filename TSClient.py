import sys
import time
from socket import *


def main(hostname="localhost"):
    clientSocket = socket(AF_INET, SOCK_STREAM)  # Create client's socket
    clientSocket.connect((hostname, 13202))  # Send a connection request to server

    T1 = time.time_ns() // 1000000  # Timestamp when NTP request is sent
    clientSocket.send(f"{T1}".encode())  # Send the message to server

    # Receive timestamps T2, T3 from server
    T2, T3 = map(lambda x: int(x), clientSocket.recv(1024).decode().split())

    # Timestamp when response from server is received
    T4 = time.time_ns() // 1000000

    # Calculate RTT and offset
    RTT = (T4 - T1) - (T3 - T2)
    offset = ((T2 - T1) + (T3 - T4)) // 2

    # Print time values
    print(f"REMOTE_TIME {T4 + offset}")
    print(f"LOCAL_TIME {T4}")
    print(f"RTT_ESTIMATE {RTT}")
    clientSocket.close()  # Close client's socket


if __name__ == "__main__":
    main(sys.argv[1]) if len(sys.argv) > 1 else main()
