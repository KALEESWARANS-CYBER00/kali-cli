#!/usr/bin/env python3

import argparse
import os
import re
import sys
from datetime import datetime

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
██╗  ██╗ █████╗ ██╗     ██╗      ██████╗██╗     ██╗
██║ ██╔╝██╔══██╗██║     ██║     ██╔════╝██║     ██║
█████╔╝ ███████║██║     ██║     ██║     ██║     ██║
██╔═██╗ ██╔══██║██║     ██║     ██║     ██║     ██║
██║  ██╗██║  ██║███████╗███████╗╚██████╗███████╗██║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝╚══════╝╚═╝
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
