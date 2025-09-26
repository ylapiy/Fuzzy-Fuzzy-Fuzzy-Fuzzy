import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as pescadorControl


Regras = [
    pescadorControl.Rule(Umidade["seca"] & Temperatura["baixa"], Irrigacao["moderada"]),
    pescadorControl.Rule(Umidade["seca"] & Temperatura["media"], Irrigacao["intensa"]),
    pescadorControl.Rule(Umidade["seca"] & Temperatura["alta"], Irrigacao["intensa"]),
    pescadorControl.Rule(Umidade["media"] & Temperatura["baixa"], Irrigacao["pouca"]),
    pescadorControl.Rule(Umidade["media"] & Temperatura["media"], Irrigacao["moderada"]),
    pescadorControl.Rule(Umidade["media"] & Temperatura["alta"], Irrigacao["intensa"]),
    pescadorControl.Rule(Umidade["umida"] & Temperatura["baixa"], Irrigacao["pouca"]),
    pescadorControl.Rule(Umidade["umida"] & Temperatura["media"], Irrigacao["pouca"]),
    pescadorControl.Rule(Umidade["umida"] & Temperatura["alta"], Irrigacao["moderada"]),
]

Valores =


def Fuzzyy(Valores,Regras,):
    Umidade = pescadorControl.Antecedent(np.arange(Valores[0],Valores[1] , 1), "Umidade")
    Temperatura = pescadorControl.Antecedent(np.arange(Valores[2], Valores[3], 1), "Temperatura")

    Irrigacao = pescadorControl.Consequent(np.arange(Valores[4], Valores[5], 1), "Irrigacao")

    # Faixas de valores

    Umidade["seca"] = fuzz.trimf(Umidade.universe, [0, 25, 50])
    Umidade["media"] = fuzz.trimf(Umidade.universe, [25, 50, 75])
    Umidade["umida"] = fuzz.trimf(Umidade.universe, [50, 75, 100])

    Temperatura["baixa"] = fuzz.trimf(Temperatura.universe, [0, 10, 20])
    Temperatura["media"] = fuzz.trimf(Temperatura.universe, [10, 20, 30])
    Temperatura["alta"] = fuzz.trimf(Temperatura.universe, [20, 30, 40])

    Irrigacao["pouca"] = fuzz.trimf(Irrigacao.universe, [0, 2.5, 5])
    Irrigacao["moderada"] = fuzz.trimf(Irrigacao.universe, [3, 5, 7])
    Irrigacao["intensa"] = fuzz.trimf(Irrigacao.universe, [5, 7.5, 10])

    # Regras dos Amigos


    Fim = pescadorControl.ControlSystem(Regras)
    Simu = pescadorControl.ControlSystemSimulation(Fim)

    Simu.input["Umidade"] = 30
    Simu.input["Temperatura"] = 35
    Simu.compute()

    # Saidas e printadas

    print(Simu.output["Irrigacao"])
    maior_pertinencia = 0
    categoria = ""

    for termo in Irrigacao.terms:
        pertinencia = fuzz.interp_membership(
            Irrigacao.universe, Irrigacao[termo].mf, Simu.output["Irrigacao"]
        )
        print(f"perti: '{termo}': {pertinencia:.3f}")
        if pertinencia > maior_pertinencia:
            maior_pertinencia = pertinencia
            categoria = termo

    print("É:", categoria)
