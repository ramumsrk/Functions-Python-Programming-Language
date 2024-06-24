#! /usr/bin/python3.12

from typing import Literal, List

def practice(
  input_list_of_numbers: List[int],
  sample_input_number: Literal[int],
  /
) -> List[int]:
  """
  Add sample_input_number to every
  item in input_list_of_numbers
  Inputs:
    input_list_of_numbers:
      A list of numbers to increment
    sample_input_number:
      Number used to increment every item in input_list_of_numbers
  Outputs:
    Return a new list with every item in input_list_of_numbers incremented by sample_input_number
  """
  output_list_of_numbers: List[int] = [number + sample_input_number for number in input_list_of_numbers]
  return output_list_of_numbers 