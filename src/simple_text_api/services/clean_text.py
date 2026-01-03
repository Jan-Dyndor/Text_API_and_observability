from simple_text_api.config.conf import CHARS_TO_DEL
import re


def clean_input(
    input: str,
) -> str:
    output = input.strip().lower()

    for char in CHARS_TO_DEL:
        output = output.replace(char, "")

    output = re.sub(
        r"\s+", " ", output
    )  # Remove multiple spaces, \t ,\n  inside string

    return output


z = "Hell@o.     worl!d"
print(z)
print(clean_input(z))
