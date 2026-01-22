from variabelen import *
from stapel import *

#toont de 12 kaarten op 'tafel' als overzicht (met scores)
def toon_tafel(kaarten, indices, bericht, score):
    scherm.fill((255,255,255))
    for p, kaart in enumerate(kaarten):
        rij = p // kaart_per_rij
        kolom = p % kaart_per_rij
        x = x_marge + kolom * (kaartbreedte+x_marge)
        y = y_marge + rij * (kaartlengte+y_marge)
        kaart_trekken(kaart, x, y, p, p in indices)
    if bericht:
        tekst = grote_letter.render(bericht, True, (0,150,0))
        scherm.blit(tekst, (scherm.get_width()//2 - 100, scherm.get_height() - 75))
        score_tekst = lettertype.render(f'Speler: {score['Speler']}     Computer: {score['Computer']}', True, (0,0,0))
        scherm.blit(score_tekst, (scherm.get_width() - 325 , 10))
        pygame.display.flip()

def vervang_drie(tafel, stapel):
    """vervangt de 3 kaarten die zijn verdwenen van de tafel met degene van de stapel"""
    if len(stapel) >= 3:
        for _ in range(3):
            tafel.pop(0)
            tafel.insert(0, stapel.pop(0))
