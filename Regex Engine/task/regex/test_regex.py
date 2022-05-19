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
        self.assertTrue(regex.reg_engine('^app|apple'), 'Error when comparing "^app|apple"')
        self.assertTrue(regex.reg_engine('le$|apple'), 'Error when comparing "le$|apple"')
        self.assertTrue(regex.reg_engine('^a|apple'), 'Error when comparing "^a|apple"')
        self.assertTrue(regex.reg_engine('.$|apple'), 'Error when comparing ".$|apple"')
        self.assertTrue(regex.reg_engine('apple$|tasty apple'), 'Error when comparing "apple$|tasty apple"')
        self.assertTrue(regex.reg_engine('^apple|apple pie'), 'Error when comparing "^apple|apple pie"')
        self.assertTrue(regex.reg_engine('^apple$|apple'), '^apple$|apple"')
        self.assertFalse(regex.reg_engine('^apple$|tasty apple'), 'Error when comparing "^apple$|tasty apple"')
        self.assertFalse(regex.reg_engine('^apple$|apple pie'), 'Error when comparing "^apple$|apple pie"')
        self.assertFalse(regex.reg_engine('app$|apple'), 'Error when comparing "app$|apple"')
        self.assertFalse(regex.reg_engine('^le|apple'), 'Error when comparing "^le|apple"')

    def test_corners(self):
        self.assertTrue(regex.reg_engine('.|a'), 'Error when comparing ".|a"')
        self.assertTrue(regex.reg_engine('|a'), 'Error when comparing "|a"')
        self.assertTrue(regex.reg_engine('|'), 'Error when comparing "|"')
        self.assertTrue(regex.reg_engine('^|apple'), 'Error when comparing "^|apple"')
        self.assertTrue(regex.reg_engine('$|apple'), 'Error when comparing "$|apple"')
        self.assertFalse(regex.reg_engine('a|'), 'Error when comparing "a|"')
        self.assertFalse(regex.reg_engine('^$|'), 'Error when comparing "^$|"')
        self.assertFalse(regex.reg_engine('^$|apple'), 'Error when comparing "^$|apple"')
        self.assertTrue(regex.reg_engine('.*|aaa'), 'Error when comparing ".*|aaa"')
        self.assertTrue(regex.reg_engine('^no+|noooooooope'), 'Error when comparing "^no+|noooooooope"')
        self.assertTrue(regex.reg_engine('^no+pe$|noooooooope'), 'Error when comparing "^no+pe$|noooooooope"')
        self.assertTrue(regex.reg_engine('^.*c$|abcabc'), 'Error when comparing "^.*c$|abcabc"')

    def test_question_mark(self):
        self.assertTrue(regex.reg_engine('colou?r|color'), 'Error when comparing "colou?r|color"')
        self.assertTrue(regex.reg_engine('colou?r|colour'), 'Error when comparing "colou?r|colour"')
        self.assertFalse(regex.reg_engine('colou?r|colouur'), 'Error when comparing "colou?r|colouur"')

    def test_asterisk(self):
        self.assertTrue(regex.reg_engine('colou*r|color'), 'Error when comparing "colou*r|color"')
        self.assertTrue(regex.reg_engine('colou*r|colour'), 'Error when comparing "colou*r|colour"')
        self.assertTrue(regex.reg_engine('colou*r|colouur'), 'Error when comparing "colou*r|colouur"')
        self.assertTrue(regex.reg_engine('col.*r|color'), 'Error when comparing "col.*r|color"')
        self.assertTrue(regex.reg_engine('col.*r|colour'), 'Error when comparing "col.*r|colour"')
        self.assertTrue(regex.reg_engine('col.*r|colr'), 'Error when comparing "col.*r|colr"')
        self.assertTrue(regex.reg_engine('col.*r|collar'), 'Error when comparing "col.*r|collar"')
        self.assertFalse(regex.reg_engine('col.*r$|colors'), 'Error when comparing "col.*r|colors"')

    def test_plus(self):
        self.assertTrue(regex.reg_engine('colou+r|colour'), 'Error when comparing "colou+r|colour"')
        self.assertTrue(regex.reg_engine('colou+r|colouur'), 'Error when comparing "colou+r|colouur"')
        self.assertFalse(regex.reg_engine('colou+r|color'), 'Error when comparing "colou+r|color"')


if __name__ == "__main__":
    unittest.main()
