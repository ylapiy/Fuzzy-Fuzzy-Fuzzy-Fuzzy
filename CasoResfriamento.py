import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as pescadorControl

Temperatura = pescadorControl.Antecedent(np.arange(0, 151, 1), "Temperatura")
Carga = pescadorControl.Antecedent(np.arange(0, 101, 1), "Carga")
Resfriamento = pescadorControl.Consequent(np.arange(0, 11, 1), "Resfriamento")

Temperatura["baixa"] = fuzz.trapmf(Temperatura.universe, [0, 0, 40, 80])
Temperatura["media"] = fuzz.trapmf(Temperatura.universe, [60, 80, 110, 130])
Temperatura["alta"] = fuzz.trapmf(Temperatura.universe, [110, 130, 150, 150])

Carga["leve"] = fuzz.trapmf(Carga.universe, [0, 0, 30, 60])
Carga["moderada"] = fuzz.trapmf(Carga.universe, [40, 55, 65, 80])
Carga["pesada"] = fuzz.trapmf(Carga.universe, [60, 80, 100, 100])

Resfriamento["baixo"] = fuzz.trapmf(Resfriamento.universe, [0, 0, 2.5, 5])
Resfriamento["medio"] = fuzz.trapmf(Resfriamento.universe, [3, 4.5, 5.5, 7])
Resfriamento["alto"] = fuzz.trapmf(Resfriamento.universe, [5, 7.5, 10, 10])

Regra = [
    pescadorControl.Rule(Temperatura["baixa"] & Carga["leve"], Resfriamento["baixo"]),
    pescadorControl.Rule(
        Temperatura["baixa"] & Carga["moderada"], Resfriamento["baixo"]
    ),
    pescadorControl.Rule(Temperatura["baixa"] & Carga["pesada"], Resfriamento["medio"]),
    pescadorControl.Rule(Temperatura["media"] & Carga["leve"], Resfriamento["baixo"]),
    pescadorControl.Rule(
        Temperatura["media"] & Carga["moderada"], Resfriamento["medio"]
    ),
    pescadorControl.Rule(Temperatura["media"] & Carga["pesada"], Resfriamento["alto"]),
    pescadorControl.Rule(Temperatura["alta"] & Carga["leve"], Resfriamento["medio"]),
    pescadorControl.Rule(Temperatura["alta"] & Carga["moderada"], Resfriamento["alto"]),
    pescadorControl.Rule(Temperatura["alta"] & Carga["pesada"], Resfriamento["alto"]),
]


Fim = pescadorControl.ControlSystem(Regra)
Simu = pescadorControl.ControlSystemSimulation(Fim)

Simu.input["Temperatura"] = 95
Simu.input["Carga"] = 80

Simu.compute()

print(Simu.output["Resfriamento"])
print("Resfriamento calculado:", Simu.output["Resfriamento"])
maior_pertinencia = 0
categoria = ""

for termo in Resfriamento.terms:
    pertinencia = fuzz.interp_membership(
        Resfriamento.universe, Resfriamento[termo].mf, Simu.output["Resfriamento"]
    )
    print(f"perti: '{termo}': {pertinencia:.3f}")
    if pertinencia > maior_pertinencia:
        maior_pertinencia = pertinencia
        categoria = termo

Temperatura.view(sim=Simu)
Carga.view(sim=Simu)
Resfriamento.view(sim=Simu)