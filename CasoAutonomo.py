import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as pescadorControl

#Definido as coisas que variam (populamente conhecidas como variaveis)

Distancia = pescadorControl.Antecedent(np.arange(0,31,1),"Distancia")     
Curvatura = pescadorControl.Antecedent(np.arange(0,46,1),"Curvatura")       

Velocidade = pescadorControl.Consequent(np.arange(0,101,1), "Velocidade")

#Faixas de valores 

Distancia['perto'] = fuzz.trimf(Distancia.universe,[0,5,10])
Distancia['media'] = fuzz.trimf(Distancia.universe,[9,15,20])
Distancia['longe'] = fuzz.trimf(Distancia.universe,[19,25,30])

Curvatura['reta'] = fuzz.trimf(Curvatura.universe,[0,7.5,15])
Curvatura['leve'] = fuzz.trimf(Curvatura.universe,[15,22.5,30])
Curvatura['acentuada'] = fuzz.trimf(Curvatura.universe,[30,37.5,45])

Velocidade['baixa'] = fuzz.trimf(Velocidade.universe,[0,20,40])
Velocidade['media'] = fuzz.trimf(Velocidade.universe,[30,50,70])
Velocidade['alta'] = fuzz.trimf(Velocidade.universe,[60,80,100])

#Regras dos Amigos

Regra1 = pescadorControl.Rule(Distancia['perto'] & Curvatura['acentuada'], Velocidade['baixa'])
Regra2 = pescadorControl.Rule(Distancia['longe'] & Curvatura['reta'], Velocidade['alta'])

#Inicio da Simulação

Fim = pescadorControl.ControlSystem([Regra1, Regra2])
Simu = pescadorControl.ControlSystemSimulation(Fim)

Simu.input['Distancia'] = 8
Simu.input['Curvatura'] = 40
Simu.compute()
print(Simu.output['Velocidade'])

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as pescadorControl

#Definido as coisas que variam (populamente conhecidas como variaveis)

Distancia = pescadorControl.Antecedent(np.arange(0,31,1),"Distancia")     
Curvatura = pescadorControl.Antecedent(np.arange(0,46,1),"Curvatura")       

Velocidade = pescadorControl.Consequent(np.arange(0,101,1), "Velocidade")

#Faixas de valores 

Distancia['perto'] = fuzz.trimf(Distancia.universe,[0,5,10])
Distancia['media'] = fuzz.trimf(Distancia.universe,[9,15,20])
Distancia['longe'] = fuzz.trimf(Distancia.universe,[19,25,30])

Curvatura['reta'] = fuzz.trimf(Curvatura.universe,[0,7.5,15])
Curvatura['leve'] = fuzz.trimf(Curvatura.universe,[15,22.5,30])
Curvatura['acentuada'] = fuzz.trimf(Curvatura.universe,[30,37.5,45])

Velocidade['baixa'] = fuzz.trimf(Velocidade.universe,[0,20,40])
Velocidade['media'] = fuzz.trimf(Velocidade.universe,[30,50,70])
Velocidade['alta'] = fuzz.trimf(Velocidade.universe,[60,80,100])

#Regras dos Amigos

Regra1 = pescadorControl.Rule(Distancia['perto'] & Curvatura['acentuada'], Velocidade['baixa'])
Regra2 = pescadorControl.Rule(Distancia['longe'] & Curvatura['reta'], Velocidade['alta'])

#Inicio da Simulação

Fim = pescadorControl.ControlSystem([Regra1, Regra2])
Simu = pescadorControl.ControlSystemSimulation(Fim)

Simu.input['Distancia'] = 8
Simu.input['Curvatura'] = 40
Simu.compute()
print(Simu.output['Velocidade'])

valor = Simu.output['Velocidade']

if valor <= 40:
    categoria = 'baixa'
elif valor <= 70:
    categoria = 'media'
else:
    categoria = 'alta'

print(categoria)


