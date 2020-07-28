def MinMax(temperaturas):
	print("A menor temperatura do mês foi: ", minimo(temperaturas), "C.")
	print("A maior temperatura do mês foi: ", maximo(temperaturas), "C.")
	
def maximo(temps):
	max = temps[0]
	i = 1
	while i < len(temps):
		if temps[i] > max:
			max = temps[i]
		i = i + 1
	return max
	
def minimo(temps):
	min = temps[0]
	i = 1
	while i < len(temps):
		if temps[i] < min:
			min = temps[i]
		i = i + 1
	return min
	
	
def teste_pontual(temp, valor_esperado):
	valor_calculado = minima(temp)
	if valor_calculado != valor_esperado:
		print("Valor errado para array ", temp)
		print("Valor esperado ", valor_esperado, ". Valor calculado: ", valor_calculado)
	
def testa_minima():
	print("Iniciando os testes")
	teste_pontual = ([0], 0)
	teste_pontual = ([0, 0, 0, 0, 0, 0], 0)
	teste_pontual = ([0, 1, 2, 3, 4, 5, 6, 8, 9, 10], 0)
	teste_pontual = ([30, 18, 27, 23, 24, 28, 30, 33, 29, 26, 39, 25, 22, 26, 27, 29, 35, 34], 22)
	teste_pontual = ([-15, -12, 0, 20, 30], -15)
	print("Finalizando os testes")
