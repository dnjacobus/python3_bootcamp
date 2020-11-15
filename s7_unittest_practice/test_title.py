import unittest
import title

class TestTitle(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = title.title_text(text)
        self.assertEqual(result,'Python')
    
    def multi_words(self):
        text = 'monty python'
        result = title.title_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
    unittest.main()