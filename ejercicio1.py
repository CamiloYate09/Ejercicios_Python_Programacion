




def es_negativo(num):
    """
    (num) -> str
    Escribe el mensaje 'El numero es negativo' cuando el numero es
    menor que cero
    >>> es_negativo(0.0)
    ''
    >>> es_negativo(-20.0)
    'El numero es negativo'
    >>> es_negativo(1.0)
    ''
    :param num: el numero a evaluar
    :return: el mensaje resultante
    """

    if (num < 0):
        return 'El numero es negativo'

    else:
        return 'Tu numero es positivo'



num = int(input("Ingresa un numero"))
es_negativo(num)