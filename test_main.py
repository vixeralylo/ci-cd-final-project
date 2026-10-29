import subprocess
import sys
import unittest


class TestMain(unittest.TestCase):
    def test_main_prints_hello_world(self):
        result = subprocess.run(
            [sys.executable, "main.py"],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertEqual(result.stdout.strip(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
