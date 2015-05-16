# -*- coding: utf-8 -*-
import math
import re

UNIDADES=(u"", u"primero", u"segundo", u"tercero",
        u"cuarto", u"quinto", u"sexto", u"séptimo", u"octavo", u"noveno")

DECENAS=(u"", u"décimo", u"vigésimo", u"trigésimo", u"cuadragésimo",
        u"quincuagésimo", u"sexagésimo", u"septuagésimo", u"octogésimo",
u"nonagésimo")

CENTENAS=(u"", u"centésimo", u"ducentésimo", u"tricentésimo",
        u" cuadringentésimo", u" quingentésimo", u" sexcentésimo",
u" septingentésimo",u" octingentésimo", u" noningentésimo")

def int_to_ordinal(num,genre='m'):
    num = int(num)
    if num > 1000 or num < 0:
        return 'Number must be less than 1000 and higher than 0'
    units = num % 10
    tens = int(math.floor(num/10))%10
    hundreds = int(math.floor(num/100))

    if(num>=100):
        ordinal_human = '%s %s %s' % (CENTENAS[hundreds],DECENAS[tens],UNIDADES[units])
    else:
        if(num>=10):
            ordinal_human = '%s %s' % (DECENAS[tens],UNIDADES[units])
        else:
            ordinal_human = UNIDADES[units]

    if genre == 'f':
        ordinal_human = re.sub(r'\b([\w]*)o\b',r'\1a',ordinal_human)


    return unicode(' '.join(ordinal_human.title().split()))
