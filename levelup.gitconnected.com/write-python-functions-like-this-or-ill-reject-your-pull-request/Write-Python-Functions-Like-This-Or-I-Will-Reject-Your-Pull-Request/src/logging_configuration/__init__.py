#! /usr/bin/python3.12

from pathlib import Path

import logging

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  filemode='+at',
  filename=f'{Path(__file__).parent.parent.parent}/logs/write_python_functions_like_this_or_I_will_reject_your_pull_request.log',
  format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
  datefmt='%A, %B %d, %Y %H:%M:%S %Z %z'
)