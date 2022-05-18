import unittest
import regex


class TestRegex(unittest.TestCase):  # a test case for the regex.py module
    def test_single_character_check(self):
        self.assertTrue(regex.single_character_check('a', 'a'), 'Error when comparing "a" and "a"')
        self.assertTrue(regex.single_character_check('.', 'a'), 'Error when comparing "." and "a"')
        self.assertFalse(regex.single_character_check('a', 'b'), 'Error when comparing "a" and "b"')

    def test_multi_character_check(self):
        self.assertTrue(regex.multi_character_check('apple|apple'), 'Error when comparing "apple|apple"')
        self.assertTrue(regex.multi_character_check('.pple|apple'), 'Error when comparing ".pple|apple"')
        self.assertTrue(regex.multi_character_check('appl.|apple'), 'Error when comparing "appl.|apple"')
        self.assertTrue(regex.multi_character_check('.....|apple'), 'Error when comparing ".....|apple"')
        self.assertFalse(regex.multi_character_check('peach|apple'), 'Error when comparing "peach|apple"')

    def test_reg_engine(self):
        self.assertTrue(regex.reg_engine('apple|apple'), 'Error when comparing "apple|apple"')
        self.assertTrue(regex.reg_engine('ap|apple'), 'Error when comparing ".ap|apple"')
        self.assertTrue(regex.reg_engine('le|apple'), 'Error when comparing "le|apple"')
        self.assertTrue(regex.reg_engine('a|apple'), 'Error when comparing "a|apple"')
        self.assertTrue(regex.reg_engine('.|apple'), 'Error when comparing ".|apple"')
        self.assertFalse(regex.reg_engine('apwle|apple'), 'Error when comparing "apwle|apple"')
        self.assertFalse(regex.reg_engine('peach|apple'), 'Error when comparing "peach|apple"')


if __name__ == "__main__":
    unittest.main()
