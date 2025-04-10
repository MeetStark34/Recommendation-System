import json
import os
from utils.cipher import encrypt_password

# Navigate one level up from 'auth' to the 'movie_matcher' directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_FILE = os.path.join(DATA_DIR, "users.json")

def create_account():
    os.makedirs(DATA_DIR, exist_ok=True)

    print("Home 》 Register\n")
    username = input("👤 Choose a username: ").strip()
    password = input("🔑 Choose a password: ").strip()

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            users = json.load(file)
    else:
        users = {}

    if username in users:
        print("⚠️ Username already exists. Try logging in.\n")
        return

    users[username] = {"password": encrypt_password(password)}

    with open(DATA_FILE, "w") as file:
        json.dump(users, file, indent=2)

    print("✅ Account created successfully!\n")
