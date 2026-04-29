# Password Strength Analyzer 🔐

Password Strength Analyzer is a simple web application that checks how strong a password is and helps users create safer passwords.

This project is built using Python and Flask. It also uses SQLite to store old passwords securely and bcrypt to hash passwords, so plain text passwords are never saved.

---

## 🚀 Features

- Live password strength meter (changes while typing)
- Checks length, uppercase, lowercase, numbers, and symbols
- Calculates password entropy
- Suggests stronger passwords
- Copy suggested password button
- Show / Hide password option
- Dark / Light theme switch
- Prevents reuse of old passwords
- Secure password storage using hashing

---

## 🛠 Technologies Used

- Python
- Flask
- SQLite
- bcrypt
- HTML, CSS, JavaScript

---

## 📁 Project Structure
password_strength_analyzer/
│
├── app.py
├── analyzer.py
├── generator.py
├── database.py
├── templates/
│ └── index.html
├── weak_passwords.txt
└── requirements.txt


---

## ▶️ How to Run the Project

### 1. Clone the repository

bash
git clone https://github.com/your-username/password-strength-analyzer.git
cd password-strength-analyzer

Install requirements

pip install -r requirements.txt

Run the application
python app.py

4. Open in browser
http://127.0.0.1:5000



Learning Purpose

This project helps to understand:

Password security rules
Password entropy and complexity
Hashing using bcrypt
Preventing password reuse
Building a security tool with web interface
