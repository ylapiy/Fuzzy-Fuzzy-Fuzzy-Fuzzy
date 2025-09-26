import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as pescadorControl

# Definido as coisas que variam (populamente conhecidas como variaveis)

Temperatura = pescadorControl.Antecedent(np.arange(0, 31, 1), "Temperatura")
Pessoas = pescadorControl.Antecedent(np.arange(0, 16, 1), "Pessoas")

Saida = pescadorControl.Consequent(np.arange(0, 11, 1), "Saida")

# Faixas de valores

Temperatura["frio"] = fuzz.trimf(Temperatura.universe, [0, 5, 10])
Temperatura["ameno"] = fuzz.trimf(Temperatura.universe, [10, 15, 20])
Temperatura["quente"] = fuzz.trimf(Temperatura.universe, [20, 25, 30])

Pessoas["vazio"] = fuzz.trimf(Pessoas.universe, [0, 2.5, 5])
Pessoas["media"] = fuzz.trimf(Pessoas.universe, [5, 7.5, 10])
Pessoas["lotado"] = fuzz.trimf(Pessoas.universe, [10, 12.5, 15])

Saida["baixo"] = fuzz.trimf(Saida.universe, [0, 2.5, 5])
Saida["media"] = fuzz.trimf(Saida.universe, [3, 5, 7])
Saida["alto"] = fuzz.trimf(Saida.universe, [5, 7.5, 10])


# Regras dos Amigos
Regras = [
    pescadorControl.Rule(Temperatura["frio"] & Pessoas["vazio"], Saida["media"]),
    pescadorControl.Rule(Temperatura["frio"] & Pessoas["media"], Saida["alto"]),
    pescadorControl.Rule(Temperatura["frio"] & Pessoas["lotado"], Saida["alto"]),
    pescadorControl.Rule(Temperatura["ameno"] & Pessoas["vazio"], Saida["baixo"]),
    pescadorControl.Rule(Temperatura["ameno"] & Pessoas["media"], Saida["alto"]),
    pescadorControl.Rule(Temperatura["ameno"] & Pessoas["lotado"], Saida["media"]),
    pescadorControl.Rule(Temperatura["quente"] & Pessoas["vazio"], Saida["baixo"]),
    pescadorControl.Rule(Temperatura["quente"] & Pessoas["media"], Saida["media"]),
    pescadorControl.Rule(Temperatura["quente"] & Pessoas["lotado"], Saida["baixo"]),
]
# Inicio da Simulação

Fim = pescadorControl.ControlSystem(Regras)

Simu = pescadorControl.ControlSystemSimulation(Fim)

Simu.input["Temperatura"] = 30
Simu.input["Pessoas"] = 10
Simu.compute()

# Saidas e printadas

print(Simu.output['Saida'])
maior_pertinencia = 0
categoria = ""

for termo in Saida.terms:
    pertinencia = fuzz.interp_membership(
        Qualidade.universe, Saida[termo].mf, Simu.output["Saida"]
    )
    print(f"perti: '{termo}': {pertinencia:.3f}")
    if pertinencia > maior_pertinencia:
        maior_pertinencia = pertinencia
        categoria = termo

print("É:", categoria)

Temperatura.view(sim=Simu)
Pessoas.view(sim=Simu)
Saida.view(sim=Simu)
