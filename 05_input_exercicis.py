###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.

tecnic = str(input("Quin es el nom del tècnic?: "))
xarxa = str(input("Quin es el nom de la xarxa?: "))

print(f"Nom del tècnic: {tecnic}, Nom de la xarxa: {xarxa}")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.

fibra_km = float(input("KM d'enllaç de Fibra: "))
gbps = float(input("Velocitat de transmissió (Gbps):"))
segons = 8 / gbps

print(f"Segons necessaris per transmetre 1 GB de dades: {segons}")

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.

hores = float(input("Hores de feina?: "))
preuh = float(input("Preu per hores de feina? (€): "))
preumat = float(input("Preu del material? (€): "))
cost = preuh + preumat + hores

print(f"Cost total de la instal·lació: {cost}€.")