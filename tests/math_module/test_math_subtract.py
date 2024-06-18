import sys
import os
from dotenv import load_dotenv

load_dotenv()
sys.path.insert(0, os.getenv("PYTHONPATH"))

from math_module import Math

def test_math_subtract():
  # Pass tests
  assert Math.subtract(1, 2) == -1
  assert Math.subtract(1.5, 2.5) == -1.0
  assert Math.subtract(1, 2.5) == -1.5
  assert Math.subtract(1.5, 2) == -0.5
  # Fail tests
  assert not Math.subtract(5, 4) == 50
  assert not Math.subtract(1.5, 2.5) == 0.0
  assert not Math.subtract(1, 2.5) == 0.5
