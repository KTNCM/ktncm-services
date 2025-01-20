import unittest
from unittest.mock import patch, MagicMock
from source.database import Database
import mysql.connector

class TestDatabase(unittest.TestCase):
    @patch('mysql.connector.connect', return_value = MagicMock())
    def test_connect_successful(self, mock_connect: MagicMock):
        """Test that the database connection is established successfully."""
        db = Database()
        db.connect()
        self.assertIsNotNone(db.connection)
        mock_connect.assert_called_once()

    @patch('mysql.connector.connect')
    def test_connect_unsuccessful(self, mock_connect: MagicMock):
        """Test that the database connection is established unsuccessfully."""
        mock_connect.side_effect = mysql.connector.Error()
        db = Database()
        db.connect(2, 0)
        self.assertIsNone(db.connection)
        self.assertEqual(mock_connect.call_count, 2)

    def test_insert_destinations(self):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor

        excursion_destinations = []
        db = Database()
        db.connection = mock_connection

        db.insert_destinations(excursion_destinations)

        mock_cursor.executemany.assert_called_once()
        
        mock_connection.commit.assert_called_once()
        