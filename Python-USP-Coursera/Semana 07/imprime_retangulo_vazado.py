largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

if altura < 0:
	altura = altura * -1
if largura < 0:
	largura = largura * -1

alt = altura
larg = largura
while altura > 0:
    x = 0
    while x < largura:
        if altura == (alt) or x == (larg - 1) or altura == 1 or x == 0:
            print("#" , end = '')
        else: 
            print(" " , end = '')
        x+=1
    altura = altura - 1
    print()