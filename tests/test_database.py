import unittest
from unittest.mock import patch, MagicMock
from source.database import Database

class TestDatabase(unittest.TestCase):
    @patch('mysql.connector.connect', return_value = MagicMock())
    def test_connect_successful(self, mock_connect: MagicMock):
        """Test that the database connection is established successfully."""
        db = Database()
        db.connect()
        self.assertIsNotNone(db.connection)
        mock_connect.assert_called_once()