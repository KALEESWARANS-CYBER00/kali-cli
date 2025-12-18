# kali-cli  v0.1

**kali-cli** is a  CLI tool built purely with Python's `argparse`.  
It provides a stylish ASCII banner, colored output, and basic target classification for IPs, CIDRs, domains, and files.

---

## Features (v0.1)

- ASCII banner with colored output
- Target classification: IPv4, CIDR, Domain, File, Unknown
- Verbose mode for step-by-step output
- Output results to a file
- Pure Python, no external dependencies

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/kali-cli.git
cd kali-cli
chmod +x kali-cli.py

Usage
Basic

./kali-cli.py 192.168.1.1

Verbose Mode

./kali-cli.py example.com -v

Output to File

./kali-cli.py 10.0.0.1 -o output.txt

Disable Banner

./kali-cli.py 10.0.0.1 --no-banner

Example Output

██╗  ██╗ █████╗ ██╗     ██╗         ██████╗ ██╗     ██╗
██║ ██╔╝██╔══██╗██║     ██║         ██╔════╝██║     ██║
█████╔╝ ███████║██║     ██║ █████╗  ██║     ██║     ██║
██╔═██╗ ██╔══██║██║     ██║ ╚════╝  ██║     ██║     ██║
██║  ██╗██║  ██║███████╗██║         ╚██████╗███████╗██║ v1.0
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝          ╚═════╝╚══════╝╚═╝
[ kali-cli :: hacker-style argparse tool ]

[+] Target     : 192.168.1.1
[+] Type       : IPv4
[+] Length     : 11
[+] Timestamp  : 2025-12-18T13:23:34+00:00

License

MIT License
Author

kali