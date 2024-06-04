import sys
import os
from dotenv import load_dotenv

load_dotenv()
sys.path.insert(0, os.getenv("PYTHONPATH"))

from math_module import Math

def test_math_subtract():
  assert Math.subtract(1, 2) == -1
  assert Math.subtract(1.5, 2.5) == -1.0
  assert Math.subtract(1, 2.5) == -1.5
  assert Math.subtract(1.5, 2) == -0.5
