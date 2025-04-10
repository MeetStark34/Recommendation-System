import json
import os
from utils.cipher import encrypt_password

DATA_FILE = "data/users.json"

def reset_user_password():
    if not os.path.exists(DATA_FILE):
        print("❗ No users found. Please register first.\n")
        return

    print("Home 》 Reset Password\n")
    username = input("👤 Enter your username: ").strip()

    with open(DATA_FILE, "r") as file:
        users = json.load(file)

    if username not in users:
        print("❌ Username not found.\n")
        return

    new_password = input("🔐 Enter new password: ").strip()
    confirm_password = input("🔁 Confirm new password: ").strip()

    if new_password != confirm_password:
        print("⚠️ Passwords do not match. Try again.\n")
        return

    users[username]["password"] = encrypt_password(new_password)

    with open(DATA_FILE, "w") as file:
        json.dump(users, file, indent=2)

    print("✅ Password updated successfully!\n")
