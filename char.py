# -*- coding: utf-8 -*-
from var import CHO, JOONG, JONG, FIRST_HANGUL_UNICODE, NUM_CHO, NUM_JOONG, NUM_JONG, ENG_KOR_SUBSTITUENT
from exception import NotHangulException, NotLetterException
import ischecker

# Externel Library
from six import unichr
import string


def Compose(chosung, joongsung, jongsung=u''):

    if jongsung is None:
        jongsung = u''

    try:
        chosung_index = CHO.index(chosung)
        joongsung_index = JOONG.index(joongsung)
        jongsung_index = JONG.index(jongsung)
        
    except Exception:
        raise NotHangulException('한글 index가 유효하지 않습니다')

    return unichr(0xAC00 + chosung_index * NUM_JOONG * NUM_JONG +
                  joongsung_index * NUM_JONG + jongsung_index)


def Hangul_index(letter):
    return ord(letter) - FIRST_HANGUL_UNICODE


def Decompose_index(code):
    jong = int(code % NUM_JONG)
    code /= NUM_JONG
    joong = int(code % NUM_JOONG)
    code /= NUM_JOONG
    cho = int(code)

    return cho, joong, jong


def Decompose(letter):

    if len(letter) < 1:
        raise NotLetterException('')
    elif not ischecker.Is_hangul(letter):
        raise NotHangulException('')

    if letter in CHO:
        return letter, '', ''

    if letter in JOONG:
        return '', letter, ''

    if letter in JONG:
        return '', '', letter

    code = Hangul_index(letter)
    cho, joong, jong = Decompose_index(code)

    if cho < 0:
        cho = 0

    try:
        return CHO[cho], JOONG[joong], JONG[jong]

    except:
        print("%d / %d  / %d"%(cho, joong, jong))
        print("%s / %s " %( JOONG[joong].encode("utf8"), JONG[jong].encode('utf8')))
        raise Exception()

def Get_substituent_of(letter):
    return ENG_KOR_SUBSTITUENT.get(letter.upper(), '')