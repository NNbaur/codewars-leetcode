# Welcome.
#
# In this kata you are required to, given a string,
# replace every letter with its position in the alphabet.
#
# If anything in the text isn't a letter,
# ignore it and don't return it.
#
# "a" = 1, "b" = 2, etc.
#
# Example
# alphabet_position("The sunset")
# Should return "20 8 5 19 21 14 19 5 20" ( as a string )


def alphabet_position(text: str) -> str:
    return ' '.join(
        [str(ord(char.lower())-96) for char in text if char.isalpha()]
    )
