import subprocess
import sys
import unittest
from pathlib import Path


class SimpleExampleTests(unittest.TestCase):
    def test_program_prints_totals_with_tax(self):
        script = Path(__file__).with_name("simple.py")
        result = subprocess.run(
            [sys.executable, str(script)],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertEqual(result.stdout, "Total: 120.0\nTotal: 240.0\n")


if __name__ == "__main__":
    unittest.main()
