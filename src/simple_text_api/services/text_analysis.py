from collections import Counter
from typing import Dict, List


def count_words(clean_text: str) -> int:
    """
    Count number of words in string input

    :param clean_text: clean string
    :return: numebr of words
    :rtype: int
    """
    words: List[str] = clean_text.split()
    count: int = len(words)
    return count


def most_frequent_words(clean_text: str) -> Counter[str]:
    """
    Most frequent words counts

    :param clean_text: clean string
    :type clean_text: str
    :return: dictionary containing the word : count values
    :rtype: Dict[string, int]
    """
    clean_text = clean_text.replace(".", "")
    return Counter(clean_text.split())


def most_frequent_char(clean_text: str) -> Counter[str]:
    """
    Most frequent char in clean string

    :param clean_text: clean string
    :type clean_text: str
    :return: dictionary containing the word : count values
    :rtype: Dict[str, int]
    """
    return Counter(clean_text)


def count_sentences(clean_text: str) -> int:
    """
    Sentence counter

    :param clean_text: clean string
    :type clean_text: str
    :return: numebr of sentences in string
    :rtype: int
    """
    return clean_text.count(".")
