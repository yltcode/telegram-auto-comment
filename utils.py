import json
import random

normal = list("абвгдежзийклмнопрстуфхцчшщыьэюя")

with open("chars.json", "r") as file:
    fonts = json.load(file)


def make_text_with_font(string: str):
    for letter in string:
        if letter == " ":
            yield " "
        elif letter.isupper():
            continue
        else:
            index = normal.index(letter)
            yield random.choice(fonts)[index]
