morse_code = {'0': '_____', '1': '.____', '2': '..___', '3': '...__', '4': '...._',
              '5': '.....', '6': '_....', '7': '__...', '8': '___..', '9': '____.',
              'Á': '.__._', 'Ä': '._._', 'É': '.._..', 'Ñ': '__.__', 'Ö': '___.',
              'Ü': '..__', 'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.',
              'F': '.._.', 'G': '__ .', 'H': '....', 'I': '..', 'J': '.___', 'K': '_._',
              'L': '._..', 'M': '__', 'N': '_.', 'O': '___', 'P': '.__ .', 'Q': '__._',
              'R': '._.', 'S': '...', 'T': '_', 'U': '.._', 'V': '..._', 'W': '.__',
              'X': '_.._', 'Y': '_.__', 'Z': '__..', ',': '__..__', '.': '._._._',
              '?': '..__..', ';': '_._._.', ':': '___...', '/': '_.._.',
              '-': '_...._', "'": '.____.', '"': '._.._.', '_': '..__._',
              '(': '_.__.', ')': '_.__._', '=': '_..._', '+': '._._', " ": "/"}

def decode():
    sentence = input("What would you like to translate? Write here: ")
    splitted_sentence = sentence.split()
    splitted_word = []
    morse_sentence = []
    not_included = []

    for word in splitted_sentence:
        for letter in word:
            splitted_word.append(letter.upper())
        splitted_word.append(" ")

    for letter in splitted_word:
        if letter in morse_code:
            morse_sentence.append(morse_code[letter])

        else:
            not_included.append(letter)

    full_string = ""

    for string in morse_sentence:
        if string == " ":
            full_string += "/"
        full_string += string + " "

    if not_included == []:
        print(f"This si your sentence in morse code: {full_string.strip()}")
    else:
        print(f"This characters cannot be translated into morse code: {not_included}, please replace them with another similar characters.")
        decode()

def encode():
    flipped_morse_code = {}
    for key, value in morse_code.items():
        flipped_morse_code[value] = key

    morse_sentence = input("What would you like to translate? Write here: ")
    splitted_morse_sentance = morse_sentence.split()
    sentence = []
    not_included = []

    for letter in splitted_morse_sentance:
        if letter in flipped_morse_code:
            sentence.append(flipped_morse_code[letter])
        else:
            not_included.append(letter)

    if not_included != []:
        print("Please enter morse code to translate.")
        encode()
    else:
        full_string = ""

        for string in sentence:
            full_string += string

        print(f"This si your encoded sentence: {full_string.strip().lower()}")


active = True
while active:
    question = input("Do you want to decode into morse code or encode from morse code? ").lower()
    if question == "decode":
        decode()

        want_continue = input('Do you want to continue? Press "N" for not continue or any other key for continue ').lower()
        if want_continue == "n":
            active = False

    elif question == "encode":
        encode()

        want_continue = input('Do you want to continue? Press "N" for not continue or any other key for continue ').lower()
        if want_continue == "n":
            active = False

    else:
        print('Wrong input. Write "decode" or "encode" please.')






