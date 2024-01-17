import time
from socket import *
import threading


def synchronize_client(connectionSocket: socket):
    try:
        while True:
            # Receive and timestamp the NTP request from the client
            connectionSocket.recv(1024)
            T2 = time.time_ns() // 1000000

            # Timestamp when response is sent to client
            T3 = time.time_ns() // 1000000
            connectionSocket.send(f"{T2} {T3}".encode())  # Send T2, T3 to the client
    except:
        connectionSocket.close()  # Close this connection socket


def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)  # Create server's welcome socket
    # Bind welcome socket to 0.0.0.0 at port 10000 + student ID
    serverSocket.bind(("0.0.0.0", 13202))
    serverSocket.listen(1)  # Listen for incoming connection requests
    print("Server listening on port 13202")
    try:
        while True:
            # Accept any incoming connection requests
            connectionSocket, clientAddress = serverSocket.accept()

            # Create a new thread to handle the NTP protocol and keep the main
            # thread free to listen for new connection requests.
            thread = threading.Thread(
                target=synchronize_client,
                args=[connectionSocket],
                daemon=True,
            )
            thread.start()
            print(f"Active Threads: {threading.active_count() - 1}")
    except:
        serverSocket.close()  # Close the server's welcome socket


if __name__ == "__main__":
    main()
