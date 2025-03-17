import unittest
from singleton01 import Logger

class TestLogger(unittest.TestCase):
    def test_log_message(self):
        """Test if log messages are stored correctly."""
        logger = Logger()
        logger.log("Test message")
        self.assertIn("Test message", logger.get_logs())

    def test_multiple_log_messages(self):
        """Test if multiple log messages are stored in order."""
        logger = Logger()
        messages = ["First log", "Second log", "Third log"]
        
        for msg in messages:
            logger.log(msg)
        
        self.assertEqual(logger.get_logs(), messages)

    def test_logs_are_separate_instances(self):
        """Ensure separate instances have separate logs (before Singleton is implemented)."""
        logger1 = Logger()
        logger2 = Logger()

        logger1.log("Logger 1 message")
        logger2.log("Logger 2 message")

        self.assertNotEqual(logger1.get_logs(), logger2.get_logs())

if __name__ == "__main__":
    unittest.main()
