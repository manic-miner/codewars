from preloaded import MORSE_CODE


def decode_morse(morse_code):
    # Remember - you can use the preloaded MORSE_CODE dictionary:
    # For example:
    # MORSE_CODE['.-'] = 'A'
    # MORSE_CODE['--...'] = '7'
    # MORSE_CODE['...-..-'] = '$'
    decoded = ""
    for morse in morse_code.split(" "):
        if morse in MORSE_CODE:
            decoded += MORSE_CODE[morse]

    return decoded