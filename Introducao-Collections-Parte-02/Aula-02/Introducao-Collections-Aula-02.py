usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
# set transforma em conjunto e elimina repetidos "set(assistiram)"

for usuario in set(assistiram):
    print(usuario)

'''
Recebi um erro ao utilizar & ou |, resolvi usando o set

>>> usuarios_data_science & usuarios_machine_learning
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    usuarios_data_science & usuarios_machine_learning
TypeError: unsupported operand type(s) for &: 'list' and 'list'


>>> set(usuarios_data_science) & set(usuarios_machine_learning)
{56, 23}

>>> usuarios
{1, 34, 5, 73, 12, 76, 17, 18}
>>> usuarios = frozenset(usuarios)
>>> type(usuarios)
<class 'frozenset'>
>>> usuarios.add(90)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    usuarios.add(90)
AttributeError: 'frozenset' object has no attribute 'add'

Usando o conjunto para remover strings duplicadas
>>> meu_texto
'Bem vindo, meu nome é Dennis, gosto muito do meu nome e tenho um cachorro, eu gosto muito de cachorro'
>>> meu_texto.split()
['Bem', 'vindo,', 'meu', 'nome', 'é', 'Dennis,', 'gosto', 'muito', 'do', 'meu', 'nome', 'e', 'tenho', 'um', 'cachorro,', 'eu', 'gosto', 'muito', 'de', 'cachorro']
>>> set(meu_texto.split())
{'muito', 'cachorro', 'vindo,', 'meu', 'e', 'tenho', 'nome', 'cachorro,', 'Dennis,', 'Bem', 'de', 'eu', 'um', 'é', 'do', 'gosto'}

Para adicionar um item a lista temos que usar a função "add" que é nativa do python para utilizar em conjuntos,
O Python nao permite a utilização da função "append" em conjuntos, o que adicionaria o elemento ao fim da lista.

O que aprendi nesta aula:

Modificar o conjunto em tempo real;
Congelar o conjunto com o frozenset;
Tirar a duplicidade de uma String;
Adicionar elementos no conjunto.
'''
