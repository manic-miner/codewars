def alphabet_position(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text_convert = ""
    for letter in text:
        if letter.lower() in alphabet:
            text_convert += str(alphabet.index(letter.lower()) + 1) + " "
        else:
            pass
    return text_convert.rstrip()


test1 = alphabet_position("The sunset sets at twelve o' clock.")
print(test1)