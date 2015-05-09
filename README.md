humanizar
--------

Humanization utilities for spanish language. 
Utilidades de humanización para el idioma español.

- Convertidor de números a su escritura con palabras o valor en letras.
- Convertidor de fechas a su escritura en palabras usada en cartas

usage
-----

Integer humanization:

    >>> import humanizar
    >>> humanizar.number_to_words(12323)
    'Doce Mil Trescientos Ventitres'
    >>> humanizar.number_to_words(53625999567)
    'Cincuenta Y Tres Mil Seiscientos Venticinco Millones Novecientos Noventa Y Nueve Mil Quinientos Sesenta Y Siete'
    >>> humanizar.number_to_words(12322.233)
    'Doce Mil Trescientos Ventidos con Doscientos Treinta Y Tres'

Dates humanization
    
    >>> import humanizar
    >>> from datetime import date
    >>> humanizar.alosdias(date.today())
    u'9 d\xedas del mes de Mayo'
    >>> humanizar.fechacarta(date.today())
    'Mayo 9 de 2015'
    >>> humanizar.fechacarta('31/12/1923')
    'Diciembre 31 de 1923'
