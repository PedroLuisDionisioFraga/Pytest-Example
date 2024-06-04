import sys
import os
from dotenv import load_dotenv


load_dotenv()
sys.path.insert(0, os.getenv("PYTHONPATH"))

from math_module import Math

def test_math_multiply():
  assert Math.multiply(1, 2) == 2
  assert Math.multiply(1.5, 2.5) == 3.75
  assert Math.multiply(1, 2.5) == 2.5
  assert Math.multiply(1.5, 2) == 3.0