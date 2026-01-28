from time import time
import sys
import pygame
from is_set import *
from tafel import *
from variabelen import *

def beurt_speler(tafel, stapel, score, bericht, scherm, kleine_letter, grote_letter):
    """Zorgt ervoor dat knoppen werken, er een tijdslimiet is
    , scores worden bijgewerkt en stapel wordt aangepast"""
    geklikt = []
    start_tijd = time()
    while time() - start_tijd < 30:
        toon_tafel(tafel, geklikt, bericht, score, scherm, kleine_letter, grote_letter)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                kolom = mx // (kaartbreedte+x_marge)
                rij = my // (kaartlengte+y_marge)
                idx = rij * kaart_per_rij + kolom
                if 0 <= idx < len(tafel):
                    if idx in geklikt:
                        geklikt.remove(idx)
                    else:
                        geklikt.append(idx)
                    if len(geklikt) == 3:
                        if is_set(tafel[geklikt[0]], tafel[geklikt[1]], tafel[geklikt[2]]):
                            score['Speler'] += 1
                            for p in sorted(geklikt, reverse=True):
                                if stapel:
                                    tafel[p] = stapel.pop(0)
                                else:
                                    del tafel[p]
                            while len(tafel) < 12 and stapel:
                                tafel.append(stapel.pop(0))
                            geklikt.clear()
                            return True
                        else:
                            geklikt.clear()
                            bericht = 'Is geen SET'
    return False
