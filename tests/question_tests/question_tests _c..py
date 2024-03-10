#write function tests here, don't add input('') statements here!
import unittest
from src.question_c.question_c import get_random_number
# Testing the function over multiple calls to ensure it generates numbers in the range 1 to 5
for _ in range(100):  # Test it 100 times to be confident
    number = get_random_number()
    assert 1 <= number <= 5, "The generated number is out of the 1-5 range."
print("Function passed the test: Always generates a number in the 1-5 range.")
