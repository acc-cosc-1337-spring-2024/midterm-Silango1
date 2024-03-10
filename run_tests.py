#DON'T MAKE CHANGES TO THIS FILE

#write tests for all the questions here

import unittest

from tests.question_tests import question_tests_a

suite = unittest.TestLoader().loadTestsFromModule(question_tests_a)
unittest.TextTestRunner(verbosity=2).run(suite)
