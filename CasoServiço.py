import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as pescadorControl

#Definido as coisas que variam (populamente conhecidas como variaveis)

Espera = pescadorControl.Antecedent(np.arange(0,31,1),"Espera")
Satisfacao = pescadorControl.Antecedent(np.arange(0,11,1),"Satisfacao")

Qualidade = pescadorControl.Consequent(np.arange(0,11,1), "Qualidade")

#Faixas de valores 

Espera['curta'] = fuzz.trimf(Espera.universe,[0,5,10])
Espera['média'] = fuzz.trimf(Espera.universe,[10,15,20])
Espera['longa'] = fuzz.trimf(Espera.universe,[20,25,30])

Satisfacao['baixa'] = fuzz.trimf(Satisfacao.universe,[0,2.5,5]) 
Satisfacao['média'] = fuzz.trimf(Satisfacao.universe,[3,5,7]) 
Satisfacao['alta'] = fuzz.trimf(Satisfacao.universe,[5,7.5,10]) 

Qualidade['ruim'] = fuzz.trimf(Qualidade.universe,[0,2.5,5])
Qualidade['aceitavel'] = fuzz.trimf(Qualidade.universe,[3,5,7])
Qualidade['execelente'] = fuzz.trimf(Qualidade.universe,[5,7.5,10])

#Regras dos Amigos

Regra1 = pescadorControl.Rule(Espera['longa'] & Satisfacao['alta'], Qualidade['aceitavel'])
Regra2 = pescadorControl.Rule(Espera['curta'] & Satisfacao['baixa'], Qualidade['ruim'])

#Inicio da Simulação

Fim = pescadorControl.ControlSystem([Regra1, Regra2])
Simu = pescadorControl.ControlSystemSimulation(Fim)

Simu.input['Espera'] = 25
Simu.input['Satisfacao'] = 8
Simu.compute()
print(Simu.output['Qualidade'])

valor = Simu.output['Qualidade']

if valor < 5:
    categoria = 'ruim'
elif valor <= 7:
    categoria = 'aceitavel'
else:
    categoria = 'execelente'

print(categoria)


#5, deveria ser 6 , mds pq nada da certo nessa vida 