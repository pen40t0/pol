import unittest
from main import remove_polish_diacritics


class TestPolishAlphabetConverter(unittest.TestCase):
    def test_remove_polish_diacritics(self):
        self.assertEqual(
            remove_polish_diacritics("Jędrzej Błądziński"),
            "Jedrzej Bladzinski"
        )
        self.assertEqual(
            remove_polish_diacritics("ąćęłńóśźż"),
            "acelnoszz"
        )
        self.assertEqual(
            remove_polish_diacritics("Hello World"),
            "Hello World"
        )


if __name__ == "__main__":
    unittest.main()
