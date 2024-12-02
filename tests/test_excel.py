from source.excel import get_excel, get_column_widths
from source.destination import Destination

def test_get_column_widths():
    # Arrange
    test_dest = Destination(name="Test location", contact_info=["Contact person"])
    test_list = [test_dest]

    # Act
    result = get_column_widths(test_list)

    # Assert
    assert result == (15, 16, 16)
