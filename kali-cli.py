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
