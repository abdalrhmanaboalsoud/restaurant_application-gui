import pytest
from unittest.mock import patch, MagicMock
from rest_gui.rest_gui import *


@patch('rest_gui.rest_gui.pizza_size_var')
@patch('rest_gui.rest_gui.pizza_quantity_var')
@patch('rest_gui.rest_gui.burger_size_var')
@patch('rest_gui.rest_gui.burger_quantity_var')
@patch('rest_gui.rest_gui.soft_drinks_quantity_var')
@patch('rest_gui.rest_gui.cheese_var')
@patch('rest_gui.rest_gui.ketchup_var')
def test_calculate_price(mock_ketchup_var, mock_cheese_var, mock_soft_drinks_quantity_var, mock_burger_quantity_var, mock_burger_size_var, mock_pizza_quantity_var, mock_pizza_size_var):
    # Set the return values of the mock objects
    mock_pizza_size_var.get.return_value = "Medium"
    mock_pizza_quantity_var.get.return_value = "2"
    mock_burger_size_var.get.return_value = "Big"
    mock_burger_quantity_var.get.return_value = "1"
    mock_soft_drinks_quantity_var.get.return_value = "3"
    mock_cheese_var.get.return_value = True
    mock_ketchup_var.get.return_value = False

    expected_price = 28
    
    assert calculate_price() == expected_price
