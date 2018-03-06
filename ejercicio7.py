"""
    (num,num) -> str
    Escribe el mensaje 'El numero es negativo' cuando el numero es
    menor que cero
    >>> mensajes(12.24)
    'El segundo numero es mayor que el cuadrado del primero.'
    >>> mensajes(1.3)
    'El segundo numero es menor que el cuadrado del primero'
    >>> mensajes(4.2)
    'El segundo numero es el cuadrado del primero'
    :param numero1, numero2: los numeros  a evaluar
    :return: el mensaje resultante de acuerdo a cada operacion
"""

def mensajes(numero1,numero2):
  if(numero1 == numero2*numero2 ):
    return ("El segundo numero es el cuadrado del primero")
  elif((numero1*numero1) < numero2):
    return ("El segundo numero es menor que el cuadrado del primero")
  elif((numero1*numero1) > numero2):
    return ("El segundo numero es mayor que el cuadrado del primero.")
  else:
    return ("Los numeros son iguales")
    
numero1 = int(input("Ingresa Tu primer numero"))
numero2 = int(input("Ingresa Tu segundo numero"))
print(mensajes(numero1,numero2))
