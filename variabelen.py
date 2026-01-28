import pygame
import sys
#volgende variabelen worden meerdere keren gebruikt in heel de code
#te maken met het beeld van de kaarten
kaartbreedte = 120
kaartlengte = 150
x_marge = 30
y_marge = 30
kaart_per_rij = 3

#variabelen hebben te maken met uitstraling van de scherm als geheel
schermbreedte = kaart_per_rij * (kaartbreedte * x_marge) + x_marge
schermlengte = 4 * (kaartlengte + y_marge) + 100
scherm = pygame.display.set_mode((schermbreedte, schermlengte))
FONT_GROOTTE = 24
FONT_GROOT = 48


