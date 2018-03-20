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
    {'text': 'Tomate Jambon Pain Beurre', 'category': 'tomate'},
    {'text': 'J‘ai besoin de savoir une informaton ou une question', 'category': 'question'},
    {'text': 'J‘ai une question', 'category': 'question'},
    {'text': 'Aurevoir', 'category': 'tiao'},
    {'text': 'Merci, bonne journée !', 'category': 'tiao'},
    {'text': 'Top merci pour votre aide', 'category': 'tiao'},
    {'text': 'PSG / Marseille', 'category': 'classico'},
    {'text': 'Dimanche dernier', 'category': 'classico'},
    {'text': 'Evra', 'category': 'classico'},
    {'text': 'Panini panini paninie paninis', 'category': 'panini'},
]
