#!/usr/bin/env python3
"""
Unit tests for main.py
"""

import unittest
import sys
import os

# Add parent directory to path to import main
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import hello_world

class TestHelloWorld(unittest.TestCase):
    """
    Test cases for hello_world function
    """
    
    def test_hello_world_returns_string(self):
        """
        Test that hello_world returns a string
        """
        result = hello_world()
        self.assertIsInstance(result, str)
    
    def test_hello_world_content(self):
        """
        Test that hello_world returns expected message
        """
        result = hello_world()
        expected = "Hello World from CSDR Compliance Knowledge Graphs and Assistant!"
        self.assertEqual(result, expected)
    
    def test_hello_world_not_empty(self):
        """
        Test that hello_world returns non-empty string
        """
        result = hello_world()
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()
