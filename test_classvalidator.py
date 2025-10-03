# test_classvalidator.py
"""
Tests for ClassValidator module.
"""

import unittest
from classvalidator import ClassValidator

class TestClassValidator(unittest.TestCase):
    """Test cases for ClassValidator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ClassValidator()
        self.assertIsInstance(instance, ClassValidator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ClassValidator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
