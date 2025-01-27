#!/usr/bin/env python
# coding: utf-8

"""
Polish Alphabet Diacritic Remover

This script replaces Polish letters with diacritics (e.g., ą, ć, etc.)
with their ASCII equivalents. It provides a function `remove_polish_diacritics`
that takes a string as input and returns the converted string.

Steps:
1. Define a dictionary mapping Polish letters with diacritics to their ASCII counterparts.
2. Iterate through the dictionary and replace each Polish letter in the input text.
3. Return the modified string.

Usage:
Run the script and provide a string with Polish letters when prompted.
Example:
Input: "Jędrzej Błądziński"
Output: "Jedrzej Bladzinski"
"""


def remove_polish_diacritics(text: str) -> str:
    """
    Replace Polish letters with diacritics in a string with their ASCII equivalents.

    Args:
        text (str): The input string containing Polish letters.

    Returns:
        str: The modified string with Polish letters replaced by ASCII equivalents.
    """
    replacements: dict[str, str] = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l',
        'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'
    }
    for polish_char, ascii_char in replacements.items():
        text = text.replace(polish_char, ascii_char)
    return text


if __name__ == "__main__":
    # Prompt the user for input
    input_text: str = input("Enter a string with Polish letters: ")

    # Call the function to replace Polish letters
    result: str = remove_polish_diacritics(input_text)

    # Print the result
    print("Converted string:", result)
