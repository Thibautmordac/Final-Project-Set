import os
import sys
import pygame
import random
from variabelen import *
from is_set import *
from stapel import *
from laden_afb import *
from tafel import *
from beurt_speler import *

pygame.init()

kleine_letter = pygame.font.SysFont(None, FONT_KLEIN)
grote_letter = pygame.font.SysFont(None, FONT_GROOT)
scherm = pygame.display.set_mode((SCHERM_BREEDTE, SCHERM_HOOGTE))

def main():
    laden_afb()
    stapel = creëren_stapel()
    random.shuffle(stapel)
    scores = {'Speler':0, 'Computer':0}

    tafel = []
    for _ in range(12):
        tafel.append(stapel.pop(0))

    while True:
        toon_tafel(tafel, [], '', scores, scherm, kleine_letter, grote_letter)
        gevonden = beurt_speler(tafel, stapel, scores, '', scherm, kleine_letter, grote_letter)
        if gevonden:
            if len(tafel) < 3 or (not stapel and not vind_set(tafel)):
                break
            continue

        while not vind_set(tafel) and len(stapel) >= 3:
            vervang_drie(tafel, stapel)

        een_set = vind_set(tafel)
        if een_set:
            scores['Computer'] += 1
            for kaart in een_set:
                idx = tafel.index(kaart)
                if stapel:
                    tafel[idx] = stapel.pop(0)
                else:
                    del tafel[idx]
            while len(tafel) < 12 and stapel:
                tafel.append(stapel.pop(0))
        else:
            break
    
    toon_tafel(tafel, [], 'Game Over', scores, scherm, kleine_letter, grote_letter)
    print(f"Eindscores: Speler = {scores['Speler']}, Computer = {scores['Computer']}")
    pygame.quit()
if __name__ == '__main__':
    main()
