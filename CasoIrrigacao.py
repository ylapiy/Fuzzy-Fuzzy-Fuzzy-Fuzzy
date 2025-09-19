import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as pescadorControl

#Definido as coisas que variam (populamente conhecidas como variaveis)

Umidade = pescadorControl.Antecedent(np.arange(0,101,1),"Umidade")
Temperatura = pescadorControl.Antecedent(np.arange(0,41,1),"Temperatura")

Irrigacao = pescadorControl.Consequent(np.arange(0,11,1), "Irrigacao")

#Faixas de valores 

Umidade['seca'] = fuzz.trimf(Umidade.universe,[0,25,50])
Umidade['media'] = fuzz.trimf(Umidade.universe,[25,50,75])
Umidade['umida'] = fuzz.trimf(Umidade.universe,[50,75,100])

Temperatura['baixa'] = fuzz.trimf(Temperatura.universe,[0,10,20])
Temperatura['media'] = fuzz.trimf(Temperatura.universe,[10,20,30])
Temperatura['alta'] = fuzz.trimf(Temperatura.universe,[20,30,40])

Irrigacao['pouca'] = fuzz.trimf(Irrigacao.universe,[0,2.5,5])
Irrigacao['moderada'] = fuzz.trimf(Irrigacao.universe,[3,5,7])
Irrigacao['intensa'] = fuzz.trimf(Irrigacao.universe,[5,7.5,10])

#Regras dos Amigos

Regra1 = pescadorControl.Rule(Umidade['seca'] & Temperatura['alta'], Irrigacao['intensa'])

#Inicio da Simulação

Fim = pescadorControl.ControlSystem([Regra1])
Simu = pescadorControl.ControlSystemSimulation(Fim)

Simu.input['Umidade'] = 30
Simu.input['Temperatura'] = 35
Simu.compute()
print(Simu.output['Irrigacao'])

valor = Simu.output['Irrigacao']

if valor <= 5:
    categoria = 'pouca'
elif valor <= 7:
    categoria = 'moderada'
else:
    categoria = 'intensa'

print(categoria)


#7.5 acho que ta bom ne -> Intensa