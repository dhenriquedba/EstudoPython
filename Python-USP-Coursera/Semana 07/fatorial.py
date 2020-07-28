n = int(input("Digite um numero inteiro positivo: "))
while n >= 0:
	n_fat = 1
	while n > 1:
		n_fat = n_fat * n
		n = n - 1
	print(n_fat)
	n = int(input("Digite um numero inteiro: "))