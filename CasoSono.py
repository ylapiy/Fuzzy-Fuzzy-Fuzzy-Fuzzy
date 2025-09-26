import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as pescadorControl

# Definido as coisas que variam (populamente conhecidas como variaveis)

Cansaco = pescadorControl.Antecedent(np.arange(0, 11, 1), "Cansaco")
Sono = pescadorControl.Antecedent(np.arange(0, 11, 1), "Sono")

Acao = pescadorControl.Consequent(np.arange(0, 11, 1), "Acao")

# Faixas de valores

Cansaco["baixo"] = fuzz.trimf(Cansaco.universe, [0, 2.5, 5])
Cansaco["medio"] = fuzz.trimf(Cansaco.universe, [3, 5, 7])
Cansaco["alto"] = fuzz.trimf(Cansaco.universe, [5, 7.5, 10])

Sono["pouco"] = fuzz.trimf(Sono.universe, [0, 2.5, 5])
Sono["adequado"] = fuzz.trimf(Sono.universe, [3, 5, 7])
Sono["muito"] = fuzz.trimf(Sono.universe, [5, 7.5, 10])

Acao["alerta"] = fuzz.trimf(Acao.universe, [0, 2.5, 5])
Acao["descanso"] = fuzz.trimf(Acao.universe, [3, 5, 7])
Acao["forcar_pausa"] = fuzz.trimf(Acao.universe, [5, 7.5, 10])

# Regras dos Amigos

Regras = [
    pescadorControl.Rule(Cansaco["baixo"] & Sono["pouco"], Acao["alerta"]),
    pescadorControl.Rule(Cansaco["baixo"] & Sono["adequado"], Acao["alerta"]),
    pescadorControl.Rule(Cansaco["baixo"] & Sono["muito"], Acao["descanso"]),
    pescadorControl.Rule(Cansaco["medio"] & Sono["pouco"], Acao["descanso"]),
    pescadorControl.Rule(Cansaco["medio"] & Sono["adequado"], Acao["descanso"]),
    pescadorControl.Rule(Cansaco["medio"] & Sono["muito"], Acao["forcar_pausa"]),
    pescadorControl.Rule(Cansaco["alto"] & Sono["pouco"], Acao["forcar_pausa"]),
    pescadorControl.Rule(Cansaco["alto"] & Sono["adequado"], Acao["forcar_pausa"]),
    pescadorControl.Rule(Cansaco["alto"] & Sono["muito"], Acao["forcar_pausa"]),
]

# Inicio da Simulação

Fim = pescadorControl.ControlSystem(Regras)
Simu = pescadorControl.ControlSystemSimulation(Fim)

Simu.input["Cansaco"] = 8
Simu.input["Sono"] = 4
Simu.compute()


# Saidas e printadas

print(Simu.output["Acao"])
maior_pertinencia = 0
categoria = ""

for termo in Acao.terms:
    pertinencia = fuzz.interp_membership(
        Acao.universe, Acao[termo].mf, Simu.output["Acao"]
    )
    print(f"perti: '{termo}': {pertinencia:.3f}")
    if pertinencia > maior_pertinencia:
        maior_pertinencia = pertinencia
        categoria = termo

print("É:", categoria)

Cansaco.view(sim=Simu)
Sono.view(sim=Simu)
Acao.view(sim=Simu)
# Pausa Forçada, mas deu 7.5 ao inves de 8 hummmmmmmmmmmmmmmmmmmm
