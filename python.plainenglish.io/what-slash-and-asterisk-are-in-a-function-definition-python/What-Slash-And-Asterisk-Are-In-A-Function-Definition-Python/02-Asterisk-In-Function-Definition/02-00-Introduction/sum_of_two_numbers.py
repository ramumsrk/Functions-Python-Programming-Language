#! /usr/bin/python3.12

from typing import TypeVar

T: TypeVar = TypeVar('T')

# User-defined generic function definition
def sum_of_two_numbers[T: (int, float)](first_number: T, second_number: T) -> T:
  return first_number + second_number