# coding: utf-8

"""
Suppose you have some texts of news and know their categories.
You want to train a system with this pre-categorized/pre-classified
texts. So, you have better call this data your training set.
"""

# You need to train the system passing each text one by one to the trainer module.
newsSet = [
    {'text': 'Bonjour', 'category': 'hello'},
    {'text': 'On mange quoi ce soir', 'category': 'hello'},
    #Ingrédients
    {'text': 'Tomate Jambon Pain Beurre Creme champignon Champignon salade fromage mozzarella', 'category': 'sandwich'},
    {'text': 'pates pate creme lardon oeuf oeufs oignons oignon ognons jambon lardon', 'category': 'pate'},
    {'text': 'poivrons poulet tomate oignons poulet boeuf maïs oignon fromage', 'category': 'mexicain'},
    #Recettes
    #Sandwich
    {'text': 'panini Panini PANINI', 'category': 'panini'},
    {'text': 'pizza Pizza PIZZA', 'category': 'pizza'},
    #Pate
    {'text': 'Carbonara Carbo carbonara', 'category': 'carbonara'},
    {'text': 'Bolognaise bolognaise bolo Bolo', 'category': 'bolognaise'},
    {'text': 'Jambon jambon', 'category': 'jambon'},
    {'text': 'Toscane toscane', 'category': 'toscane'},
    #Mexicain
    {'text': 'tacos poulet', 'category': 'tacospoulet'},
    {'text': 'tacos boeuf', 'category': 'tacosboeuf'},
    #Question de base
    {'text': 'J‘ai besoin de savoir une informaton ou une question', 'category': 'question'},
    {'text': 'J‘ai une question', 'category': 'question'},
    {'text': 'Aurevoir', 'category': 'tiao'},
    {'text': 'Merci, bonne journée !', 'category': 'tiao'},
    {'text': 'Top merci pour votre aide', 'category': 'tiao'},
    {'text': 'PSG / Marseille', 'category': 'classico'},
    {'text': 'Dimanche dernier', 'category': 'classico'},
    {'text': 'Evra', 'category': 'classico'},
]