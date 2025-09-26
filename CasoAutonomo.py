import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as pescadorControl

# Definido as coisas que variam (populamente conhecidas como variaveis)

Distancia = pescadorControl.Antecedent(np.arange(0, 31, 1), "Distancia")
Curvatura = pescadorControl.Antecedent(np.arange(0, 46, 1), "Curvatura")

Velocidade = pescadorControl.Consequent(np.arange(0, 101, 1), "Velocidade")

# Faixas de valores

Distancia["perto"] = fuzz.trimf(Distancia.universe, [0, 5, 10])
Distancia["media"] = fuzz.trimf(Distancia.universe, [9, 15, 20])
Distancia["longe"] = fuzz.trimf(Distancia.universe, [19, 25, 30])

Curvatura["reta"] = fuzz.trimf(Curvatura.universe, [0, 7.5, 15])
Curvatura["leve"] = fuzz.trimf(Curvatura.universe, [15, 22.5, 30])
Curvatura["acentuada"] = fuzz.trimf(Curvatura.universe, [30, 37.5, 45])

Velocidade["baixa"] = fuzz.trimf(Velocidade.universe, [0, 20, 40])
Velocidade["media"] = fuzz.trimf(Velocidade.universe, [30, 50, 70])
Velocidade["alta"] = fuzz.trimf(Velocidade.universe, [60, 80, 100])

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
