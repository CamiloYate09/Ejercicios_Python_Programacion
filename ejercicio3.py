def el_mayor(edad_1, edad_2):
    """
    (num,num) -> str
    retorna quien es el mayor de las dos edades
    >>> el_mayor(10,10)
    'los dos son igual de jovenes'
    >>> el_mayor(5,10)
    'El primero es el mas joven'
    >>> el_mayor(10,5)
    'El segundo es el mas joven'
    :param edad_1: la edad de la primera persona
    :param edad_2: la edad de la segunda persona
    :return: mensaje con el dato del mas joven
    """
    salida = ''
    if edad_1 > edad_2:
        salida = 'El segundo es el mas joven'
    elif edad_1 < edad_2:
        salida = 'El primero es el mas joven'
    else:
        salida = 'los dos son igual de jovenes'
    return salida
