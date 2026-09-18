# 🔐 Password Security Analyzer

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-%23E34F26.svg?style=for-the-badge&logo=shield&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

---

## 📌 Project Overview

**Password Security Analyzer** is a Python-based cybersecurity project designed to evaluate the security strength of user-provided passwords.

The program:
- Analyzes different characteristics of a password
- Detects common and predictable patterns
- Calculates estimated password entropy
- Provides personalized security recommendations
- Generates a cryptographically secure random password

This project was developed to understand basic password security concepts and Python programming techniques used in cybersecurity.

---

## 🎯 Objectives

- ✅ Analyze overall password strength
- ✅ Check password length and character composition
- ✅ Detect commonly used passwords
- ✅ Detect repeated character patterns
- ✅ Detect sequential patterns
- ✅ Calculate estimated password entropy
- ✅ Provide actionable security recommendations
- ✅ Generate a secure random password

---

## ⚙️ Features

### 1. 🏆 Password Strength Score
Evaluates the password using five security criteria:
- Minimum length of 12 characters
- Uppercase letter present
- Lowercase letter present
- Number present
- Special character present

**Score: 0/5 to 5/5**

---

### 2. 🔍 Character Detection
Checks whether the password contains:
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

```
Contains uppercase      : True
Contains lowercase      : True
Contains number         : True
Contains special char   : True
```

---

### 3. ⚠️ Common Password Detection
Checks against a list of commonly used passwords:
- password, password123, 123456
- qwerty, admin, welcome, letmein

If matched → displays an instant warning!

---

### 4. 🔁 Repeated Character Detection
Detects if same character appears 3+ times.

Example: `AAAAAAAAAAAA` → Warning displayed!

---

### 5. 📈 Sequential Pattern Detection
Detects predictable sequences like:
- `1234`, `2345`, `abcd`, `qwer`

If detected → Warning displayed!

---

### 6. 🧮 Character Pool Calculation
Calculates possible character pool size:

| Character Type | Pool Size |
|----------------|-----------|
| Lowercase letters | 26 |
| Uppercase letters | 26 |
| Numbers | 10 |
| Special characters | 32 |
| **All combined** | **94** |

---

### 7. 📊 Password Entropy Calculation
Estimates entropy using:

```
Entropy = Password Length × log2(Character Pool Size)
```

| Entropy Level | Classification |
|--------------|----------------|
| Low | Weak |
| Medium | Moderate |
| High | Strong |
| Very High | Very Strong |

> Note: This is an educational entropy estimate.

---

### 8. 💡 Security Recommendations
Provides personalized recommendations based on analysis:

```
Recommendations:
- Use at least 12 characters
- Add at least one uppercase letter
- Add at least one number
- Add a special character
```

Only relevant recommendations are shown!

---

### 9. 🔑 Secure Password Generator
Generates a cryptographically secure random password using Python's `secrets` module.

Generated password includes:
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

At least one character from each category is guaranteed!

```
Generated Secure Password: xK#9mP$2nL@qR
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| Python 3 | Core programming language |
| math module | Entropy calculation |
| secrets module | Secure password generation |
| string module | Character set handling |

---

## 📂 Project Structure

```
Password-Security-Analyzer/
│
├── password_analyzer.py   → Main program file
└── README.md              → Project documentation
```

---

## ▶️ How to Run

**1. Clone the repository**
```bash
git clone https://github.com/shelkeonkar782-lab/password-analyzer-python.git
```

**2. Open the project folder**
```bash
cd password-analyzer-python
```

**3. Run the Python program**
```bash
python password_analyzer.py
```

**4. Enter a password when prompted**

The analyzer will display:
- Full password analysis
- Security recommendations
- Entropy estimate
- Generated secure password

---

## 🧪 Example Analysis

**Input:** `HelloWorld123!`

```
===== PASSWORD SECURITY ANALYZER =====

Password Length         : 14 characters
Contains uppercase      : True
Contains lowercase      : True
Contains number         : True
Contains special char   : True

Common Password         : No ✅
Repeated Characters     : No ✅
Sequential Pattern      : No ✅

Character Pool Size     : 94
Password Entropy        : 91.83 bits → Very Strong

Strength Score          : 5/5 ⭐⭐⭐⭐⭐

Recommendations         : None — Great password!

Generated Secure Password: xK#9mP$2nL@qR
```

---

## 🔐 Cybersecurity Concepts Demonstrated

- Password security fundamentals
- Password complexity requirements
- Brute-force resistance concepts
- Password entropy theory
- Predictable pattern detection
- Common password attack awareness
- Secure random password generation
- Basic security recommendations

---

## 📚 Learning Outcomes

Through this project, I practiced:
- Python programming fundamentals
- Conditional statements and loops
- Sets, lists and string manipulation
- Functions and built-in methods
- Mathematical calculations
- Secure random value generation
- Basic cybersecurity concepts
- Git and GitHub project management

---

## 👨‍💻 Author

**Onkar Shelke**

![Python](https://img.shields.io/badge/Python-Learning-blue?style=flat-square)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Interested-red?style=flat-square)

- 🎓 BBA(CA) Graduate — Savitribai Phule Pune University, Pune
- 💻 Currently learning Python & Web Development
- 🔐 Interested in Cybersecurity
- 🌐 [LinkedIn](https://linkedin.com/in/onkar-shelke1)
- 💻 [GitHub](https://github.com/shelkeonkar782-lab)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">⭐ If you found this helpful, give it a star! ⭐</p>
