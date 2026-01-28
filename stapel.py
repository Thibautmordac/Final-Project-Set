import pygame
from variabelen import *
from is_set import *

def creëren_stapel():
    """Genereert een stapel van 81 kaarten met enkel getallen"""
    stapel = [Kaart(k, sy, sc, g) for k in range(3) for sy in range(3) for sc in range(3) for g in range(3)]
    return stapel

def kaart_trekken(kaart, x, y, index, gekozen=False, scherm=None):
    """Trekt kaart uit de stapel"""
    bg = (180,220,255) if gekozen else (240,240,240)
    pygame.draw.rect(scherm, bg, (x, y, kaartbreedte, kaartlengte))
    key = (kaart.color, kaart.symbol, kaart.shading, kaart.number + 1)
    if key in afb_kaarten:
        afb = afb_kaarten[key]
        rect = afb.get_rect(center=(x + kaartbreedte // 2, y + kaartlengte // 2 + 10))
        scherm.blit(afb, rect)
