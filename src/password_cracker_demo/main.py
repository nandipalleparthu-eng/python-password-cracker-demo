"""
EDUCATIONAL PASSWORD CRACKER GUI DEMO – COLLEGE PROJECT ONLY
============================================================
THIS IS STRICTLY FOR DEMONSTRATION PURPOSES ON YOUR OWN TEST ACCOUNT!
YOU CREATED YOURSELF.

NEVER use on real accounts, real emails, or without permission.
Illegal under IT Act and other laws – serious consequences.

Only for cybersecurity project viva/presentation.
============================================================
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import hashlib
import time
from threading import Thread
import os

# Load wordlist from file
def load_wordlist(filepath):
    try:
        with open(filepath, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Warning: Wordlist file {filepath} not found. Using built-in list.")
        return [
            "123456", "password", "12345678", "qwerty", "abc123", "111111",
            "12345", "iloveyou", "123123", "password1", "welcome", "admin",
            "letmein", "parthu", "parthu123", "parthu2025", "madurai", "madurai123",
            "regina", "regina2025", "demo", "test123", "hello123", "password123",
            "123456789", "sunshine", "princess", "flower", "monkey", "jesus",
            "superman", "batman", "love", "hate", "god123", "india", "tamil"
        ]

class PasswordCrackerGUI:
    def __init__(self, root, wordlist):
        self.root = root
        self.root.title("Educational Password Cracker Demo")
        self.root.geometry("680x580")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        # Style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#1e1e2e", foreground="#cdd6f4")
        style.configure("Header.TLabel", font=("Arial", 14, "bold"), foreground="#f38ba8")
        style.configure("Warning.TLabel", font=("Arial", 10, "bold"), foreground="#f38ba8")
        style.configure("TButton", font=("Arial", 10), padding=6)
        style.map("TButton", background=[("active", "#45475a")])

        # Header + Warning
        ttk.Label(root, text="EDUCATIONAL DEMO ONLY", style="Header.TLabel").pack(pady=10)
        warning = ttk.Label(root, text="ONLY FOR YOUR OWN DUMMY ACCOUNT\n"
                                       "Never use on real accounts – ILLEGAL otherwise!",
                             style="Warning.TLabel", justify="center")
        warning.pack(pady=5)

        frame = ttk.Frame(root, padding=15)
        frame.pack(fill="both", expand=True)

        # Dummy Email
        ttk.Label(frame, text="Dummy Gmail (for display):").grid(row=0, column=0, sticky="w", pady=5)
        self.email_entry = ttk.Entry(frame, width=40)
        self.email_entry.insert(0, "regina.demo.2025@gmail.com")
        self.email_entry.grid(row=0, column=1, pady=5, sticky="w")

        # Test Password (shown – for education)
        ttk.Label(frame, text="Your Test Password:").grid(row=1, column=0, sticky="w", pady=5)
        self.pwd_entry = ttk.Entry(frame, width=40, show="*")
        self.pwd_entry.grid(row=1, column=1, pady=5, sticky="w")

        # Hash Type
        ttk.Label(frame, text="Hash Type:").grid(row=2, column=0, sticky="w", pady=5)
        self.hash_var = tk.StringVar(value="md5")
        ttk.Radiobutton(frame, text="MD5 (fast, insecure)", variable=self.hash_var, value="md5").grid(row=2, column=1, sticky="w")
        ttk.Radiobutton(frame, text="SHA-256", variable=self.hash_var, value="sha256").grid(row=3, column=1, sticky="w")

        # Start Button
        self.start_btn = ttk.Button(frame, text="Start Cracking Demo", command=self.start_crack_thread)
        self.start_btn.grid(row=4, column=0, columnspan=2, pady=15)

        # Result Area
        self.result_text = scrolledtext.ScrolledText(frame, width=75, height=12, font=("Consolas", 10), bg="#2e2e3e", fg="#cdd6f4")
        self.result_text.grid(row=5, column=0, columnspan=2, pady=10)
        self.result_text.insert(tk.END, "Results will appear here...\n")
        self.result_text.config(state="disabled")

        # Educational note
        note = ttk.Label(root, text="Takeaway: Weak passwords + fast hashes = easy to crack\n"
                                    "Use 14+ char passphrases + bcrypt/Argon2 + 2FA",
                         font=("Arial", 9, "italic"), foreground="#94e2d5", background="#1e1e2e")
        note.pack(pady=10)

        self.running = False
        self.wordlist = wordlist

    def compute_hash(self, password, hash_type):
        password = password.encode('utf-8')
        if hash_type == "md5":
            return hashlib.md5(password).hexdigest()
        elif hash_type == "sha256":
            return hashlib.sha256(password).hexdigest()
        return ""

    def crack_in_thread(self):
        self.running = True
        self.start_btn.config(state="disabled")
        self.result_text.config(state="normal")
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, "Starting demo attack...\n\n")
        self.result_text.config(state="disabled")

        email = self.email_entry.get().strip() or "dummy@gmail.com"
        password = self.pwd_entry.get().strip()

        if not password:
            self.show_result("Error: Enter a test password first!")
            self.finish()
            return

        hash_type = self.hash_var.get()
        target_hash = self.compute_hash(password, hash_type)

        self.show_result(f"Target email (display only): {email}")
        self.show_result(f"Entered password: {'*' * len(password)}")
        self.show_result(f"Computed {hash_type.upper()} hash: {target_hash}\n")

        wordlist = self.wordlist[:]
        if password not in wordlist:
            wordlist.append(password)  # so demo always succeeds quickly

        start_time = time.time()
        found = False

        self.show_result("Dictionary attack started...\n")

        for pwd in wordlist:
            if self.compute_hash(pwd, hash_type) == target_hash:
                duration = time.time() - start_time
                self.show_result("★" * 40)
                self.show_result(f" PASSWORD CRACKED!")
                self.show_result(f" Cracked password: {pwd}")
                self.show_result(f" Time taken: {duration:.2f} seconds")
                self.show_result("★" * 40)
                found = True
                break

            # Small delay to simulate work & allow GUI update
            time.sleep(0.005)

        if not found:
            self.show_result("Not found in this small list (unlikely – check input).")

        self.show_result("\nEducational message:")
        self.show_result("• MD5/SHA-256 are NOT safe for passwords")
        self.show_result("• Use slow salted hashes: bcrypt, Argon2, PBKDF2")
        self.show_result("• Password length ≥14 + 2FA is strongly recommended")
        self.show_result("• Never reuse passwords – use a password manager")

        self.finish()

    def start_crack_thread(self):
        if self.running:
            return
        Thread(target=self.crack_in_thread, daemon=True).start()

    def show_result(self, text):
        self.result_text.config(state="normal")
        self.result_text.insert(tk.END, text + "\n")
        self.result_text.see(tk.END)
        self.result_text.config(state="disabled")
        self.root.update_idletasks()

    def finish(self):
        self.running = False
        self.start_btn.config(state="normal")

def main():
    """Entry point for the password cracker demo."""
    # Get the path to the data directory
    data_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
    wordlist_path = os.path.join(data_dir, 'wordlist.txt')
    wordlist = load_wordlist(wordlist_path)
    root = tk.Tk()
    app = PasswordCrackerGUI(root, wordlist)
    root.mainloop()

if __name__ == "__main__":
    main()