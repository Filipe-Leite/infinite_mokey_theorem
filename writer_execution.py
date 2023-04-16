#!pip install names

import names
from macaco import Macaco

texto_escolhido="ba"
tamanho_texto=len(texto_escolhido)

nome_macaco=names.get_full_name()+" Caesar"
caf_macaco=1

macaco_escritor = Macaco(nome_macaco,caf_macaco,1,texto_escolhido)

texto_tentativas=[]

#(texto_recebido,letras_espacos_digitados_tentativa,tempo_digitacao,texto_tentativas,tempo_transcorrido_total,n_letras_espacos_digitados)
#return (n_letras_espacos_digitados_total, texto_tentativas, tempo_transcorrido_total, texto_tentativas)

macaco_escritor.escreve_texto_aleatoriamente(texto_recebido=texto_escolhido,
                                             letras_espacos_digitados_tentativa="",
                                             texto_tentativas=texto_tentativas,
                                             tempo_transcorrido_total=0,
                                             n_letras_espacos_digitados_total=0)

print(macaco_escritor.nome_macaco)
print(macaco_escritor.caf_macaco)
print(macaco_escritor.tempo_digitacao_letra)
print(macaco_escritor.texto_recebido)
#print(macaco_escritor.texto_tentativas)
print(macaco_escritor.tempo_transcorrido_total)
print(macaco_escritor.n_letras_espacos_digitados_total)
print(macaco_escritor.texto_escrito)