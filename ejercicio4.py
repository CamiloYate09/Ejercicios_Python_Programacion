import sys


   """
    (char) -> Mensaje
    Escribe el mensaje 'El numero es negativo' cuando el numero es
    menor que cero
    >>> caracter("(")
    'Esto es un paréntesis abierto'
    >>> caracter(")")
    'Esto es un paréntesis cerrado'
  
    :param char: recibe la funcion un caracter alfanumérico
    :return: el mensaje resultante si es paréntesis abierto o cerrado
    """


def caracter(entrada):
  if entrada == "(":
    print("Esto es un paréntesis abierto")
  elif entrada == ")":
    print("Esto es un paréntesis cerrado")
  else:
    print("No has escrito ningún parentesis")
    


entrada = str(input("Escribe un caracter alfanumérico "))

print(caracter(entrada))
