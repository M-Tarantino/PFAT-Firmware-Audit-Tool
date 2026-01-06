import os
import re
import sys
import getpass
from datetime import datetime

class FirmwareScanner:
    def __init__(self, author_name="M-Tarantino"):
        self.author = author_name
        self.system_user = getpass.getuser()
        
        self.C_BLUE = "\033[38;5;75m"
        self.C_GREEN = "\033[38;5;112m"
        self.C_YELLOW = "\033[38;5;220m"
        self.C_RED = "\033[38;5;196m"
        self.C_PURPLE = "\033[38;5;176m"
        self.C_BOLD = "\033[1m"
        self.C_END = "\033[0m"

        self.all_signatures = {
            "Hardcoded_Credentials": {
                "pattern": r'(?i)(password|passwd|pwd|admin123|shadow|root_password)\s*[:=]\s*["\']?([a-zA-Z0-9!@#$%^&*()_+]{3,})["\']?',
                "risk": "HIGH"
            },
            "IPv4_Addresses": {
                "pattern": r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b',
                "risk": "LOW"
            },
            "Private_Keys": {
                "pattern": r'-----BEGIN (?:RSA|OPENSSH|EC|PRIVATE) KEY-----',
                "risk": "CRITICAL"
            },
            "Shell_Backdoors": {
                "pattern": r'(nc -e|/bin/sh|/bin/bash|reverse_shell|telnetd)',
                "risk": "CRITICAL"
            }
        }
        self.selected_cats = []
        self.findings = {}

    def print_banner(self):
        os.system('clear')
      
        banner = r"""
    ____________ ___ _____ 
    | ___ \  ___/ _ \_   _|
    | |_/ / |_ / /_\ \| |  
    |  __/|  _||  _  || |  
    | |   | |  | | | || |  
    \_|   \_|  \_| |_/\_/
    """
        print(f"{self.C_BLUE}{self.C_BOLD}{banner}{self.C_END}")
        print(f"    {self.C_YELLOW}>> Professional Firmware Audit Tool v3.2{self.C_END}")
        print(f"    {self.C_PURPLE}{self.C_BOLD}Developed by: {self.author}{self.C_END}\n")

    def select_categories(self):
        self.print_banner()
        print(f"{self.C_BOLD}Select categories (comma separated | 'all' | 'q' to abort):{self.C_END}")
        cats = list(self.all_signatures.keys())
        for i, cat in enumerate(cats, 1):
            print(f" [{i}] {cat.replace('_', ' ')}")
        
        choice = input(f"\n{self.C_BOLD}Selection:{self.C_END} ").strip().lower()
        if choice == 'q': return False
        
        if choice == 'all' or choice == '':
            self.selected_cats = cats
        else:
            try:
                indices = [int(x.strip()) - 1 for x in choice.split(',')]
                self.selected_cats = [cats[i] for i in indices if 0 <= i < len(cats)]
            except:
                self.selected_cats = cats
        
        self.findings = {key: [] for key in self.selected_cats}
        return True

    def navigate(self, current_path):
        while True:
            self.print_banner()
            print(f"{self.C_PURPLE}LOCATION:{self.C_END} {current_path}\n")
            try:
                items = sorted([d for d in os.listdir(current_path) if os.path.isdir(os.path.join(current_path, d))])
            except PermissionError:
                print(f"{self.C_RED}[!] Permission Denied{self.C_END}"); return None

            print(f" {self.C_GREEN}[0]{self.C_END} -> START SCAN HERE")
            print(f" {self.C_YELLOW}[1]{self.C_END} -> .. (Back)")
            print(f" {self.C_RED}[q]{self.C_END} -> EXIT PROGRAM")
            print("-" * 40)
            for i, folder in enumerate(items, 2):
                print(f" [{i}] -> {folder}/")

            choice = input(f"\n{self.C_BOLD}Select ID or 'q':{self.C_END} ").strip().lower()
            if choice == 'q': sys.exit()
            elif choice == '0': return current_path
            elif choice == '1': current_path = os.path.dirname(current_path)
            else:
                try:
                    idx = int(choice) - 2
                    if 0 <= idx < len(items): current_path = os.path.join(current_path, items[idx])
                except: continue

    def run_scan(self, target_path):
        if not self.select_categories(): return
        all_files = []
        for root, _, files in os.walk(target_path):
            for f in files: all_files.append(os.path.join(root, f))
        
        total = len(all_files)
        if total == 0: return

        print(f"\n{self.C_YELLOW}[*] Scanning {total} files...{self.C_END}\n")

        for i, file_path in enumerate(all_files, 1):
            try:
                with open(file_path, 'r', errors='ignore') as f:
                    content = f.read()
                    for cat in self.selected_cats:
                        pattern = self.all_signatures[cat]['pattern']
                        for m in re.finditer(pattern, content):
                            self.findings[cat].append({"file": file_path, "match": m.group(0)})
            except: pass
            
            # Progress bar update
            if i % 5 == 0 or i == total:
                percent = "{0:.1f}".format(100 * (i / float(total)))
                bar = '█' * int(40 * i // total) + '░' * (40 - int(40 * i // total))
                sys.stdout.write(f'\r{self.C_BLUE} PROGRESS:{self.C_END} |{bar}| {percent}%')
                sys.stdout.flush()
        
        report = self.generate_report(target_path)
        print(f"\n\n{self.C_GREEN}[✔] SCAN COMPLETE! Report: {report}{self.C_END}")
        input("\nPress Enter to return...")

    def generate_report(self, target):
        ts = datetime.now().strftime('%Y%m%d_%H%M%S')
        name = f"pro_audit_{ts}.md"
        with open(name, 'w') as f:
            f.write(f"# Professional Firmware Audit Report\n\n")
            f.write(f"## 📊 Executive Summary\n")
            f.write(f"- **Target Folder:** `{target}`\n")
            f.write(f"- **Auditor:** `{self.system_user}`\n")
            f.write(f"- **Developer:** {self.author}\n\n")
            f.write("| Category | Risk Level | Findings |\n| :--- | :--- | :--- |\n")
            for cat in self.selected_cats:
                risk = self.all_signatures[cat]['risk']
                f.write(f"| {cat.replace('_', ' ')} | **{risk}** | {len(self.findings[cat])} |\n")
            
            f.write("\n## 🔍 Detailed Vulnerability Analysis\n")
            for cat in self.selected_cats:
                if self.findings[cat]:
                    f.write(f"\n### ⚠️ {cat.replace('_', ' ')}\n")
                    f.write("| File Path | Found Evidence |\n| :--- | :--- |\n")
                    for entry in self.findings[cat][:100]:
                        # Sanitize match for Markdown table integrity
                        clean = entry['match'].replace('\n', ' ').replace('|', r'\|')[:120]
                        f.write(f"| `{entry['file']}` | `{clean}` |\n")
        return name

if __name__ == "__main__":
    scanner = FirmwareScanner(author_name="M-Tarantino")
    path = os.getcwd()
    while True:
        target = scanner.navigate(path)
        if target:
            scanner.run_scan(target)
            path = target
