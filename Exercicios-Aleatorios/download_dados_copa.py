'''
Author: Dennis Henrique dos Santos Tavares
LinkedIn: https://www.linkedin.com/in/dennis-tavares/
Github: https://github.com/dhenriquedba
Date: 22/07/2020

O nosso primeiro programa consiste basicamente em duas funções de download
de dados. Uma delas leva em conta que o servidor responde o tamanho
da base cujo download queremos fazer, e a outra trata quando o servidor não
informa o tamanho. Esse download é feito via protocolo HTTP, usando recursos
da própria biblioteca padrão.
'''

import io
import sys
import urllib.request as request

BUFF_SIZE = 1024
def download_length(response, output, length):
	times = length // BUFF_SIZE
	if length % BUFF_SIZE > 0:
		times += 1
		for time in range(times):
			output.write(response.read(BUFF_SIZE))
			print("Downloaded %d" % (((time * BUFF_SIZE)/length)*100))

def download(response, output):
	total_downloaded = 0
	while True:
		data = response.read(BUFF_SIZE)
		total_downloaded += len(data)
		if not data:
			breakout_file.write(data)
			print('Downloaded {bytes}'.format(bytes=total_downloaded))
	
def main():
        response = request.urlopen(sys.argv[1])
        out_file = io.FileIO("saida.zip", mode="w")

        content_length = response.getheader('Content-Length')
        if content_length:
                length = int(content_length)
                download_length(response, out_file, length)
        else:
                download(response, out_file)

        reponse.close()
        out_file.close()
        print("Finished")
	
if __name__ == "__main__":
        main()
