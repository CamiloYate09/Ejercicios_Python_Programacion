 """
    (num1,float,num3) -> str
    Escribe el mensaje 'Cuando Pasen", años, " Años con un ", interes, "de interes usted habra ganado", resultado, "Euros"
    >>> intereses_euros(5000.8.5,10)
    'Cuando Pasen 10  Años con un  8.5 de interes usted habra ganado 11305 Euros'
    
    >>> intereses_euros(2000.4.5,5)
    'Cuando Pasen 5  Años con un  4.5 de interes usted habra ganado 2492 Euros'
   
    :param num, floatante: el numero de euros, intereses, tiempo
    :return: el mensaje resultante
    """



def principal():
    euros = int(input("Cuantos Euros"))
    interes = float(input("Cuanto interes"))
    anos = int(input("Cuantos años"))
    print("")
    resultado = intereses_euros(euros, interes, anos)
    print("Cuando Pasen", anos, " Años con un ", interes, "de interes usted habra ganado", resultado, "Euros")


def intereses_euros(euros, intereses, cantidad_anos):
    total = round(euros * ((1 + intereses / 100) ** cantidad_anos))
    return total


principal()
