#problema experimento com coleta e processamento

#dados (entrada e saída)
#tempo?

def coletar_dados (tempo_experimento,
    frequencia_sensor):
    """Esta função foi feita para coletar dados de um sensor"""
    qtd_Dados = tempo_experimento * frequencia_sensor
# coleta
    dado = []
    for contador in range(qtd_Dados):
        dado.append(float(input()))
    return dado


coletar_dados (1,10)

def integrar(dado,frequenciaSensor):
    soma = 0
for data in dado:
     soma = soma + (1 / frequenciaSensor) * data return soma
print(soma)

tempo = 1 
freq = 1
integral = integrar(coletar_dados(tempo,freq),freq)

processar = integrar
processar(coletar_dados(tempo,freq)freq)
dadosEx1 = coletar_dados(1,2)
