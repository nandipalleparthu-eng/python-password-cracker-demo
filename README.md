# Educational Password Cracker 

**THIS IS STRICTLY FOR EDUCATIONAL PURPOSES ONLY!**

This project is a demonstration tool created for cybersecurity education and college projects. It simulates password cracking to illustrate security concepts.

**NEVER USE THIS ON REAL ACCOUNTS, EMAILS, OR SYSTEMS WITHOUT EXPLICIT PERMISSION!**

Using this tool on real systems or accounts is illegal under the IT Act and other cybersecurity laws. This can result in serious legal consequences including fines and imprisonment.

## What This Demo Does

This GUI application demonstrates:
- How dictionary attacks work against weak passwords
- Why fast hashes (MD5, SHA-256) are insecure for password storage
- The importance of strong passwords and proper hashing algorithms

### Features
- Graphical user interface built with Tkinter
- Supports MD5 and SHA-256 hash types
- Uses a small wordlist of common weak passwords
- Educational messages about password security best practices
- Threaded execution to keep GUI responsive

## Project Structure

```
password_cracker_demo/
├── src/
│   └── password_cracker_demo/
│       ├── __init__.py
│       └── main.py              # Main GUI application
├── data/
│   └── wordlist.txt             # Common password wordlist
├── run.py                       # Simple runner script
├── README.md                    # This file
├── requirements.txt             # Dependencies (minimal)
├── pyproject.toml               # Package configuration
├── LICENSE                      # MIT License
└── .gitignore                   # Git ignore file
```

## Installation

### Basic Setup
1. Clone or download this repository
2. Ensure Python 3.6+ is installed
3. Install Tkinter if not present:
   - Ubuntu/Debian: `sudo apt-get install python3-tk`
   - macOS: Usually pre-installed
   - Windows: Usually pre-installed with Python

### Optional: Install as Package
For system-wide installation:
```bash
pip install -e .
```
This will install the `password-cracker-demo` command.

## Usage

### Running the Demo

1. Navigate to the project directory
2. Run the application using one of these methods:

   **Option 1: Using the runner script**
   ```bash
   python run.py
   ```

   **Option 2: Direct module execution**
   ```bash
   python -m src.password_cracker_demo.main
   ```

   **Option 3: After installation (see below)**
   ```bash
   password-cracker-demo
   ```

### How to Use

1. **Enter a Dummy Email**: This is just for display purposes (e.g., `test@example.com`)
2. **Enter Your Test Password**: Choose a weak password from the wordlist or any password you want to test
3. **Select Hash Type**: Choose MD5 (fast, insecure) or SHA-256
4. **Click "Start Cracking Demo"**: The tool will simulate a dictionary attack

### What Happens

- The tool computes the hash of your entered password
- It then tries each password in the wordlist against that hash
- If found, it displays the "cracked" password and time taken
- Educational messages explain why this is dangerous in real scenarios

## Educational Takeaways

### Why Passwords Get Cracked
- **Weak passwords**: Common words, short lengths, predictable patterns
- **Fast hashes**: MD5 and SHA-256 are designed for speed, not security
- **No salting**: Real systems add random salts to prevent rainbow table attacks
- **Dictionary attacks**: Automated guessing using common password lists

### How to Stay Secure
- Use **14+ character passphrases** instead of passwords
- Enable **Two-Factor Authentication (2FA)** wherever possible
- Use **password managers** to generate and store unique passwords
- Choose systems that use **slow, salted hashing** like:
  - bcrypt
  - Argon2
  - PBKDF2 with high iteration counts

## Technical Details

- **Language**: Python 3
- **GUI Framework**: Tkinter (standard library)
- **Hashing**: hashlib (MD5, SHA-256)
- **Threading**: For non-blocking GUI updates
- **Wordlist**: ~35 common weak passwords (expandable)

## Customization

### Adding More Passwords
Edit `data/wordlist.txt` to add more common passwords for testing.

### Modifying the GUI
The code is well-commented. Modify `src/password_cracker.py` to:
- Change colors/themes
- Add more hash types
- Implement brute-force attacks
- Add progress bars

## Legal and Ethical Notice

This tool is provided as-is for educational purposes. The author is not responsible for misuse. Always follow ethical guidelines and legal requirements when studying cybersecurity.

## License

MIT License - See LICENSE file for details.

## Contributing

This is an educational project. Feel free to submit improvements, but remember the ethical guidelines.
