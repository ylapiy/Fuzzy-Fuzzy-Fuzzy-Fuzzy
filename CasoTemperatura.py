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
Pessoas["média"] = fuzz.trimf(Pessoas.universe, [5, 7.5, 10])
Pessoas["lotado"] = fuzz.trimf(Pessoas.universe, [10, 12.5, 15])

Saida["baixo"] = fuzz.trimf(Saida.universe, [0, 2.5, 5])
Saida["media"] = fuzz.trimf(Saida.universe, [3, 5, 7])
Saida["alto"] = fuzz.trimf(Saida.universe, [5, 7.5, 10])


# Regras dos Amigos

Regra1 = pescadorControl.Rule(Temperatura["frio"] & Pessoas["vazio"], Saida["media"])
Regra2 = pescadorControl.Rule(Temperatura["ameno"] & Pessoas["média"], Saida["alto"])
Regra3 = pescadorControl.Rule(Temperatura["quente"] & Pessoas["lotado"], Saida["baixo"])

# Inicio da Simulação

Fim = pescadorControl.ControlSystem([Regra1, Regra2, Regra3])
Simu = pescadorControl.ControlSystemSimulation(Fim)

Simu.input["Temperatura"] = 30
Simu.input["Pessoas"] = 10
Simu.compute()
print(Simu.output["Saida"])
