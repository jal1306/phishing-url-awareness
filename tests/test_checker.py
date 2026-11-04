import sys
import unittest
from pathlib import Path

# Allow tests to import the project module when run from the project root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from phishing_checker import inspect_url


class PhishingCheckerTests(unittest.TestCase):
    def test_workbook_sample_1_no_listed_indicators(self):
        self.assertEqual(inspect_url("https://www.example.com/login"), [])

    def test_workbook_sample_2_ip_and_http(self):
        warnings = inspect_url("http://192.0.2.10/account")
        self.assertTrue(any("IP address" in item for item in warnings))
        self.assertTrue(any("HTTP" in item for item in warnings))

    def test_workbook_sample_3_at_symbol_and_http(self):
        warnings = inspect_url("http://example.com@sample.invalid/login")
        self.assertTrue(any("@'" in item for item in warnings))
        self.assertTrue(any("HTTP" in item for item in warnings))

    def test_workbook_sample_4_many_hostname_segments(self):
        warnings = inspect_url("https://a.b.c.d.e.example.invalid/path")
        self.assertTrue(any("segments" in item for item in warnings))

    def test_workbook_sample_5_punycode(self):
        warnings = inspect_url("https://xn--example.invalid/")
        self.assertTrue(any("punycode" in item for item in warnings))

    def test_long_url(self):
        url = "https://example.invalid/" + ("a" * 100)
        warnings = inspect_url(url)
        self.assertTrue(any("longer than 100" in item for item in warnings))

    def test_malformed_url_raises_value_error(self):
        with self.assertRaises(ValueError):
            inspect_url("http://[bad")

    def test_incomplete_url_raises_value_error(self):
        with self.assertRaises(ValueError):
            inspect_url("example.com")


if __name__ == "__main__":
    unittest.main()
