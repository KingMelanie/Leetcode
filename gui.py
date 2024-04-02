import hashlib
import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox

# Function to generate random number, message digest, session key, and encrypt hash
def generate_and_encrypt():
    # Generate a random number
    random_number = os.urandom(16)  # 16 bytes for a 128-bit random number

    # Generate a message digest using SHA-256 hashing algorithm
    hash_object = hashlib.sha256()
    hash_object.update(random_number)
    message_digest = hash_object.digest()

    # Generate a session key
    session_key = Fernet.generate_key()

    # Encrypt the new hash using the session key
    cipher_suite = Fernet(session_key)
    encrypted_hash = cipher_suite.encrypt(message_digest)

    # Show the results in a message box
    messagebox.showinfo("Results", 
                        f"Random Number: {random_number.hex()}\n"
                        f"Message Digest: {message_digest.hex()}\n"
                        f"Session Key: {session_key.hex()}\n"
                        f"Encrypted Hash: {encrypted_hash.hex()}")

# Create the main window
root = tk.Tk()
root.title("Message Digest Hashing & Encryption")

# Create a label
label = tk.Label(root, text="Click the button to generate a random number, message digest, session key, and encrypted hash.")
label.pack(pady=10)

# Create a button
button = tk.Button(root, text="Generate and Encrypt", command=generate_and_encrypt)
button.pack()

# Start the GUI event loop
root.mainloop()
