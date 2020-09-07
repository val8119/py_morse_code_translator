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

# functions

def translate_options():
    option = input("\nWhat would you like to do?\n(1) ASCII to morse\n(2) Morse to ASCII\n> ")
    return "ascii2morse" if option == "1" else "morse2ascii"

# main

print(f"\nLoaded py_morse_code_translator | Translate text to morse code and vice versa\n")

while True:

    if translate_options() == "ascii2morse":

    user_input = input("type something: ")

    for character in user_input:
        output += morse_alphabet.get(character)
        output += " "

    print(output)