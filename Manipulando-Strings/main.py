class ExtratorArgumentoUrl:
    def __init__(self, url):
        if self.urlEhValida(url):
            self = url
        else:
            raise LookupError("Url inválida!!!")


#url = "https://butebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"
