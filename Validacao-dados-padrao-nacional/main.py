from cpf_cnpj import Documento
from validate_docbr import CNPJ
from telefonesBR import TelefonesBr
import re
from datetime import datetime, timedelta
from datas_br import DatasBr
import requests
from acesso_cep import BuscaEndereco


#cpf_um = Cpf("15316264754")
#print(cpf_um)

#exemplo_cnpj = "35379838000112"
exemplo_cpf = "22417874857"

#cnpj = CNPJ()
#print(cnpj.validate(exemplo_cnpj))
documento = Documento.cria_documento(exemplo_cpf)
print(documento)

telefone = "552126481234"
telefone_objeto = TelefonesBr(telefone)

#padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
#resposta = re.search(padrao,telefone)
#print(resposta.group())

print(telefone_objeto)

hoje = DatasBr()
print(hoje.tempo_cadastro())

cep = "25800320"
objeto_cep = BuscaEndereco(cep)

#r = requests.get("https://viacep.com.br/ws/01001000/json/")
#print(r.text)

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)