#!/usr/bin/python

from __future__ import annotations

import string

LETTER_MIN: int = ord('A')
LETTER_MAX: int = ord('Z')


def crypt(shift: int, instr: str) -> str:
    out: str = ''
    for letter in instr.upper():
        if letter in string.whitespace:
            out += letter

        if ord(letter) > LETTER_MAX or ord(letter) < LETTER_MIN:
            continue

        shifted: int = (ord(letter) + shift)
        if shifted > LETTER_MAX:
            shifted -= LETTER_MAX - LETTER_MIN
        elif shifted < LETTER_MIN:
            shifted += LETTER_MAX - LETTER_MIN
        out += chr(shifted)
        # out += chr((ord(letter % LETTER_MAX) + shift))
    return out

    # return ''.join(chr((ord(letter)+shift) % LETTER_MAX) for letter in instr if ord(letter) <= LETTER_MAX)


if __name__ == '__main__':

    pairs: dict[int, str] = {
        7: "Aab vinder guld igen",
        16: "Programmering er sjovt",
        4: "H5PD rejser sig, når Per kommer ind af døren",
    }

    for shift, instr in pairs.items():
        encrypted = crypt(shift, instr)
        print(encrypted)
        print(crypt(-shift, encrypted))

