#!/usr/bin/python

from __future__ import annotations

import string

LETTER_MIN: int = ord('A')
LETTER_MAX: int = ord('Z')
ALPHABET_LENGTH: int = LETTER_MAX - LETTER_MIN + 1


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

