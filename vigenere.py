import string
from typing import Sequence

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


def decrypt_key_length(message: str) -> int:
    # TODO Kevin: Doesn't work yet

    shift_coincidences: list[int] = []
    for shift in range(2, len(message)):  # for shifted_message
        coincidences: int = 0
        for shifted_index in range(len(message) - shift):  # for char in shifted_message
            original_index = shifted_index + shift
            if message[shifted_index] == message[original_index]:
                coincidences += 1
        shift_coincidences.append(coincidences)

    coincidence_score: list[float] = []
    for step_size in range(2, len(shift_coincidences)):
        coincidence_sumlist: list[int] = []
        for coincidence_index in range(0, len(shift_coincidences), step_size):
            coincidence_cnt = shift_coincidences[coincidence_index]
            coincidence_sumlist.append(coincidence_cnt)
        coincidence_score.append(sum(coincidence_sumlist) / len(coincidence_sumlist))
    print(coincidence_score)
    key_length = max(coincidence_score)
    return key_length


if __name__ == '__main__':


    key = "coolio"

    # encoded = crypt("XWIGI EGI XLS XNTTW SU TRRVNTIMDR SCI XWEI LMAP TGIKICX CDYG HMHXTV JGSB GIPHXRV NSJV HXEGC ECH SCI XWEI LMAP TGIKICX CDYG VSKIGRBICX XWMH XW E ZTVN XQESGXPRI AIHWDR XD GIBIQIG TWEIRMPPAC JDV EIXPGZW YHMCK JGIFYTRRC ECEACHMH LLXGW GIFYXVT ASCKTV TPWHEVI SU IIMX MC DVSIG IS ERLXIKI FTXIIG GIHYAXH", key)
    encoded = crypt("hello hello", key)
    print(encoded)
    decoded = crypt(encoded, key, reverse=True)
    print(decoded)



    # decrypt_key_length("pretty")
    # decrypt_key_length(crypt("whatisitactuallythatitisinpeaspleasetellmeohprettypleaseiwouldliketoknowitverymuchsoyes", key))
    decrypt_key_length(crypt("ineedareallylongmessagesoiamjustgonnakeeponwritingsomerandomstuffwhoevencarewhatitisicertainlydontsodonteventrytomakesenseofthisisweartogodwhatisitactuallythatitisinpeaspleasetellmeohprettypleaseiwouldliketoknowitverymuchsoyes", key))
    # decrypt_key_length("VVHQWVVRMHUSGJG")

    raise SystemExit