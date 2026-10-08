###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.

nom = "Encaminador3000"
ubi = "Facultat d'enginyeria"
ports = 25
ences = "Si"

print(f"Nom: {nom}, Ubicació: {ubi}, Numero de ports: {ports}, Encés: {ences}")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.

inclosos = 67
consumits = 3
queden = inclosos - consumits
print(f"Queden {queden}GB. (1)")

consumits = 25
queden = inclosos - consumits
print(f"Queden {queden}GB. (2)")