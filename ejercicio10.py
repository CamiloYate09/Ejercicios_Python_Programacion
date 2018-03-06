# Introducir datos a la variable.


   """
    (num) -> str
    Escribe el mensaje 'El numero es negativo' cuando el numero es
    menor que cero
    >>> es_negativo(0.0)
    ''
    >>> desglose(100)
    'La cantidad de 100 euros se desglosa en 1 billete de 100 euros'
    >>> desglose(438)
    'La cantidad de 438 euros se desglosa en:
    2 billetes de 200 euros
    1 billete de 20 euros
    1 billete de 10 euros
    1 billete de 5 euros
    1 moneda de 2 euros
    1 moneda de 1 euros'
    :param num: el numero a evaluar
    :return: el mensaje resultante, con la cantidad de billetes y monedas disponibles para desglosar el valor del usuario
    """

def desglose(cantidad): 
    billetes_monedas=[500,200,100,50,20,10,5,2,1] 
    print ("La cantidad de " + str(cantidad) + " euros se desglosa en:") 
    for i in billetes_monedas: 
        if cantidad / i >= 1: 
            suelto = cantidad // i 
            print(str(suelto) + (" billete" if i > 2 else " moneda") + ('s' if (suelto) > 1 else '') + " de "+ str(i) + " euros") 
            cantidad %= i 


cantidad = int(input("Ingresa un valor "))
desglose(cantidad)
