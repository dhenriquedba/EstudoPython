# --------------------------------------------#
# Impressão de fatura do cliente			  #
# Criado por: Dennis Tavares                  #
# Data: 04/11/2019 - 16:00                    #
# --------------------------------------------#

NomeCliente = input("Digite o nome do cliente: ")
DiaVencimento = input("Digite o dia de vencimento: ")
MesVencimento = input("Digite o mês de vencimento: ")
ValorFatura = input("Digite o valor da fatura: ")

print("Olá,",NomeCliente)
print("A sua fatura com vencimento em",DiaVencimento, "de", MesVencimento, "no valor de R$",ValorFatura, "está fechada.")