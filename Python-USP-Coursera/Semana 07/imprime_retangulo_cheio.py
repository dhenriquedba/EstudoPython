largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

if altura < 0:
	altura = altura * -1
if largura < 0:
	largura = largura * -1

cont_altura = 1
while cont_altura <= altura:
    cont_largura = 1
    cont_altura = cont_altura + 1
    while cont_largura <= largura:
        print ("#", end = "")
        cont_largura = cont_largura + 1
    print ()