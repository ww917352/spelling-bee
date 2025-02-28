from app.dictionary import lookup
from app.llm import collect_words_with_gemini

MAX_ROUNDS = 20

found_words = {}

def find_words(letters, center):
    words = collect_words_with_gemini(letters, center, found_words.keys())
    valid_words = [word for word in words if center in word and all(letter in letters for letter in word) and len(word) >= 4 and word not in found_words.keys()]
    new_words = {word: lookup(word) for word in valid_words}
    found_words.update({word: definition for word, definition in new_words.items() if definition is not None})
    return bool(new_words)


def play(letters, center):
    round = 1
    while find_words(letters, center) and round <= MAX_ROUNDS:
        print(f"Round {round} completed.")
        round += 1
    return found_words