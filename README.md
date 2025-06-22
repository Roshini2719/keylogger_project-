# keylogger_project
# 🔐 Encrypted Keylogger PoC (Ethical Use Only)

This project is a **Proof-of-Concept (PoC) Encrypted Keylogger** designed exclusively for **educational and authorized security testing**. It captures keystrokes, encrypts them securely using AES (Fernet), stores logs locally, simulates data exfiltration over localhost, and generates human-readable reports in HTML.

---

## ⚠️ Ethical Disclaimer

> 🚨 This project must **only be used on systems you own or have explicit authorization to test**.  
> Unauthorized use may violate ethical and legal boundaries and is strictly prohibited.

---

## 🛠️ Tools Used

- **Python 3**
- `pynput` — Keystroke logging
- `cryptography` — AES encryption via Fernet
- `base64` — Encodes data before encryption
- `socket` — TCP connection for local exfil
- `Flask` (optional) — HTTP-based localhost receiver
- `xdg-open` — Opens report in browser

---

## 📁 Project Structure
keylogger_project/
├── keylogger.py            # Main keylogger script
├── server.py               # Simulated localhost TCP server
├── config.py               # Key generator script (Fernet key)
├── decrypt_log.py          # Text-based decryption
├── decrypt_to_html.py      # Decrypts and builds HTML report
├── keylog_encrypted.log    # [Ignored] Encrypted keystrokes
├── keylog_decrypted.txt    # [Ignored] Decrypted logs
├── keylog_report.html      # [Ignored] Browser report output
├── secret.key              # ❗ Do NOT upload this key
└── README.md
 Getting Started
Step 1: Environment Setup
bash
Copy code
sudo apt update
sudo apt install python3-pip
pip3 install pynput cryptography flask
Step 2: Initialize Encryption Key
bash
Copy code
python3 config.py
This creates a secret.key used for all encryption/decryption.

🎹 Running the Keylogger
1️⃣ Start the Exfiltration Server (in new terminal)
Copy code
python3 server.py
2️⃣ Run the Keylogger

Copy code
python3 keylogger.py
Type random characters

Press ESC to stop

3️⃣ View Encrypted Logs

Copy code
cat keylog_encrypted.log
🔓 Decrypting Logs
Option A: View Decrypted Text

Copy code
python3 decrypt_log.py
cat keylog_decrypted.txt
Option B: Generate HTML Report
Copy code
python3 decrypt_to_html.py
xdg-open keylog_report.html
