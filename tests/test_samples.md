# Workbook Sample Test Cases

These are the five fictional/example URL strings provided in the EWB workbook. They are analysed as text only; the checker does not open them.

| # | Sample URL | Expected warning indicators |
|---|---|---|
| 1 | `https://www.example.com/login` | No listed warning signs |
| 2 | `http://192.0.2.10/account` | IP-address hostname; HTTP scheme |
| 3 | `http://example.com@sample.invalid/login` | `@` symbol; HTTP scheme |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Five or more hostname segments |
| 5 | `https://xn--example.invalid/` | Punycode marker |

## Interpretation

- “No listed warning signs” does **not** mean the URL is safe.
- A detected indicator does **not** prove the URL is malicious.
- These examples are for learning and testing only. No network connection is made.
