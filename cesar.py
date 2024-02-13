#!/usr/bin/python

from __future__ import annotations

import string

LETTER_MIN: int = ord('A')
LETTER_MAX: int = ord('Z')
ALPHABET_LENGTH: int = LETTER_MAX - LETTER_MIN + 1

freq_norm = [0.64297, 0.11746, 0.21902, 0.33483, 1.00000, 0.17541,
                        0.15864, 0.47977, 0.54842, 0.01205, 0.06078, 0.31688, 0.18942,
                        0.53133, 0.59101, 0.15187, 0.00748, 0.47134, 0.49811, 0.71296,
                        0.21713, 0.07700, 0.18580, 0.01181, 0.15541, 0.00583]


def crypt(shift: int, instr: str, strip_invalid: bool = True) -> str:

    shift %= ALPHABET_LENGTH

    out: str = ''
    for letter in instr.upper():
        if letter in string.whitespace:
            out += letter
            continue

        if ord(letter) > LETTER_MAX or ord(letter) < LETTER_MIN:
            if strip_invalid:
                continue
            out += letter
            continue

        shifted: int = (ord(letter) + shift)
        if shifted > LETTER_MAX:
            shifted -= ALPHABET_LENGTH
        elif shifted < LETTER_MIN:
            shifted += ALPHABET_LENGTH
        out += chr(shifted)
        # out += chr((ord(letter % LETTER_MAX) + shift))
    return out

    # return ''.join(chr((ord(letter)+shift) % LETTER_MAX) for letter in instr if ord(letter) <= LETTER_MAX)


def frec_deviation(instr: str) -> float:

    instr = instr.upper()

    # TODO Kevin: ord() or string.ascii ?
    cnt_dict: dict[str, int] = {letter: 0 for letter in string.ascii_uppercase}
    frec_truth: dict[str, int] = dict(zip(string.ascii_uppercase, freq_norm))
    #norm_len = sum(1 for letter in instr if letter in string.ascii_uppercase)

    for letter in instr:
        try:
            cnt_dict[letter] += 1
        except KeyError:
            pass

    deviation = lambda *args: max(*args) - min(*args)

    divider: int = max(cnt_dict.items(), key=lambda keyval: keyval[1])[1]

    diff_dict: dict[str, int] = {letter: deviation((cnt/divider), frec_truth[letter]) for letter, cnt in cnt_dict.items()}
    diff_sum: float = sum(diff_dict.values())

    return diff_sum


def decrypt(instr: str) -> str:

    decrypt_dict: dict[str, float] = {(decrypted := crypt(i, instr)): frec_deviation(decrypted) for i in range(ALPHABET_LENGTH)}

    # Return the string with the lowest devition from standard english
    return min(decrypt_dict.items(), key=lambda x: x[1])[0]


if __name__ == '__main__':

    pairs: dict[int, str] = {
        7: "Aab vinder guld igen",
        16: "Programmering er sjovt",
        4: "H5PD rejser sig, når Per kommer ind af døren",
        20: "sygt, shit, bro",

    }

    for shift, instr in pairs.items():
        encrypted = crypt(shift, instr, strip_invalid=True)
        print(encrypted)
        print(crypt(-shift, encrypted, strip_invalid=True))

