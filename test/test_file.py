from unittest.mock import MagicMock, patch
from src.file import AvgCalculator


def test_calculate():
    data = [['1', '2', '3', '4', '5'], ['2', '4', '1', '12']]
    mock = MagicMock()
    mock.return_value = data

    with patch('src.file.AvgCalculator._get_content', mock):
        avg = AvgCalculator('whatever.txt')
        assert avg.calculate() == [3, 4.75]


def test_get_data():
    data = [['1', '2', '3', '4', '5'], ['2', '4', '1', '12']]
    mock = MagicMock()
    mock.return_value = data

    with patch('src.file.AvgCalculator._get_content', mock):
        avg = AvgCalculator('whatever.txt')
        assert avg.get_data() == data
