#! /usr/bin/python3.12

from pathlib import Path

import logging

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S.%s",
  filemode='+a',
  filename=f'{Path(__file__).parent}/sum_of_two_numbers_main.log'
)

import sum_of_two_numbers

from typing import Literal

# User-defined function
def main() -> Literal[None]:
  logging.debug(
    f'Sum of {2=} and {3=} is {sum_of_two_numbers.sum_of_two_numbers(2,3)=}'
  )
  logging.debug(
    f'Sum of {2=} and {3=} is {sum_of_two_numbers.sum_of_two_numbers(first_number=2,second_number=3)=}'
  )  
  return None

if __name__ == '__main__':

  # Function call
  main()