
 """
    (num) -> str
    Escribe el mensaje 'Tu numero ingresado en la funcion es primo o no es primo '
    >>> es_negativo(0.0)
    ''
    >>> es_primo(10)
    '('Tu numero', 10, 'Es primo')'
    >>> es_primo(3)
    '('Tu numero', 3, 'No es primo')'
    :param num: el numero a evaluar
    :return: el mensaje resultante es primo o no es primo 
    """




def es_primo(numero):
  if((numero % 2) == 0):
    return ("Tu numero", numero, "Es primo")
  else:
    return ("Tu numero", numero, "No es primo")
      
  
numero = int(input("Ingrese un numero"))
print(es_primo(numero))
