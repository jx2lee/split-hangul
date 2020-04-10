import re
import char
from var import CHO, JOONG, JONG, JAMO, FIRST_HANGUL_UNICODE, LAST_HANGUL_UNICODE, NUM_JONG


# 한자/라틴 문자 range (by bluedisk)
FIRST_HANJA_UNICODE = 0x4E00
LAST_HANJA_UNICODE = 0x9FFF

FIRST_HANJA_EXT_A_UNICODE = 0x3400
LAST_HANJA_EXT_A_UNICODE = 0x4DBF

FIRST_LATIN1_UNICODE = 0x0000 # NUL
LAST_LATIN1_UNICODE = 0x00FF # 'ÿ'


def Is_hangul(phrase):
    for letter in phrase:
        code = ord(letter)
        if (code < FIRST_HANGUL_UNICODE or code > LAST_HANGUL_UNICODE) and not Is_jamo(letter):
            return False
    return True


def Is_jamo(letter):
    return letter in JAMO


def Is_hanja(phrase):
    for unicode_value in map(lambda letter:ord(letter), phrase):
        if ((unicode_value < FIRST_HANJA_UNICODE or unicode_value > LAST_HANJA_UNICODE) and
                (unicode_value < FIRST_HANJA_EXT_A_UNICODE or unicode_value > LAST_HANJA_EXT_A_UNICODE)):
            return False
    return True


def Is_latin(phrase):
    for unicode_value in map(lambda letter:ord(letter), phrase):
        if unicode_value < FIRST_LATIN1_UNICODE or unicode_value > LAST_LATIN1_UNICODE:
            return False
    return True


def Has_jongsung(letter):

    if len(letter) != 1:
        print('The target string must be one letter.')
    if not is_hangul(letter):
        print('The target string must be Hangul')
    
    code = char.Hangul_index(letter)
    return code % NUM_JONG > 0