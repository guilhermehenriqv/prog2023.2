dado =[89127,1298,902,3097,356]


soma = dado[0]+dado[1]+dado[2]+dado[3] #Isso seria uma soma de uma integral de forma mais premitiva
print (soma)
soma = 0
for contador in range (len(dado)): #in range é uma faixa de intervalo. No caso de 4 que é a quantidade de números a serem somados. Se colocar len n precisa mudar o número do parenteses
soma+= dado [contador] #+= soma acumulada, pode ser feito assim --> soma = soma + dado [contador]
print (soma)

2
dado =[89127,1298,902,3097,356]

3
tempoExperimento = 1 #s
frequenciaSensor = 10 #Hz
qtdDados = tempoExperimento*frequenciaSensor
print (qtdDados)
#coleta
dado = []
for contador in range (qtdDados):    
    dado.append(float(input()))

soma = 0
for contador in range (len(dado)):
    soma = soma + (1 / frequenciaSensor)*dado[contador] #é integral pq além de somar, multiplica-se pela frequência
print(soma)

4
dicionario= {
                "Brasil": [1,2,2,1,4,5,3],
                "EUA" : [3,4,56,3,6,4,2]
            }
for pais in dicionario:
    print (pais)
    print (dicionario[pais])
