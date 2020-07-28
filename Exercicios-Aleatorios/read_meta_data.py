# -*- coding: utf-8 -*-

import sys

entidades = {
	'Instituicao': [
		('IdInstituicao', 'bigint', 'Identificador da instituição-PK'),
		('IdTipoInstituicao', 'bigint', 'Id do tipo de instituição'),
		('NomInstituicao' 'varchar', 'Nome da instituição'),
		('NumCnpj', 'varchar', 'Número do CNPJ')
	]
}

def extract_entity_name(filename):
	return filename.split('.')[0]

def read_meta_data(path):
        data = open(path, "rt")
        meta_data = []
        for line in data:
                line_data = line.split('\t')
                meta_data.append((line_data[0],
                                  line_data[1],
                                  line_data[2]))
        data.close()
        return meta_data
