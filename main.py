# variables

morse_alphabet = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    " ": "/"
}

user_input = ""

output = ""

# main

print(f"\nLoaded py_morse_code_translator | Translate text to morse code\nEXAMPLE: wow morse code -> .-- --- .-- / -- --- .-. ... . / -.-. --- -.. .\n")

while True:
    user_input = input("Enter text: ")

    for character in user_input:
        output += morse_alphabet.get(character)
        output += " "

    print(f"\nMorse code: {output}\n")