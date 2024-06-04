class Math:
  """
  A simple class for basic mathematical operations.
  """
  @staticmethod
  def add(a: float | int, b: float | int) -> float | int:
    """
    Returns the sum of a and b.

    Parameters
    ----------
    a : float | int
      The first number to add.
    b : float | int
      The second number to add.

    Returns
    -------
    float | int
      The sum of a and b.
    """
    return a + b
  @staticmethod
  def subtract(a: float | int, b: float | int) -> float | int:
    """
    Returns the result of a subtracted by b.

    Parameters
    ----------
    a : float | int
      The number from which to subtract.
    b : float | int
      The number to subtract.

    Returns
    -------
    float | int
      The result of a subtracted by b.
    """
    return a - b
  @staticmethod
  def multiply(a: float | int, b: float | int) -> float | int:
    """
    Returns the product of a and b.

    Parameters
    ----------
    a : float | int
      The first number to multiply.
    b : float | int
      The second number to multiply.

    Returns
    -------
    float | int
      The product of a and b.
    """
    return a * b
  @staticmethod
  def divide(a: float | int, b: float | int) -> float | int:
    """
    Returns the quotient of a divided by b. Returns None if b is 0.

    Parameters
    ----------
    a : float | int
      The dividend.
    b : float | int
      The divisor.

    Returns
    -------
    float | int
      The quotient of a divided by b. Returns None if b is 0.
    """
    if b == 0:
      return None
    return a / b