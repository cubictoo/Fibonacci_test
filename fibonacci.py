def calculate_fibonacci(n):
  """
  Calculates the nth Fibonacci number iteratively.

  Args:
    n: A non-negative integer.

  Returns:
    The nth Fibonacci number.
  """
  if n < 0:
    raise ValueError("Input must be a non-negative integer")
  elif n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    a, b = 0, 1
    for _ in range(2, n + 1):
      a, b = b, a + b
    return b

if __name__ == "__main__":
  result = calculate_fibonacci(13)
  print(f"F(13) = {result}")
