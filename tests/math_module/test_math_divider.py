import sys
import os
from dotenv import load_dotenv

load_dotenv()
sys.path.insert(0, os.getenv("PYTHONPATH"))

from math_module import Math

def test_math_divide():
  # Pass tests
  assert Math.divide(1, 2) == 0.5
  assert Math.divide(1.5, 2.5) == 0.6
  assert Math.divide(1, 2.5) == 0.4
  assert Math.divide(1.5, 2) == 0.75
  assert Math.divide(1, 0) == None
  assert Math.divide(1.5, 0) == None
  assert Math.divide(0, 0) == None
  # Fail tests
  assert not Math.divide(5, 4) == 50
  assert not Math.divide(1.5, 2.5) == 0.0
  assert not Math.divide(1, 2.5) == 0.5
