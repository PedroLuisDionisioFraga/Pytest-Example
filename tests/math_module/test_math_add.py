import sys
import os
from dotenv import load_dotenv

load_dotenv()
sys.path.insert(0, os.getenv("PYTHONPATH"))

from math_module import Math
#from foo import bar

def test_math_add():
  # Pass tests
  assert Math.add(1, 2) == 3
  assert Math.add(1.5, 2.5) == 4.0
  assert Math.add(1, 2.5) == 3.5
  assert Math.add(1.5, 2) == 3.5
  # Fail tests
  assert not Math.add(5, 4) == 50
  assert not Math.add(1.5, 2.5) == 0.0
  assert not Math.add(1, 2.5) == 0.5

  #bar()
