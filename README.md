# 🛡️ demo-cbom-python-app

This project demonstrates weak vs strong cryptographic practices.

## Branches
- `main`: insecure version (MD5, DES)
- `secure`: secure version (SHA-256, AES-GCM)

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

## Project Overview
This project is a simple demonstration of cryptographic practices. It accepts a username and password as input from the user and generates encrypted content based on the provided data.
