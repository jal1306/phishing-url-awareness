# Phishing URL Awareness Checker

A beginner-friendly Python command-line project that checks **URL text only** for six common warning signs. It is designed for defensive cybersecurity awareness and follows the EWB Phishing URL Checker Workbook.

> **Important:** This tool does not visit URLs, connect to websites, check reputation, or prove whether a URL is safe or malicious. “No listed warning signs found” is not a safety guarantee.

## 1. Overview

Phishing URLs can use confusing characters, unusual hostnames, or insecure URL schemes to mislead users. This project highlights a small set of indicators so a user can pause and review a link carefully.

## 2. Features

The checker looks for these six indicators:

1. `@` symbol in the URL text.
2. URL length greater than 100 characters.
3. An IP address used as the hostname.
4. Five or more hostname segments/labels.
5. `xn--` punycode marker in the hostname.
6. `http` scheme instead of `https`.

It also includes:
- A multi-URL input loop; type `quit` to exit.
- A “Review carefully” summary when warning signs are found.
- A clear message when no listed warning signs are found.
- Basic malformed-input handling.
- A numbered explanation for each warning.

## 3. Requirements

- Python 3.10 or newer.
- No third-party Python packages are required. The project uses Python standard-library modules: `ipaddress`, `urllib.parse`, and `re` (the URL checker itself uses the standard library only).

## 4. Project structure

```text
phishing-url-awareness/
├── phishing_checker.py
├── README.md
├── requirements.txt
├── tests/
│   ├── test_checker.py
│   └── test_samples.md
└── screenshots/
    ├── sample_run.png
    └── test_results.png
```

## 5. How to run

Open a terminal in this project folder and run:

```bash
python phishing_checker.py
```

Enter a complete URL including `http://` or `https://`. Enter multiple URLs one by one. Type `quit` when finished.

Example:

```text
PHISHING URL AWARENESS CHECKER
Offline text checker | Does not visit or verify websites
Enter one complete URL at a time. Type 'quit' to exit.

Enter URL: http://192.0.2.10/account

==================================================================
URL: http://192.0.2.10/account
Review carefully — 2 warning sign(s) found:
  1. The hostname is an IP address rather than a domain name.
  2. The URL uses HTTP instead of HTTPS.
==================================================================
```

## 6. Testing

Run the automated tests from the project folder:

```bash
python -m unittest discover -s tests -v
```

The five workbook sample cases and expected indicators are documented in [`tests/test_samples.md`](tests/test_samples.md). Automated tests are in [`tests/test_checker.py`](tests/test_checker.py).

## 7. Screenshots / evidence

- `screenshots/sample_run.png` — example command-line run using a workbook sample.
- `screenshots/test_results.png` — evidence of the five sample cases and automated test results.

The screenshots use fictional/example URLs only.

## 8. Improvements included

- Added a multi-URL loop with a quit option.
- Added a “Review carefully” warning summary.
- Added handling for malformed and incomplete URL input.
- Added a short explanation for every detected indicator.
- Improved command-line formatting and numbered output.

## 9. Limitations

- The checker only analyses the text supplied by the user.
- It does not visit URLs or make internet requests.
- It does not scan websites, follow redirects, or query threat-intelligence services.
- It checks only the six indicators listed in the workbook.
- A URL may be dangerous even when none of these indicators are found.
- A URL containing one or more indicators is not automatically malicious; manual review is required.

## 10. Ethical use

Use this project for defensive learning and awareness. Use only fictional or otherwise authorised sample strings. Do not use it to target, scan, probe, or test websites without permission. Never enter passwords, OTPs, session tokens, or other private information.

## 11. Author

**Name:** [Add your full name]  
**Course/Batch:** [Add your course and batch]  
**Project:** EWB Cybersecurity — Phishing URL Awareness Checker

Before publishing, replace the author placeholders with your own details and review the code so you can explain how it works.
