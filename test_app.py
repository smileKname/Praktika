import unittest
from app import get_message

class TestApp(unittest.TestCase):
    def test_get_message(self):
        self.assertEqual(get_message(), "Привет, CI/CD!")

if __name__ == "__main__":
    unittest.main()