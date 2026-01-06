# PFAT - Professional Firmware Audit Tool v3.2

**PFAT** is a specialized, interactive command-line security tool designed for security researchers and auditors. It performs rapid static analysis on firmware filesystem extractions to identify critical security risks.

## 🚀 Key Features

- **Interactive File Navigation:** Built-in CUI (Console User Interface) to browse and select firmware directories easily.
- **Customizable Scan Modules:** Selective scanning for Credentials, IPv4 addresses, Private Keys, and Backdoors.
- **Risk Categorization:** Automatically assigns risk levels (CRITICAL, HIGH, LOW) to discovered vulnerabilities.
- **Professional Markdown Reports:** Generates structured, audit-ready .md files after every scan.

## 📊 Proof of Concept (Sample Report)

To see the tool in action, you can view the actual audit performed on the TP-Link firmware image:
👉 **[View Sample Audit Report](pro_audit_Sample.md)**

## 🛠 Installation & Requirements

PFAT is highly portable and runs on any system supporting Python 3.x, including Termux, Debian, Kali Linux, and macOS.

1. **Download:** Copy `Firmware_Audit_Tool.py` to your local environment.
2. **Permissions:** (Optional) Grant execution rights via `chmod +x Firmware_Audit_Tool.py`.
3. **Run:** Execute the tool using `python Firmware_Audit_Tool.py`.

## 💡 Background & Motivation

This tool was born out of necessity. During the analysis of a TP-Link firmware (extracted via `unblob` and `sasquatch`), I realized how time-consuming it is to manually sift through thousands of files. PFAT automates this "grinding" phase, allowing researchers to focus on actual vulnerability verification.

## 🔍 Scan Categories

| Module | Description | Risk Level |
| :--- | :--- | :--- |
| Hardcoded Credentials | Searches for passwords, shadow files, and hardcoded logins. | HIGH |
| Private Keys | Detects RSA, OpenSSH, and EC private keys. | CRITICAL |
| Shell Backdoors | Identifies potential listeners like nc, telnetd, or /bin/sh calls. | CRITICAL |
| IPv4 Addresses | Extracts hardcoded IP addresses for network callback analysis. | LOW |

## ⚖️ Disclaimer

This tool is intended for educational and professional security auditing purposes only. Always obtain explicit permission before analyzing any firmware or software that is not your own.

---
**Developed by:** M-Tarantino  
**Version:** 3.2 (Stable)
