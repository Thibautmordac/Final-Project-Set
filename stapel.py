from is_set import Kaart

#Genereert een stapel van 81 kaarten met enkel getallen
def creëren_stapel():
    stapel = [Kaart(k, sy, sc, g) for k in range(3) for sy in range(3) for sc in range(3) for g in range(3)]
    return stapel
