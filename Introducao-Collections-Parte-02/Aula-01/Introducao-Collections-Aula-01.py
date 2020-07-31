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
'''
