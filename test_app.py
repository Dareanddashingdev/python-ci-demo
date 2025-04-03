import unittest
from app import add  # Import the function from app.py

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # Test case 1
        self.assertEqual(add(-1, 1), 0)  # Test case 2
        self.assertEqual(add(0, 0), 0)  # Test case 3

if __name__ == "__main__":
    unittest.main()
