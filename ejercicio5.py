


def numero_par_impar(entero):

    """
    (numero) -> Str
    Diseña un programa que, dado un número entero, muestre por pantalla el mensaje «El numero es par.» cuando el número sea par y el mensaje «El numero es impar.» cuando sea impar.

    :param entero:
    :return: string

    >>> numero_par_impar(2)
    'El numero es par'
     >>> numero_par_impar(5)
    'El numero es impar'

    """

    mensaje = ""

    if (entero %2 == 0 ):
        mensaje = "Numero es par"
    else:
        mensaje = "El numero no es par"
        return  mensaje


print(numero_par_impar(2))