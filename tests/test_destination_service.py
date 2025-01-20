import unittest
from unittest.mock import patch, MagicMock
from source.destinations_service import update_info
from source.destination import Destination


class TestDestinationService(unittest.TestCase):
    @patch('source.destinations_service.return_soup', return_value = MagicMock())
    def test_update_info_calls_return_soup(self, mock_return_soup: MagicMock):
        # Arrange
        destination = Destination()
        destination.url = "http://mock-url.com"

        # Act
        update_info(destination)

        # Assert
        mock_return_soup.assert_called_once_with("http://mock-url.com")