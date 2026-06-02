def normalize_text(text):
    result = text.strip().lower()
    return result


def split_words(text):
    result = text.split()
    return result


def has_word(text, word):
    words = split_words(text)
    result = word in words
    return result
