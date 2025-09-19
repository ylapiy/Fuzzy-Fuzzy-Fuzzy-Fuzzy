import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as pescadorControl

#Definido as coisas que variam (populamente conhecidas como variaveis)

Cansaco = pescadorControl.Antecedent(np.arange(0,11,1),"Cansaco")
Sono = pescadorControl.Antecedent(np.arange(0,11,1),"Sono")

Acao = pescadorControl.Consequent(np.arange(0,11,1), "Acao")

#Faixas de valores 

Cansaco['baixo'] = fuzz.trimf(Cansaco.universe,[0,2.5,5])
Cansaco['medio'] = fuzz.trimf(Cansaco.universe,[3,5,7])
Cansaco['alto'] = fuzz.trimf(Cansaco.universe,[5,7.5,10])

Sono['pouco'] = fuzz.trimf(Sono.universe,[0,2.5,5])
Sono['adequado'] = fuzz.trimf(Sono.universe,[3,5,7])
Sono['muito'] = fuzz.trimf(Sono.universe,[5,7.5,10])

Acao['alerta'] = fuzz.trimf(Acao.universe,[0,2.5,5])
Acao['descanso'] = fuzz.trimf(Acao.universe,[3,5,7])
Acao['forcar_pausa'] = fuzz.trimf(Acao.universe,[5,7.5,10])

#Regras dos Amigos

Regra1 = pescadorControl.Rule(Cansaco['alto'] & Sono['pouco'], Acao['forcar_pausa'])
Regra2 = pescadorControl.Rule(Cansaco['baixo'] & Sono['adequado'], Acao['alerta'])

#Inicio da Simulação

Fim = pescadorControl.ControlSystem([Regra1, Regra2])
Simu = pescadorControl.ControlSystemSimulation(Fim)

Simu.input['Cansaco'] = 8
Simu.input['Sono'] = 4
Simu.compute()
print(Simu.output['Acao'])

valor = Simu.output['Acao']

if valor < 5:
    categoria = 'alerta'
elif valor <= 7:
    categoria = 'descanso'
else:
    categoria = 'forca_pausa'

print(categoria)

#Pausa Forçada, mas deu 7.5 ao inves de 8 hummmmmmmmmmmmmmmmmmmm