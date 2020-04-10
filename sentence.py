from var import CHO, JOONG, JONG
import ischecker
import char

JONG_COMP = {
    u'ㄱ': {
        u'ㄱ': u'ㄲ',
        u'ㅅ': u'ㄳ',
    },
    u'ㄴ': {
        u'ㅈ': u'ㄵ',
        u'ㅎ': u'ㄶ',
    },
    u'ㄹ': {
        u'ㄱ': u'ㄺ',
        u'ㅁ': u'ㄻ',
        u'ㅂ': u'ㄼ',
        u'ㅅ': u'ㄽ',
        u'ㅌ': u'ㄾ',
        u'ㅍ': u'ㄿ',
        u'ㅎ': u'ㅀ',
    }
}
DEFAULT_COMPOSE_CODE = u'鰅'


def Decompose(text, latin_filter=True, compose_code=DEFAULT_COMPOSE_CODE):
    
    result=u""

    for c in list(text):
        if ischecker.Is_hangul(c):

            if ischecker.Is_jamo(c):
                result = result + c + compose_code
            else:
                result = result + "".join(char.Decompose(c)) + compose_code

        else:
            if latin_filter:    # 한글 외엔 Latin1 범위까지만 포함 (한글+영어)
                if ischecker.Is_latin(c):
                    result = result + c
            else:
                result = result + c

    return result


STATUS_CHO = 0
STATUS_JOONG = 1
STATUS_JONG1 = 2
STATUS_JONG2 = 3


def Compose(text, compose_code=DEFAULT_COMPOSE_CODE):
    res_text = u""

    status = STATUS_CHO

    for c in text:

        if status == STATUS_CHO:

            if c in CHO:
                chosung = c
                status = STATUS_JOONG
            else:
                if c != compose_code:

                    res_text = res_text + c

        elif status == STATUS_JOONG:

            if c != compose_code and c in JOONG:
                joongsung = c
                status = STATUS_JONG1
            else:
                res_text = res_text + chosung

                if c in CHO:
                    chosung = c
                    status = STATUS_JOONG
                else:
                    if c != compose_code:

                        res_text = res_text + c
                    status = STATUS_CHO

        elif status == STATUS_JONG1:

            if c != compose_code and c in JONG:
                jongsung = c

                if c in JONG_COMP:
                    status = STATUS_JONG2
                else:
                    res_text = res_text + char.Compose(chosung, joongsung, jongsung)
                    status = STATUS_CHO

            else:
                res_text = res_text + char.Compose(chosung, joongsung)

                if c in CHO:
                    chosung = c
                    status = STATUS_JOONG
                else:
                    if c != compose_code:

                        res_text = res_text + c

                    status = STATUS_CHO

        elif status == STATUS_JONG2:

            if c != compose_code and c in JONG_COMP[jongsung]:
                jongsung = JONG_COMP[jongsung][c]
                c = compose_code

            res_text = res_text + char.Compose(chosung, joongsung, jongsung)

            if c != compose_code:

                res_text = res_text + c

            status = STATUS_CHO

    return res_text