from is_set import *
import os
import pygame

#laadt afbeeldingen
def laden_afb():
    global afb_kaarten
    map = 'kaarten'
    for color in kleuren:
        for symbol in symbolen:
            for shading in schaduw:
                for number in [1,2,3]:
                    bestandsnaam = f'{color}{symbol}{shading}{number}.gif'
                    pad = os.path.join(map, bestandsnaam)
                    if os.path.isfile(pad):
                        afb = pygame.image.load(pad).convert_alpha()
                        key = (kleuren.index(color), symbolen.index(symbol), schaduw.index(shading), number)
                        afb_kaarten[key] = afb
