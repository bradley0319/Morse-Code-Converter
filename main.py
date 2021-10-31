"""
Text to Morse Code Converter
Author: Bradley Johnson
Copyright: 2021

This program takes an input from the user and converts it to morse code.
"""

# Global constants
MORSE_CODE_DICTIONARY = {
    'A': ". ---",
    'B': "--- . . .",
    'C': "--- . --- .",
    'D': "--- . .",
    'E': ".",
    'F': ". . --- .",
    'G': "--- --- .",
    'H': ". . . .",
    'I': ". .",
    'J': ". --- --- ---",
    'K': "--- . ---",
    "L": ". --- . .",
    "M": "--- ---",
    "N": "--- .",
    "O": "--- --- ---",
    "P": ". --- --- .",
    "Q": "--- --- . ---",
    "R": ". --- .",
    "S": ". . .",
    "T": "---",
    "U": ". . ---",
    "V": ". . . ---",
    "W": ". --- ---",
    "X": "--- . . ---",
    "Y": "--- . --- ---",
    "Z": "--- --- . .",
    "1": ". --- --- --- ---",
    "2": ". . --- --- ---",
    "3": ". . . --- ---",
    "4": ". . . . ---",
    "5": ". . . . .",
    "6": "--- . . . .",
    "7": "--- --- . . .",
    "8": "--- --- --- . .",
    "9": "--- --- --- --- .",
    "0": "--- --- --- --- ---"
}
SPACES_BETWEEN_LETTERS = "   "
SPACES_BETWEEN_WORDS = "       "
INPUT_STRING = "What information would you like to convert to morse code?\n"
WELCOME_STRING = "Welcome to Bradley's Text to Morse Code Converter."
USER_CONTINUE_STRING = "Would you like to translate anything else?  Type 'y' or 'n':\n"
USER_CONTINUE_ANSWERS = ['y', 'n']
USER_CONTINUE_STRING_WITH_INVALID_ENTRY = "Invalid entry.  Would you like to translate anything else?  " \
                                          "Type 'y' or 'n':\n"


def display_welcome_string() -> None:
    """
    This function displays WELCOME_STRING in the console.
    :return: None
    """
    print(WELCOME_STRING)


def user_input() -> str:
    """
    This function asks the user for the string they would like to convert and returns that string
    :return: The string in all upper case containing the input from the user.
    """
    return input(INPUT_STRING).upper()


def convert_string_to_morse_code(string_to_convert: str) -> str:
    """
    This function takes the string needing conversion and converts it to more code.
    :param string_to_convert: The string to convert to morse code.
    :return morse_code_string: The morse code string after conversion
    """
    morse_code_string = ""
    string_to_convert_as_a_list = string_to_convert.split()
    for word in string_to_convert_as_a_list:
        list_of_characters = list(word)
        for character in list_of_characters:
            if character in MORSE_CODE_DICTIONARY.keys():
                morse_code_string += f"{MORSE_CODE_DICTIONARY[character]}"
                morse_code_string += SPACES_BETWEEN_LETTERS
            else:
                morse_code_string += character
        if string_to_convert_as_a_list.index(word) != len(string_to_convert_as_a_list) - 1:
            morse_code_string += SPACES_BETWEEN_WORDS
    return morse_code_string


def display_morse_code_string(string_to_convert: str, morse_code_string: str) -> None:
    """
    This function prints the strings out for the user
    :param string_to_convert: original string entered for conversion
    :param morse_code_string: string converted into morse code
    :return: None
    """
    print(f"Original String for Conversion:\n{string_to_convert}")
    print(f"Morse Code String:\n{morse_code_string}")
    return None


def would_user_like_to_continue() -> bool:
    """
    Asks the user if they would like to continue
    :return: True if answer is 'y', False if answer is 'n'.
    """
    user_continues = input(USER_CONTINUE_STRING).lower()
    while user_continues not in USER_CONTINUE_ANSWERS:
        user_continues = input(USER_CONTINUE_STRING_WITH_INVALID_ENTRY).lower()
    if user_continues == USER_CONTINUE_ANSWERS[0]:
        return True
    return False


def main_function() -> None:
    """
    This is the main function for the program.
    :return: This function returns None.
    """
    display_welcome_string()
    user_continue = True
    while user_continue:
        string_to_convert = user_input()
        morse_code_output = convert_string_to_morse_code(string_to_convert)
        display_morse_code_string(string_to_convert, morse_code_output)
        user_continue = would_user_like_to_continue()
    return None


if __name__ == "__main__":
    main_function()
