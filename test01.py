import unittest
import cap # targets for test


class TestCap(unittest.TestCase):
    def setUp(self): # called when a case is started
        pass

    def tearDown(self): # called when a case is done
        pass

    def test_one_word(self):
        text = 'duck'
        result = cap.just_do_it(text) # call the function and examine its result
        self.assertEqual(result, 'Duck')

    def test_multiple_words(self):
        text = 'a duck'
        result = cap.just_do_it(text)
        self.assertEqual(result, 'A duck')


if __name__ == '__main__':
    unittest.main()
