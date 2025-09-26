import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as pescadorControl

# Definido as coisas que variam (populamente conhecidas como variaveis)

Distancia = pescadorControl.Antecedent(np.arange(0, 31, 1), "Distancia")
Curvatura = pescadorControl.Antecedent(np.arange(0, 46, 1), "Curvatura")

Velocidade = pescadorControl.Consequent(np.arange(0, 101, 1), "Velocidade")

# Faixas de valores

Distancia["perto"] = fuzz.trimf(Distancia.universe, [0, 0, 13])
Distancia["media"] = fuzz.trimf(Distancia.universe, [10, 15, 20])
Distancia["longe"] = fuzz.trimf(Distancia.universe, [17, 29, 29])

Curvatura["reta"] = fuzz.trimf(Curvatura.universe, [0, 0, 18])
Curvatura["leve"] = fuzz.trimf(Curvatura.universe, [10, 20, 30])
Curvatura["acentuada"] = fuzz.trimf(Curvatura.universe, [22, 44, 44])

Velocidade["baixa"] = fuzz.trimf(Velocidade.universe, [0, 0, 45])
Velocidade["media"] = fuzz.trimf(Velocidade.universe, [30, 50, 70])
Velocidade["alta"] = fuzz.trimf(Velocidade.universe, [55, 99, 99])

# Regras dos Amigos

Regras = [
    pescadorControl.Rule(Distancia["perto"] & Curvatura["reta"], Velocidade["media"]),
    pescadorControl.Rule(Distancia["perto"] & Curvatura["leve"], Velocidade["baixa"]),
    pescadorControl.Rule(
        Distancia["perto"] & Curvatura["acentuada"], Velocidade["baixa"]
    ),
    pescadorControl.Rule(Distancia["media"] & Curvatura["reta"], Velocidade["media"]),
    pescadorControl.Rule(Distancia["media"] & Curvatura["leve"], Velocidade["media"]),
    pescadorControl.Rule(
        Distancia["media"] & Curvatura["acentuada"], Velocidade["baixa"]
    ),
    pescadorControl.Rule(Distancia["longe"] & Curvatura["reta"], Velocidade["alta"]),
    pescadorControl.Rule(Distancia["longe"] & Curvatura["leve"], Velocidade["media"]),
    pescadorControl.Rule(
        Distancia["longe"] & Curvatura["acentuada"], Velocidade["baixa"]
    ),
]


# Inicio da Simulação

Fim = pescadorControl.ControlSystem(Regras)
Simu = pescadorControl.ControlSystemSimulation(Fim)

Simu.input["Distancia"] = 8
Simu.input["Curvatura"] = 40
Simu.compute()

# Saidas e printadas

print(Simu.output["Velocidade"])
maior_pertinencia = 0
categoria = ""

for termo in Velocidade.terms:
    pertinencia = fuzz.interp_membership(
        Velocidade.universe, Velocidade[termo].mf, Simu.output["Velocidade"]
    )
    print(f"perti: '{termo}': {pertinencia:.3f}")
    if pertinencia > maior_pertinencia:
        maior_pertinencia = pertinencia
        categoria = termo

print("É:", categoria)

Distancia.view(sim=Simu)
Curvatura.view(sim=Simu)
Velocidade.view(sim=Simu)
