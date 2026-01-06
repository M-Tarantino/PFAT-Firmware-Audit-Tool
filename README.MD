# PFAT - Professional Firmware Audit Tool v3.2

**PFAT** is a specialized, interactive command-line security tool designed for security researchers and auditors. It performs rapid static analysis on firmware filesystem extractions to identify critical security risks.

## 🚀 Key Features

- **Interactive File Navigation:** Built-in CUI (Console User Interface) to browse and select firmware directories easily.
- **Customizable Scan Modules:** Selective scanning for Credentials, IPv4 addresses, Private Keys, and Backdoors.
- **Risk Categorization:** Automatically assigns risk levels (CRITICAL, HIGH, LOW) to discovered vulnerabilities.
- **Dynamic System Integration:** Automatically identifies the system auditor (via Linux user account) for professional reporting.
- **Professional Markdown Reports:** Generates structured, audit-ready .md files after every scan.

## 🛠 Installation & Requirements

PFAT is highly portable and runs on any system supporting Python 3.x, including Termux, Debian, Kali Linux, and macOS.

1. Clone/Download: Copy 'Firmware_Audit_Tool.py' to your local environment.
2. Permissions: (Optional) Grant execution rights via 'chmod +x Firmware_Audit_Tool.py'.
3. Run: Execute the tool using 'python Firmware_Audit_Tool.py'.

## 💻 Usage & Navigation

Upon launching, PFAT provides an intuitive menu:
- [0] START SCAN HERE: Begins analysis in the currently displayed folder.
- [1] .. (Back): Navigates to the parent directory.
- [ID Number]: Enters a specific subdirectory.
- [q] EXIT: Safely terminates the program.

## 🔍 Scan Categories

| Module | Description | Risk Level |
| :--- | :--- | :--- |
| Hardcoded Credentials | Searches for passwords, shadow files, and hardcoded logins. | HIGH |
| Private Keys | Detects RSA, OpenSSH, and EC private keys left in the filesystem. | CRITICAL |
| Shell Backdoors | Identifies potential listeners like nc, telnetd, or reverse shells. | CRITICAL |
| IPv4 Addresses | Extracts hardcoded IP addresses for network callback analysis. | LOW |

## 📊 Reporting

All findings are saved in the project root directory as a Markdown report (pro_audit_TIMESTAMP.md). These reports include:
- An Executive Summary for quick risk assessment.
- System Information regarding the auditor and software version.
- Detailed Evidence with full file paths and code snippets for verification.

## ⚖️ Disclaimer

This tool is intended for educational and professional security auditing purposes only. Always obtain explicit permission before analyzing any firmware or software that is not your own.

---
**Developed by:** M-Tarantino  
**Version:** 3.2 (Stable)