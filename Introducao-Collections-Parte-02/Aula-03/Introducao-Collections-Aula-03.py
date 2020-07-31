usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
# set transforma em conjunto e elimina repetidos "set(assistiram)"

for usuario in set(assistiram):
    print(usuario)

'''
>>> aparicoes = {"Dennis" : 1, "cachorro" : 2, "nome" : 2, "vindo" : 1}
>>> type(aparicoes)
<class 'dict'>
>>> aparicoes["Dennis"]
1
>>> aparicoes["cachorro"]
2
>>> aparicoes["xpto"]
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    aparicoes["xpto"]
KeyError: 'xpto'
>>> aparicoes.get("xpto", 0)
0
>>> aparicoes.get("cachorro", 0)
2
>>> aparicoes["Carlos"] = 1
>>> aparicoes
{'Dennis': 1, 'cachorro': 2, 'nome': 2, 'vindo': 1, 'Carlos': 1}
>>> aparicoes["Carlos"] = 2
>>> aparicoes
{'Dennis': 1, 'cachorro': 2, 'nome': 2, 'vindo': 1, 'Carlos': 2}
>>> del aparicoes["Carlos"]
>>> aparicoes
{'Dennis': 1, 'cachorro': 2, 'nome': 2, 'vindo': 1}
>>> "cachorro" in aparicoes
True
>>> "Carlos" in aparicoes
False
>>> for elemento in aparicoes:
	print(elemento)

	
Dennis
cachorro
nome
vindo
>>> for elemento in aparicoes.keys():
	print(elemento)

	
Dennis
cachorro
nome
vindo
>>> for elemento in aparicoes.values():
	print(elemento)

	
1
2
2
1
>>> for elemento in aparicoes.keys():
	valor = aparicoes(elemento)
	print(elemento, valor)

	
Traceback (most recent call last):
  File "<pyshell#78>", line 2, in <module>
    valor = aparicoes(elemento)
TypeError: 'dict' object is not callable

>>> for elemento in aparicoes.keys(): 
	valor = aparicoes[elemento] # o erro estava aqui
	print(elemento, valor)

	
Dennis 1
cachorro 2
nome 2
vindo 1
>>> for elemento in aparicoes.items():
	print(elemento)

	
('Dennis', 1)
('cachorro', 2)
('nome', 2)
('vindo', 1)
>>> for chave, valor in aparicoes.items():
	print(chave, "=", valor)

	
Dennis = 1
cachorro = 2
nome = 2
vindo = 1
>>> "palavra {}".format(chave) for chave in aparicoes.keys():
	
SyntaxError: invalid syntax

>>> ["palavra {}".format(chave) for chave in aparicoes.keys()]
['palavra Dennis', 'palavra cachorro', 'palavra nome', 'palavra vindo']

Observação: Para verificar se um item está contido um dicionario, utilizar a função GET.

O que aprendi nesta aula:

O que é um dicionário;
Verificar se o elemento está dentro do dicionário;
Utilizar o get para verificação;
Criar um dicionário a partir do dict;
Adicionar um elemento no dicionário;
Remover um elemento do dicionário;
Mostrar os elementos dentro do dicionário;
Usar a função keys para pegar as chaves;
Usar a função values para pegar os valores;
Percorrer linha a linha com a função items.
'''
