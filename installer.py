import os
import sys

# Colors
G, Y, R, W, RESET = '\033[92m', '\033[93m', '\033[91m', '\033[97m', '\033[0m'

# ALL TOOLS FROM ALL VERSIONS (v1 - v17)
TOOLS = [
    "nmap", "sqlmap", "aircrack-ng", "hashcat", "john", "nikto", 
    "theHarvester", "sherlock", "sublist3r", "dirsearch", "recon-ng", 
    "amass", "finalrecon", "whatweb", "metasploit-framework", 
    "macchanger", "proxychains4", "tor", "bully", "reaver", "crunch",
    "wfuzz", "commix", "setoolkit", "spiderfoot"
]

def full_installer():
    if os.geteuid() != 0:
        print(f"{R}[!] Error: sudo ke saath chalayein!{RESET}")
        sys.exit()

    print(f"{Y}>>> ABDUL MATEEN - SYSTEM ARMORY INSTALLER <<<{RESET}")
    print(f"{W}[*] Updating System Repositories...{RESET}")
    os.system("sudo apt-get update -y")

    for tool in TOOLS:
        print(f"{G}[+] Processing: {tool}{RESET}")
        # -y aur --fix-missing lagaya hai taaki phansay nahi
        os.system(f"sudo apt-get install {tool} -y --fix-missing")

    print(f"\n{G}[SUCCESS] Saare tools install aur update ho gaye hain!{RESET}")

if __name__ == "__main__":
    full_installer()