# Introducir datos a la variable.
N = int(raw_input('Ingresar Capital: '))

# Variables Billetes.
a = 500
b = 200
c = 100
d = 50
e = 20
f = 10
g = 5

# Variables Monedas.
h = 2
i = 1

numero_de_billetes_500 = N / 500
N = N % 500

numero_de_billetes_200 = N / 200
N = N % 200

numero_de_billetes_100 = N / 100
N = N % 100

numero_de_billetes_50 = N / 50
N = N % 50

numero_de_billetes_20 = N / 20
N = N % 20

numero_de_billetes_10 = N / 10
N = N % 10

numero_de_billetes_5 = N / 5
N = N % 5

numero_de_billetes_2 = N / 2
N = N % 2

numero_de_billetes_1 = N / 1
N = N % 1
