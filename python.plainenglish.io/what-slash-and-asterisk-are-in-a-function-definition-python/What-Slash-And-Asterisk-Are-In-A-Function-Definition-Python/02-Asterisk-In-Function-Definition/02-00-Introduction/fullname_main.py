#! /usr/bin/python3.12

from pathlib import Path

import logging

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S.%s",
  filemode='+a',
  filename=f'{Path(__file__).parent}/fullname_main.log'
)

import fullname

from typing import Literal

# User-defined function
def main() -> Literal[None]:
  logging.debug(
    f"Fullname of {'Jane'=} {'Doe'=} is {fullname.fullname('Doe', 'Jane')=}"
  )
  logging.debug(
    F"Sum of {'Jane'=} and {'Doe'=} is {fullname.fullname(first_name='Jane',last_name='Doe')=}"
  )  
  return None

if __name__ == '__main__':

  # Function call
  main()