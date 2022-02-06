#Emer
#The puzzle is a secret word randomly chosen from a list.
import random

class Secretword():

    def __init__(self):
        self.word= ""

    def secretword(self):
        
        list = [
            "water",
            "fire",
            "wind",
            "king",
            "queen",
            "apple",
            "star",
            "table",
            "Chair",
            "nun",
            "burn",
            "sustain",
            "shelf",
            "reveal",
            "hide",
            "cheap",
            "bold",
            "promote",
            "demote",
            "matrix",
            "production"
        ]
        
        word = random.choice(list)
        self.word = word
        return word
    
    def displayword(self, word):
        display = []
        for letter in range(len(word)):
            display += "_"
        return display
