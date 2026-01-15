import os
import sys

class Card:
    def __init__(self, number, symbol, color, shading):
        self.number = number
        self.symbol = symbol
        self.color = color 
        self.shading = shading 
        
    #bundel de kaarten van (0 tot 2) roep deze bundel op in een string
    def __repr__(self):
        return f"Card({self.number}, {self.color}, {self.symbol}, {self.shading}"
    
    #we willen nu het bestand combineren met de gemaakte kaarten hierboven
    def get_filename(self):
        filename = f"{self.color}{self.symbol}{self.shading}{self.number}.gif" 
        return os.path.join("kaarten", filename)
    
card = Card(2, "diamond", "green", "empty")   
print(card.get_filename())

colors = ["red", "green", "purple"]
symbols = ["oval", "squiggle", "diamond"]
shadings = ["empty", "shaded", "filled"]

def generate_deck():
    deck = []
    for number in [1, 2, 3]:
        for color in colors:
            for symbol in symbols:
                for shading in shadings:
                    deck.append(Card(number, symbol, color, shading))
    return deck

deck = generate_deck()

for c in deck[:6]:
    print(c.get_filename())

    
    
    
    
    