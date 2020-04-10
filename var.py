# HANGUL UNICODE VARIABLES
# Code = 0xAC00 + (초성 index * NUM_JOONG * NUM_JONG) + (중성 index * NUM_JONG) + (종성 index)

CHO = ( u'ㄱ', u'ㄲ', u'ㄴ', u'ㄷ', u'ㄸ', u'ㄹ', u'ㅁ', u'ㅂ', u'ㅃ', u'ㅅ',
        u'ㅆ', u'ㅇ', u'ㅈ', u'ㅉ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ' )
JOONG = ( u'ㅏ', u'ㅐ', u'ㅑ', u'ㅒ', u'ㅓ', u'ㅔ', u'ㅕ', u'ㅖ', u'ㅗ', u'ㅘ',
          u'ㅙ', u'ㅚ', u'ㅛ', u'ㅜ', u'ㅝ', u'ㅞ', u'ㅟ', u'ㅠ', u'ㅡ', u'ㅢ', u'ㅣ' )
JONG = ( u'', u'ㄱ', u'ㄲ', u'ㄳ', u'ㄴ', u'ㄵ', u'ㄶ', u'ㄷ', u'ㄹ', u'ㄺ',
         u'ㄻ', u'ㄼ', u'ㄽ', u'ㄾ', u'ㄿ', u'ㅀ', u'ㅁ', u'ㅂ', u'ㅄ', u'ㅅ',
         u'ㅆ', u'ㅇ', u'ㅈ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ' )

JAMO = CHO + JOONG + JONG[1:]

NUM_CHO = 19
NUM_JOONG = 21
NUM_JONG = 28

FIRST_HANGUL_UNICODE = 0xAC00  # '가'
LAST_HANGUL_UNICODE = 0xD7A3  # '힣'
ENG_KOR_SUBSTITUENT = { 'B': 'ㅂ', 'C':'ㄱ', 'K':'ㄱ', 'L':'ㄹ', 'M':'ㅁ', 'N':'ㄴ', 'R':'ㄹ', 'T':'ㅅ'}