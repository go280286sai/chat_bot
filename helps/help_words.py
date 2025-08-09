import pathlib


def get_words(lang):
    with open(f"stop_words/{lang}.txt", "r", encoding="utf-8") as f:
        words = f.read().splitlines()
        return words
