from simple_text_api.config.conf import CHARS_TO_DEL
import re


def clean_input(
    input: str,
) -> str:
    """
    lean text function - remove specific signs from string and unnecessary spaces

    :param input: user provided string
    :type input: str
    :return: clean string, ready for analysis
    :rtype: str
    """
    output = input.lower()

    for char in CHARS_TO_DEL:
        output = output.replace(char, "")

    output = re.sub(
        r"\s+", " ", output
    )  # Remove multiple spaces, \t ,\n  inside string

    return output.strip()
