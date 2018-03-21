# coding: utf-8

"""
Suppose you have some texts of news and know their categories.
You want to train a system with this pre-categorized/pre-classified
texts. So, you have better call this data your training set.
"""
from lib import get_classer
from data import newsSet

excec = {
    'hello': 1,
    'fin': 0,
    'question': 0,
    'sandwich': 0,
    'pate': 0,
    'mexicain': 0,
    'classico': 0,
    'panini': 0,
    'pizza': 0,
    'carbonara': 0,
    'bolognaise': 0,
    'jambon': 0,
    'toscane': 0,
    'tacospoulet': 0,
}

def ma_loop(value):
    newsClassifier = get_classer()
    classification = newsClassifier.classify(value)
    # [('tiao', 0.0), ('question', 0.0), ('hello', 0.0)]
    category = classification[0][0]
    score = classification[0][1]

    if score > 0:
        # newsSet.append({'text': value, 'category': category})
        excec[category] += 1
        if category == 'hello': return hello()
        if category == 'question': return question()
        if category == 'fin': return fin()
        if category == 'classico': return classico(value)
        if category == 'sandwich': return sandwich()
        if category == 'panini': return panini()
        if category == 'pizza': return pizza()
        if category == 'carbonara': return carbonara()
        if category == 'bolognaise': return bolognaise()
        if category == 'jambon': return jambon()
        if category == 'toscane': return toscane()
        if category == 'tacospoulet': return tacospoulet()
        if category == 'tacosboeuf': return tacosboeuf()
        if category == 'mexicain': return mexicain()
        if category == 'pate': return pate()
    return pascompris(value)

def question(value=None):
    value = raw_input("A propos de moi?")
    if "oui" in value:
        value = raw_input("Je m'appel machin je suis là pour t'aider à choisir des plats à cuisiner")
    else: 
        value = raw_input("Qu'avez vous dans votre frigo?'")
    return ma_loop(value)

def classico(value=None):
    if 'Evra' in value:
        print 'Oui, il était très mauvais'
        value = raw_input("Vous avez une autre question ?")
        return ma_loop(value)

    if 'PSG' in value:
        print 'Effectivement, très fort'
        value = raw_input("Vous voulez savoir comment evra à jour ?")
        return ma_loop(value)


def hello(value=None):
    if excec['hello'] is 1:
        value = raw_input("Bonjour! Je suis Gisèle, votre conseillère pour la préparation de votre dîner. Pour m'activer, taper On mange quoi ce soir")
    elif excec['hello'] is 2:
        value = raw_input("Tout d'abord qu'avez vous dans votre frigo?")
    elif excec['hello'] is 3:
        value = raw_input("Oui, je vous écoute nous sommes à votre service ?")
    elif excec['hello'] is 4:
        value = raw_input("Bonjour, j'ai compris pour la quatrieme fois !!, je vous écoute")
    else:
        value = raw_input("Bonjour,")


    return ma_loop(value)

def pascompris(value=None):
    value = raw_input("Je n'ai pas compris, pouvez vous réessayer? Pour recommencer entrez - On mange quoi ce soir -")
    return ma_loop(value)

def fin(value=None):
    value = raw_input("Puis-je faire autre chose maintenant? Oui / Non")
    if "oui" in value:
        value = raw_input("Pour chercher une nouvelle recette tapez - On mange quoi ce soir -")
    elif "non" in value: 
        value = raw_input("Bon appetit! 🍽 ")     
    return ma_loop(value)

def time(value=None):
    return raw_input("De combien de temps disposez-vous pour cuisiner : 10' / 20' / 30' ")

def four(value=None):
    return raw_input("Avez vous un four? Oui / Non")

#Ingrédients clé
def sandwich(value=None):
    timer = time()
    if "10" in timer:
        materiel = four()
        if 'oui' in materiel:
            value = raw_input("Je vous propose les recettes suivantes : panini / pizza ")
            if 'pizza' in value:
                exec pizza()
            elif 'panini' in value: 
                exec panini()
        elif 'non' in materiel:
            value = raw_input("Je vous propose les recettes suivantes : tomate mozzarella / salade cesar  ")
            if 'tomate mozzarella' in value:
                exec tomatemozza()
            elif 'salade cesar' in value:
                saladecesar()
    elif '20' in timer:
        exec pizza()
    return ma_loop(value)

def pate(value=None):
    if "10" in value:
        value = raw_input("Super, je vous propose : pate carbonara / pate bolognaise / pate jambon / pate toscane")
    return ma_loop(value)

def mexicain(value=None):
    value = raw_input("Super, je vous propose : tacos au poulet / tacos au boeuf")
    return ma_loop(value)

#Recettes-----------------------

#Sandwich-------
def panini(value=None):
    value = raw_input("Voilà la recette du Panini : http://bit.ly/paniniPy")
    exec fin()

def pizza(value=None):
    value = raw_input("Voilà la recette de la pizza : http://bit.ly/pizzaPy")
    exec fin()

def tomatemozza():
    value = raw_input("Voilà la recette de la Tomate Mozzarella : http://bit.ly/tomateMozzaPy")
    exec fin()

def saladecesar():
    value = raw_input("Voilà la recette de la Salade César : http://bit.ly/saladeCesarPy")
    exec fin()

#Pate-------
def carbonara(value=None):
    value = raw_input("Voilà la recette des pâtes à la carbonara : http://bit.ly/carbonaraPy ")
    exec fin() 

def bolognaise(value=None):
    value = raw_input("Voilà la recette des pâtes à la bolognaise : http://bit.ly/bolognaisePy")
    exec fin()

def jambon(value=None):
    value = raw_input("Voilà la recette des pâtes au jambon : http://bit.ly/jambonPy")
    exec fin()

def toscane(value=None):
    value = raw_input("Voilà la recette des pâtes à la façon toscane : http://bit.ly/toscanePy")
    exec fin()

#Mexicain-------
def tacosboeuf(value=None):
    value = raw_input("Voilà la recette des tacos au boeuf : http://bit.ly/tacosBoeufPy ")
    exec fin()

def tacospoulet(value=None):
    value = raw_input("Voilà la recette des tacos au poulet : http://bit.ly/tacosPouletPy")
    exec fin()



hello()
