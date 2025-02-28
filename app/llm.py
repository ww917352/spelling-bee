import json
import os
import re
import google.generativeai as genai

from app.dictionary import lookup

PROMPT = """
I am playing Spelling Bee. Its rule is described as follows:

The game presents players with a hexagonal grid of 7 letters arrayed in a honeycomb structure.
The player scores points by using these and only these letters to form words consisting of four or more letters.
However, any words proposed by the player must include the letter at the center of the honeycomb.
Each letter can be used more than once.

Now, for the following 7 letters: {letters} with {center_letter} as the center letter, find all the possible words that can be formed.
Especially, find those words that use all of these letters.

Also, we have found these words {found_words}, please do not repeat them.

Output the words in a json list and nothing else.
"""

API_KEY = os.getenv('GEMINI_API_KEY')
print(API_KEY)

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(model_name='gemini-2.0-flash')

def parse_response(response):
    match = re.search(r'```json\s*([\s\S]*?)\s*```', response.text)
    if match:
        json_string = match.group(1)
        return json.loads(json_string)
    else:
        print("Error: JSON not found in response.")
        print(response.text)


def collect_words_with_gemini(letters, center_letter, found_words):
    found_words_str = ', '.join(found_words)
    prompt = PROMPT.format(letters=letters, center_letter=center_letter, found_words=found_words_str)
    response = model.generate_content(prompt)
    return parse_response(response)