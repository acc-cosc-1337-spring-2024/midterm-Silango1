import unittest
from question_a.main import use_global

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config

class Test_Config(unittest.TestCase):

   def test_use_global():
    global my_global_var
    original_value = my_global_var  # Store the original value for comparison

    use_global()  # Call the function that modifies the global variable

    # Assert the change
    assert my_global_var != original_value, "Global variable value should have changed."
    assert my_global_var == 20, "Global variable value should be 20 after modification."

    print("Test passed: Global variable was successfully modified inside the function.")

