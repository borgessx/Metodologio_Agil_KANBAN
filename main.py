import processamento
import sys

arquivo = open("relatorio.txt", "w")

sys.stdout = arquivo

lista_princ = list()

processamento.add_lista(lista_princ)

media_princ = processamento.media(lista_princ)

processamento.media_personal(media_princ)

processamento.imprimir(lista_princ, processamento.media_personal(lista_princ))



arquivo.close()
