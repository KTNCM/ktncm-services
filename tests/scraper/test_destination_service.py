import unittest
from unittest.mock import patch, MagicMock
from source.scraper.destinations_service import update_info, fetch_destinations
from source.scraper.destination import Destination


class TestDestinationService(unittest.TestCase):
    @patch('source.scraper.destinations_service.return_soup', return_value = MagicMock())
    def test_update_info_calls_return_soup(self, mock_return_soup: MagicMock):
        """Verify that return_soup is called within update_info.

        Args:
            mock_return_soup (MagicMock): Mock for return_soup function.
        """
        # Arrange
        destination = Destination()
        destination.url = "http://mock-url.com"

        # Act
        update_info(destination)

        # Assert
        mock_return_soup.assert_called_once_with("http://mock-url.com")

    @patch('source.scraper.destinations_service.return_soup', return_value = MagicMock())
    def test_fetch_destinations_calls_return_soup(self, mock_return_soup: MagicMock):
        """Verify that return_soup is called within fetch_destination.

        Args:
            mock_return_soup (MagicMock): Mock for return_soup function.
        """
        # Arrange
        url = "https://www.kaerntencard.at/sommer/en/ausflugsziele-uebersicht/"

        # Act
        fetch_destinations(url)

        # Assert
        mock_return_soup.assert_called_once_with(url)