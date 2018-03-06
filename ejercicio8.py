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
