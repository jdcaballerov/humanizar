# -*- coding: utf-8 -*-
import locale
import datetime

from dateutil.parser import *

locale.setlocale(locale.LC_TIME, 'es_ES')

def alosdias(input_date):
    if isinstance(input_date,datetime.date):
        fecha=input_date
    else:
        fecha=parse(input_date)

    return '%s %s %s' % (fecha.strftime("%-d"),u'días del mes de',fecha.strftime("%B").title() )

def fechacarta(input_date):
    if isinstance(input_date,datetime.date):
        fecha=input_date
    else:
        fecha=parse(input_date)

    return '%s %s %s %s' % (fecha.strftime("%B").title(),fecha.strftime("%-d").title(),'de', fecha.strftime("%Y") )

