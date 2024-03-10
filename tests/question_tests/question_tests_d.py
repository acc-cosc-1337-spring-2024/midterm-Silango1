#write function tests here, don't add input('') statements here!
import unittest
from src.question_d.question_d import get_sum_of_evens

assert get_sum_of_evens(11) == 30, "Failed on input 11"
assert get_sum_of_evens(10) == 30, "Failed on input 10"
assert get_sum_of_evens(8) == 20, "Failed on input 8"

print("All test cases passed!")
