import unittest
from FileManipulation import LoadingJson


class LoadingJsonTests(unittest.TestCase):

    def test_load_json_test(self):
        actual = LoadingJson.load_dictionary_from_json('drfeg')
        expected = 'foo'
        assert actual == expected
