import unittest
from unittest.mock import patch, MagicMock, call
from source.destinations_service import fetch_destination_details, update_info, fetch_destinations
from source.destination import Destination


class TestDestinationService(unittest.TestCase):
    @patch('source.destinations_service.return_soup', return_value = MagicMock())
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

    @patch('source.destinations_service.return_soup', return_value = MagicMock())
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

    @patch('source.destinations_service.update_info')  # Mock the update_info function
    def test_fetch_destination_details(self, mock_update_info):
        # Create mock Destination objects
        destination1 = MagicMock(spec=Destination)
        destination2 = MagicMock(spec=Destination)
        excursion_destinations = [destination1, destination2]
        
        # Call the function being tested
        result = fetch_destination_details(excursion_destinations)
        
        # Assert that update_info was called once for each destination
        self.assertEqual(mock_update_info.call_count, 2)
        mock_update_info.assert_has_calls([call(destination1), call(destination2)], any_order=True)
        
        # Assert that the result matches the input (function returns the input list)
        self.assertEqual(result, excursion_destinations)