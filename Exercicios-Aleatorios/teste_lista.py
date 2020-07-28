lista = ['impostos', 'salarios', 'altos', 'baixos']
contador = 0

while contador < 4:
	print(lista[contador])
	contador = contador + 1
	if contador == 4:
		contador = 0
		print("O contador zerou.")
		break