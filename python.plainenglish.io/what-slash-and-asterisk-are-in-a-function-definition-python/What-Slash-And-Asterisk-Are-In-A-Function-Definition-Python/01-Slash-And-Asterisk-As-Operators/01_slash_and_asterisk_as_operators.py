#! /usr/bin/python3.12

from typing import TypeVar

T: TypeVar = TypeVar('T')

# User-defined function
def divide_by_n[T: (int, float)](n: T) -> T:
  return n/n

# User-defined function
def multiply_by_n[T: (int, float)](n: T) -> T:
  return n * n