###
# Exercicis - conversió de tipus (casting)
# Completa els exercicis següents convertint dades entre tipus.
###

# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.

rebut = int(input("Quants paquets s'han rebut? "))
totals = 1200 + rebut
print(f"S'han rebut {totals} paquets en total.")

# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.

mbps = float(input("Velocitat (mbps): "))
mbs = mbps / 8
print(f"La velocitat {mbps} Mbps és equivalent a {mbs} MB/s")