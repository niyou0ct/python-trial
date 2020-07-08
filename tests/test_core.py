import pathlib
from tempfile import TemporaryDirectory
import unittest
THUMBNAIL_URL = (
    'http://books.google.com/books/content'
    '?id=0gtBw760Y5EC&printsec=frontcover'
    '&img=1&zoom=1&edge=curl&source=gbs_api'
)

class SaveThumbnailsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = TemporaryDirectory()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_save_thumbnails(self):
        from booksearch.core import Book
        book = Book({'id': '', 'volumeInfo': {
            'imageLinks': {
                'thumbnail': THUMBNAIL_URL
            }
        }})
        filename = book.save_thumbnails(self.tmp.name)[0]
        self.assertTrue(pathlib.Path(filename).exists())