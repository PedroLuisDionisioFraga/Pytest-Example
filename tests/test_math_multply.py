import sys
import os
from dotenv import load_dotenv


load_dotenv()
sys.path.insert(0, os.getenv("PYTHONPATH"))

from math_module import Math

def test_math_multiply():
  # Pass tests
  assert Math.multiply(1, 2) == 2
  assert Math.multiply(1.5, 2.5) == 3.75
  assert Math.multiply(1, 2.5) == 2.5
  assert Math.multiply(1.5, 2) == 3.0
  # Fail tests
  assert not Math.multiply(5, 4) == 50
  assert not Math.multiply(1.5, 2.5) == 0.0
  assert not Math.multiply(1, 2.5) == 0.5
