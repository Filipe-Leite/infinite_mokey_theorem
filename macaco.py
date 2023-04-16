import string
import random
import numpy as np

class Macaco:
    def __init__(self, nome_macaco, caf_macaco,tempo_digitacao_letra,texto_recebido):
        self.nome_macaco = nome_macaco
        self.caf_macaco = caf_macaco
        self.tempo_digitacao_letra=tempo_digitacao_letra
        self.texto_recebido = texto_recebido
        self.texto_tentativas = []
        self.tempo_transcorrido_total={"segundos passados": 0,
                                      "minutos passados": 0,
                                      "horas passadas": 0,
                                      "dias passados": 0,
                                      "meses passados": 0,
                                      "anos passados": 0,
                                      "seculos_passados": 0,
                                      "milenios_passados": 0}
        self.n_letras_espacos_digitados_total=0
        self.texto_escrito=""
        
    def escreve_letra(self):
        
        range_letra_espaco = string.ascii_lowercase+" "
        letra_espaco_digitado=random.choice(range_letra_espaco)
                                  
        return letra_espaco_digitado
    
    def escreve_texto_aleatoriamente(self,texto_recebido,
                                     letras_espacos_digitados_tentativa,
                                     texto_tentativas,
                                     tempo_transcorrido_total,
                                     n_letras_espacos_digitados_total):
        
        while letras_espacos_digitados_tentativa != texto_recebido:
            
            letra_espaco_digitado = self.escreve_letra()
            letras_espacos_digitados_tentativa += letra_espaco_digitado
            n_letras_espacos_digitados_tentativa = len(letras_espacos_digitados_tentativa)
            n_letras_espacos_digitados_total+=len(letra_espaco_digitado)

            self.tempo_transcorrido_total["segundos passados"]=self.tempo_transcorrido_total["segundos passados"]+self.tempo_digitacao_letra

            segundos_passados=self.tempo_transcorrido_total["segundos passados"]
            minutos_passados=segundos_passados/60
            horas_passadas=minutos_passados/60
            dias_passados=horas_passadas/24
            meses_passados=dias_passados/30
            anos_passados=meses_passados/12
            seculos_passados=anos_passados/100
            milenios_passados=seculos_passados/10
            
            tempo_transcorrido_total={"segundos passados": segundos_passados,
                                      "minutos passados": minutos_passados,
                                      "horas passadas": horas_passadas,
                                      "dias passados": dias_passados,
                                      "meses passados": meses_passados,
                                      "anos passados": anos_passados,
                                      "seculos_passados": seculos_passados,
                                      "milenios_passados": milenios_passados}
            
            if n_letras_espacos_digitados_tentativa == len(texto_recebido):

                texto_tentativas.append(letras_espacos_digitados_tentativa)

            if n_letras_espacos_digitados_tentativa == len(texto_recebido) and letras_espacos_digitados_tentativa!=texto_recebido:
                
                texto_tentativas.append(letras_espacos_digitados_tentativa)
            
                letras_espacos_digitados_tentativa=""

            self.texto_escrito=letras_espacos_digitados_tentativa
            self.letras_espacos_digitados_tentativa = letras_espacos_digitados_tentativa
            self.texto_tentativas=texto_tentativas
            self.tempo_transcorrido_total=tempo_transcorrido_total
            self.n_letras_espacos_digitados_total=n_letras_espacos_digitados_total