"""
Phishing URL Awareness Checker
A beginner-friendly, offline tool that checks URL text for common warning signs.

IMPORTANT:
- This program does not open or visit URLs.
- It does not prove that a URL is safe or malicious.
- It only reports the six indicators described in the EWB workbook.
"""

import ipaddress
import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    """Inspect URL text and return a list of warning messages.

    The function performs local text parsing only. It never makes network
    requests or contacts the destination website.
    """
    if not isinstance(raw_url, str):
        raise ValueError("Input must be text.")

    raw_url = raw_url.strip()
    if not raw_url:
        raise ValueError("URL cannot be empty.")

    # urlparse can raise ValueError for malformed bracketed IPv6 addresses.
    try:
        parsed = urlparse(raw_url)
        hostname = parsed.hostname
    except ValueError as error:
        raise ValueError(f"Malformed URL: {error}") from error

    if not parsed.scheme or not parsed.netloc or not hostname:
        raise ValueError(
            "Please enter a complete URL including a scheme, "
            "for example https://www.example.com"
        )

    warnings = []

    # Indicator 1: @ can make the actual destination confusing.
    if "@" in raw_url:
        warnings.append(
            "The URL contains '@' — check carefully which part is the "
            "actual destination hostname."
        )

    # Indicator 2: unusually long URL text.
    if len(raw_url) > 100:
        warnings.append(
            f"The URL is longer than 100 characters ({len(raw_url)} characters)."
        )

    # Indicator 3: hostname is an IP address.
    try:
        ipaddress.ip_address(hostname)
        warnings.append("The hostname is an IP address rather than a domain name.")
    except ValueError:
        pass

    # Indicator 4: hostname has five or more labels/segments.
    labels = [part for part in hostname.rstrip(".").split(".") if part]
    if len(labels) >= 5:
        warnings.append(
            f"The hostname has {len(labels)} segments (5 or more is a warning sign)."
        )

    # Indicator 5: internationalised domain punycode marker.
    if "xn--" in hostname.lower():
        warnings.append("The hostname contains 'xn--' (punycode).")

    # Indicator 6: unencrypted HTTP scheme.
    if parsed.scheme.lower() == "http":
        warnings.append("The URL uses HTTP instead of HTTPS.")

    return warnings


def display_result(url, warnings):
    """Print a readable result for one URL."""
    print("\n" + "=" * 66)
    print(f"URL: {url}")
    if warnings:
        print(f"Review carefully — {len(warnings)} warning sign(s) found:")
        for number, warning in enumerate(warnings, start=1):
            print(f"  {number}. {warning}")
    else:
        print("No listed warning signs found.")
        print("This does NOT mean the URL is safe.")
    print("=" * 66)


def main():
    """Run the interactive multi-URL command-line checker."""
    print("PHISHING URL AWARENESS CHECKER")
    print("Offline text checker | Does not visit or verify websites")
    print("Enter one complete URL at a time. Type 'quit' to exit.")

    while True:
        try:
            raw_url = input("\nEnter URL: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting checker. Stay alert online!")
            break

        if raw_url.lower() in {"quit", "exit", "q"}:
            print("Exiting checker. Stay alert online!")
            break

        try:
            warnings = inspect_url(raw_url)
            display_result(raw_url, warnings)
        except ValueError as error:
            print(f"Input error: {error}")
            print("Please correct the input and try again.")


if __name__ == "__main__":
    main()
