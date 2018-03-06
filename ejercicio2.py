def es_positivo(num):
    """
    (num) -> str
    Escribe el mensaje 'El numero es positivo' cuando el numero es
    mayor o igual que cero
    >>> es_positivo(0)
    'El numero es positivo'
    >>> es_positivo(-20)
    ''
    >>> es_positivo(10)
    'El numero es positivo'
    :param num: el numero a evaluar
    :return: el mensaje resultante
    """
    salida = ''
    if num >= 0:
        salida = 'El numero es positivo'
    return salida
