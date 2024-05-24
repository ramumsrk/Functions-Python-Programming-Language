#! /usr/bin/python3.12

from typing import TypeVar

T: TypeVar = TypeVar('T')

# User-defined generic function definition
def keyword_fullname[T: str](*, first_name: T, last_name: T) -> T:
  return f'{first_name=} {last_name=}'