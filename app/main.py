from dotenv import load_dotenv
load_dotenv()

from app.bee import play


LETTERS = 'acfilor'
CENTER = 'c'


if __name__ == '__main__':
    found_words = play(LETTERS, CENTER)
    if CENTER not in LETTERS:
        print(f"Error: Center letter {CENTER} not found in letters {LETTERS}.")
        exit(1)
    for word, definition in found_words.items():
        print(f"{word}: {definition}")