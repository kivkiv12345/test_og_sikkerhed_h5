import string

LETTER_START: int = ord(string.ascii_uppercase[0])  # A
LETTER_STOP: int = ord(string.ascii_uppercase[-1])  # Z
assert LETTER_STOP > LETTER_START
ALPHABET_LENGTH: int = LETTER_STOP - LETTER_START + 1
assert len(string.ascii_uppercase) == len(string.ascii_lowercase)
assert len(string.ascii_uppercase) == ALPHABET_LENGTH


def crypt(message: str, key: str, reverse=False) -> str:

    out: str = ''

    # We can't increment key_counter with enumerate(),
    # because it doesn't account for -= 1 on invalid characters.
    key_counter: int = -1
    for letter in message:
        key_counter += 1

        if letter not in string.ascii_letters:
            out += letter  # Don't change invalid letters
            key_counter -= 1
            continue
        elif letter in string.ascii_uppercase:
            alphabet = string.ascii_uppercase
        elif letter in string.ascii_lowercase:
            alphabet = string.ascii_lowercase
        else:
            assert False, 'Letter not in any known alphabet'

        # Skip invalid characters in the key
        while (keyletter := key[key_counter % len(key)].upper()) not in string.ascii_uppercase:
            key_counter += 1

        # Letter is in either .ascii_uppercase or .ascii_lowercase

        # Official Vigenere cipher shifts by +0,
        # but I prefer shifting by +1.
        shift = (ord(keyletter) - LETTER_START + 0) % ALPHABET_LENGTH

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
    key = "pera"
    # encoded = crypt("XWIGI EGI XLS XNTTW SU TRRVNTIMDR SCI XWEI LMAP TGIKICX CDYG HMHXTV JGSB GIPHXRV NSJV HXEGC ECH SCI XWEI LMAP TGIKICX CDYG VSKIGRBICX XWMH XW E ZTVN XQESGXPRI AIHWDR XD GIBIQIG TWEIRMPPAC JDV EIXPGZW YHMCK JGIFYTRRC ECEACHMH LLXGW GIFYXVT ASCKTV TPWHEVI SU IIMX MC DVSIG IS ERLXIKI FTXIIG GIHYAXH", key)
    encoded = crypt("hello hello", key)
    print(encoded)
    decoded = crypt(encoded, key, reverse=True)
    print(decoded)
