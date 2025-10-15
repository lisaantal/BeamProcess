# test_beamprocess.py
"""
Tests for BeamProcess module.
"""

import unittest
from beamprocess import BeamProcess

class TestBeamProcess(unittest.TestCase):
    """Test cases for BeamProcess class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BeamProcess()
        self.assertIsInstance(instance, BeamProcess)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BeamProcess()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
