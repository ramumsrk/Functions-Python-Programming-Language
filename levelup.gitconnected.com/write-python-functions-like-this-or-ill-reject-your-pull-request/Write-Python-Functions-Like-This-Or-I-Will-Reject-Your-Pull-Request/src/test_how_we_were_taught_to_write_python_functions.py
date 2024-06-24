#! /usr/bin/python3.12

import logging_configuration

from how_we_were_taught_to_write_python_functions.how_we_were_taught_to_write_python_functions import practice as practice

import pytest

from typing import Literal, List

@pytest.fixture
def input_list_of_numbers() -> List[int]:
  return [3, 4, 5,]

@pytest.fixture
def sample_input_number() -> Literal[int]:
  return 10

@pytest.fixture
def output_list_of_numbers() -> List[int]:
  return [13, 14, 15,]

# @pytest.mark.parametrize(
#    "input_list_of_numbers, sample_input_number, output_list_of_numbers",
#    [
#      [[3, 4, 5,], 10, [13, 14, 15,]]
#    ]  
# )
def test_practice_validity(input_list_of_numbers, sample_input_number, output_list_of_numbers) -> Literal[None]:
  # Arrange
  # Act
  # Assert
  assert output_list_of_numbers == practice(input_list_of_numbers, sample_input_number)
  return None