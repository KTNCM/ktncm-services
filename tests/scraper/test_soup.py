from unittest import mock
from bs4 import BeautifulSoup
from source.scraper.soup import return_soup

mock_response = mock.Mock()
mock_response.text = "<html><head><title>Test Page</title></head><body></body></html>"

@mock.patch('requests.get', return_value = mock_response)
def test_return_soup(mocker):
    # Arrange
    url = "http://example.com"

    # Act
    soup = return_soup(url)

    # Assert
    assert isinstance(soup, BeautifulSoup)
    assert soup.title.string == "Test Page"