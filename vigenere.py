import string

LETTER_START: int = ord(string.ascii_uppercase[0])  # A
LETTER_STOP: int = ord(string.ascii_uppercase[-1])  # Z
assert LETTER_STOP > LETTER_START
ALPHABET_LENGTH: int = LETTER_STOP - LETTER_START + 1
assert len(string.ascii_uppercase) == len(string.ascii_lowercase)
assert len(string.ascii_uppercase) == ALPHABET_LENGTH


def crypt(message: str, key: str, reverse=False) -> str:

    out: str = ''

    for key_counter, letter in enumerate(message):

        # Skip invalid characters in the key
        while (keyletter := key[key_counter % len(key)].upper()) not in string.ascii_uppercase:
            key_counter += 1

        if letter not in string.ascii_letters:
            out += letter  # Don't change invalid letters
            continue
        elif letter in string.ascii_uppercase:
            alphabet = string.ascii_uppercase
        elif letter in string.ascii_lowercase:
            alphabet = string.ascii_lowercase
        else:
            assert False, 'Letter not in any known alphabet'

        # Letter is in either .ascii_uppercase or .ascii_lowercase

        # TODO Kevin: Should A shift by 1 or 0 ?
        shift = (ord(keyletter) - LETTER_START) % ALPHABET_LENGTH

        if reverse:
            shift = -shift

        alph_range = range(ord(alphabet[0]), ord(alphabet[-1]))

        # (95 % alph_range.stop) + alph_range.start  # TODO Kevin: Modulus for both above and below range?
        encoded_letter = ord(letter) + shift
        if encoded_letter > alph_range.stop:
            encoded_letter -= ALPHABET_LENGTH
        elif encoded_letter < alph_range.start:
            encoded_letter += ALPHABET_LENGTH

        out += chr(encoded_letter)

    return out


if __name__ == '__main__':
    key = "Mystery box"
    encoded = crypt("hvad er det egentlig det er ", key)
    print(encoded)
    decoded = crypt(encoded, key, reverse=True)
    print(decoded)
