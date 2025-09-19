from Fuzzy import Logicas

Logica = Logicas()

"""
Exercício 1: Altura de Pessoas•Baixo (1.40m a 1.60m)
•Médio (1.55m a 1.80m)
•Alto (1.75m a 2.00m)
•→ Avaliar altura 1.72m: pertinênciaparacadaconjunto
"""

print("Altura de Pessoas :")

print(f"Baixo : {Logica.Triangulho(1.72, 1.40, 1.50, 1.60)}")
print(f"Médio : {Logica.Triangulho(1.72, 1.55, 1.675, 1.80)}")
print(f"Alto : {Logica.Triangulho(1.72, 1.75, 1.875, 2.00)}")

print("----------------------------------------------------")

""" 
Exercício 2: Qualidade do Serviço•Nota de 0 a 10
•Conjuntos: Ruim (0-4), Bom(3-7), Excelente(6-10)
•→ Avaliar nota 6
"""

print("Nota :")

print(f"Ruim : {Logica.Triangulho(6, 0, 2, 4)}")
print(f"Bom : {Logica.Triangulho(6, 3, 5, 7)}")
print(f"Execelente : {Logica.Triangulho(6, 6 ,8, 10)}")

print("----------------------------------------------------")
