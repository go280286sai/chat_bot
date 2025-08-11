"""
Module stop_words
"""


def get_words(lang: str) -> list:
    """
    Get stop words from a language
    :param lang:
    :return:
    """
    with open(f"src/app/stop_words/{lang}.txt", "r", encoding="utf-8") as f:
        words = f.read().splitlines()
        return words
