#!/usr/bin/env python3

import argparse
import os
import re
import sys
from datetime import datetime, timezone


RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
GRAY = "\033[90m"

BANNER = f"""
{RED}{BOLD}
██╗  ██╗ █████╗ ██╗     ██╗         ██████╗ ██╗     ██╗
██║ ██╔╝██╔══██╗██║     ██║         ██╔════╝██║     ██║
█████╔╝ ███████║██║     ██║ █████╗  ██║     ██║     ██║
██╔═██╗ ██╔══██║██║     ██║ ╚════╝  ██║     ██║     ██║
██║  ██╗██║  ██║███████╗██║         ╚██████╗███████╗██║ v0.1
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝          ╚═════╝╚══════╝╚═╝
{RESET}
{GRAY}[ kali-cli :: hacker-style argparse tool ]{RESET}
"""


IPV4_REGEX = re.compile(r"^(?:\d{1,3}\.){3}\d{1,3}$")
CIDR_REGEX = re.compile(r"^(?:\d{1,3}\.){3}\d{1,3}/\d{1,2}$")
DOMAIN_REGEX = re.compile(r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$")


def classify_target(target: str) -> str:
    if CIDR_REGEX.match(target):
        return "CIDR"
    if IPV4_REGEX.match(target):
        return "IPv4"
    if DOMAIN_REGEX.match(target):
        return "Domain"
    if os.path.isfile(target):
        return "File"
    return "Unknown"


def info(label, value):
    print(f"{GREEN}[+]{RESET} {BOLD}{label:<12}{RESET}: {value}")


def warn(msg):
    print(f"{YELLOW}[*]{RESET} {msg}")


def error(msg):
    print(f"{RED}[-]{RESET} {msg}")


def main():
    parser = argparse.ArgumentParser(
        prog="kali-cli",
        description="argparse-style CLI tool using argparse only",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "target",
        help="Target input (IP, CIDR, domain, or file)"
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )

    parser.add_argument(
        "-o", "--output",
        metavar="FILE",
        help="Write results to output file"
    )

    parser.add_argument(
        "--no-banner",
        action="store_true",
        help="Disable banner output"
    )

    args = parser.parse_args()

    if not args.no_banner:
        print(BANNER)

    if args.verbose:
        warn("Starting classification engine")

    target_type = classify_target(args.target)
    timestamp = datetime.now(timezone.utc).isoformat()

    if args.verbose:
        warn(f"Target received: {args.target}")
        warn(f"Matched type: {target_type}")

    output_lines = []
    output_lines.append(f"Target     : {args.target}")
    output_lines.append(f"Type       : {target_type}")
    output_lines.append(f"Length     : {len(args.target)}")
    output_lines.append(f"Timestamp  : {timestamp}")

    info("Target", args.target)
    info("Type", target_type)
    info("Length", len(args.target))
    info("Timestamp", timestamp)

    if args.output:
        try:
            with open(args.output, "w") as f:
                f.write("\n".join(output_lines) + "\n")
            if args.verbose:
                warn(f"Output written to {args.output}")
        except Exception as e:
            error(str(e))
            sys.exit(1)



if __name__ == "__main__":
    main()
