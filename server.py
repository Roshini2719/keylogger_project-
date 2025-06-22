# server.py
import socket

HOST = "127.0.0.1"
PORT = 9001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[+] Server listening on {HOST}:{PORT}...")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"[+] Connection from {addr}")
            data = conn.recv(1024)
            print(f"[>] Received (Encrypted): {data}")
