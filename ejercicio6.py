def dobleImpar(entero):
    """
        (numero) -> mnumero, string
        :param entero:
        :return: mensaje resultante

        >>> dobleImpar(14)
        '14  es el doble de 7,  que es impar'
        >>> dobleImpar(20)
        '20 es un numero par'
        """
    if (entero / 2) % 2 != 0:
        return print(entero, "es el doble de ", entero / 2, " que es impar")

    else:
        return print(entero, "es un numero par")


num = int(input("Ingrese un numero: "))
dobleImpar(num)
