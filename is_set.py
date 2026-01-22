#alle verschillende eigenschappen
kleuren = ['red', 'purple', 'green']
symbolen = ['oval', 'squiggle', 'diamond']
schaduw = ['empty', 'filled', 'shaded']
afb_kaarten = {}

#kent 4 eigenschappen toe aan 1 kaart
class Kaart:
    def __init__(self, color, symbol, shading, number):
        self.color = color
        self.symbol = symbol
        self.shading = shading
        self.number = number
    
    def __repr__(self):
        k = f'Kaart({self.color}, {self.symbol}, {self.shading}, {self.number})'
        return k

#checkt om te zien dat 3 gegeven kaarten een set vormen
def is_set(k1, k2, k3):
    return ((k1.number+k2.number+k3.number % 3) == 0 and
            (k1.symbol+k2.symbol+k3.symbol % 3) == 0 and
            (k1.shading+k2.shading+k3.shading) % 3 == 0 and
            (k1.color+k2.color+k3.color) % 3 == 0)

#zoekt naar een set
def vind_set(kaarten):
    for combo in itertools.combinations(kaarten, 3):
        if is_set(*combo):
            return combo
    return None
