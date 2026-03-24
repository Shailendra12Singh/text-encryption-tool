# Text Encryption & Cryptanalysis Tool

## Overview
This project is a modular Python-based cryptographic tool that implements the **Caesar Cipher** algorithm for encryption and decryption of text messages.

In addition to encryption, the tool also demonstrates classical cryptanalysis techniques such as brute-force attacks and frequency analysis to highlight the vulnerabilities of substitution ciphers.

---

## Features

- Text Encryption using Caesar Cipher
- Text Decryption
- Brute Force Attack Simulation (tries all 25 possible shifts)
- Frequency Analysis for probable key detection
- Modular Code Structure (Separation of Concerns)

---

## Technologies Used

- Python 3
- String Manipulation
- ASCII Encoding
- Modular Arithmetic
- Collections (Counter module)

---

## Project Structure

```
text-encryption-tool/
│
├── main.py          # User Interface & Controller
├── cipher.py        # Core Encryption/Decryption Logic
├── attack.py        # Brute Force Attack Module
├── analysis.py      # Frequency Analysis Module
├── README.md
└── requirements.txt
```

---

## How to Run

1. Clone the repository:

```
git clone https://github.com/your-username/text-encryption-tool.git
```

2. Navigate to the project directory:

```
cd text-encryption-tool
```

3. Run the program:

```
python main.py
```

---

## Concepts Demonstrated

- Classical Cryptography
- Substitution Cipher
- Modular Arithmetic in Encryption
- Brute-Force Cryptanalysis
- Frequency Analysis Attack

---

## Security Note

The Caesar Cipher is a classical encryption technique and is **not secure for modern communication**.  
This project is intended for educational purposes to understand foundational cryptographic concepts.

---

## Author

Shailendra Singh Dhakad
B.Tech CSE | Cybersecurity Student
