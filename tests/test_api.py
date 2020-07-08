import unittest

class BuildUrlTest(unittest.TestCase):
    def test_build_url(self):
        from booksearch.api import build_url
        expected = 'https://www.googleapis/books/v1/volumes?q=python'
        actual = build_url({'q': 'python'})

        self.assertEqual(expected, actual)

    def test_build_url_empty_param(self):
        from booksearch.api import build_url
        expected = 'https://www.googleapis/books/v1/volumes?'
        actual = build_url({})

        self.assertEqual(expected, actual)
