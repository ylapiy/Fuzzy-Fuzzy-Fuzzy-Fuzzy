import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as pescadorControl

# Definido as coisas que variam (populamente conhecidas como variaveis)

Espera = pescadorControl.Antecedent(np.arange(0, 31, 1), "Espera")
Satisfacao = pescadorControl.Antecedent(np.arange(0, 11, 1), "Satisfacao")

Qualidade = pescadorControl.Consequent(np.arange(0, 11, 1), "Qualidade")

# Faixas de valores

Espera["curta"] = fuzz.trimf(Espera.universe, [0, 5, 10])
Espera["média"] = fuzz.trimf(Espera.universe, [10, 15, 20])
Espera["longa"] = fuzz.trimf(Espera.universe, [20, 25, 30])

Satisfacao["baixa"] = fuzz.trimf(Satisfacao.universe, [0, 2.5, 5])
Satisfacao["média"] = fuzz.trimf(Satisfacao.universe, [3, 5, 7])
Satisfacao["alta"] = fuzz.trimf(Satisfacao.universe, [5, 7.5, 10])

Qualidade["ruim"] = fuzz.trimf(Qualidade.universe, [0, 2.5, 5])
Qualidade["aceitavel"] = fuzz.trimf(Qualidade.universe, [3, 5, 7])
Qualidade["excelente"] = fuzz.trimf(Qualidade.universe, [5, 7.5, 10])

# Regras dos Amigos

Regras = [
    pescadorControl.Rule(Espera["curta"] & Satisfacao["baixa"], Qualidade["ruim"]),
    pescadorControl.Rule(Espera["curta"] & Satisfacao["média"], Qualidade["aceitavel"]),
    pescadorControl.Rule(Espera["curta"] & Satisfacao["alta"], Qualidade["excelente"]),
    pescadorControl.Rule(Espera["média"] & Satisfacao["baixa"], Qualidade["ruim"]),
    pescadorControl.Rule(Espera["média"] & Satisfacao["média"], Qualidade["aceitavel"]),
    pescadorControl.Rule(Espera["média"] & Satisfacao["alta"], Qualidade["excelente"]),
    pescadorControl.Rule(Espera["longa"] & Satisfacao["baixa"], Qualidade["ruim"]),
    pescadorControl.Rule(Espera["longa"] & Satisfacao["média"], Qualidade["ruim"]),
    pescadorControl.Rule(Espera["longa"] & Satisfacao["alta"], Qualidade["aceitavel"]),
]

# Inicio da Simulação

Fim = pescadorControl.ControlSystem(Regras)
Simu = pescadorControl.ControlSystemSimulation(Fim)

Simu.input["Espera"] = 25
Simu.input["Satisfacao"] = 8
Simu.compute()

# Saidas e printadas

print(Simu.output["Qualidade"])
maior_pertinencia = 0
categoria = ""

for termo in Qualidade.terms:
    pertinencia = fuzz.interp_membership(
        Qualidade.universe, Qualidade[termo].mf, Simu.output["Qualidade"]
    )
    print(f"perti: '{termo}': {pertinencia:.3f}")
    if pertinencia > maior_pertinencia:
        maior_pertinencia = pertinencia
        categoria = termo

print("É:", categoria)

Espera.view(sim=Simu)
Satisfacao.view(sim=Simu)
Qualidade.view(sim=Simu)

# 5, deveria ser 6 , mds pq nada da certo nessa vida
