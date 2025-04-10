import json
import os
from utils.cipher import decrypt_password

DATA_FILE = "data/users.json"

def authenticate():
    if not os.path.exists(DATA_FILE):
        print("❗ No users found. Please register first.\n")
        return None

    print("Home 》 Login\n")
    username = input("👤 Name: ").strip()
    password = input("🔑 Password: ").strip()

    with open(DATA_FILE, "r") as file:
        users = json.load(file)

    if username in users:
        stored_encrypted = users[username]["password"]
        if decrypt_password(stored_encrypted) == password:
            print("✅ Login Successful\n")
            return username

    print("❌ Incorrect username or password.\n")
    return None