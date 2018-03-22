# coding: utf-8

"""
Suppose you have some texts of news and know their categories.
You want to train a system with this pre-categorized/pre-classified
texts. So, you have better call this data your training set.
"""
from lib import get_classer
from data import newsSet
import os

excec = {
    'hello': 1,
    'fin': 0,
    'question': 0,
    'tarte': 0,
    'pate': 0,
    'salade' : 0,
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
        if category == 'pate': return pate()
        if category == 'salade': return salade()
        if category == 'tarte': return tarte()
    return pascompris(value)

def question(value=None):
    value = raw_input("A propos de moi? - Oui - ")
    if "oui" in value:
        value = raw_input("Je m'appel Gisèle je suis là pour t'aider à choisir des plats à cuisiner")
    else: 
        value = raw_input("Qu'avez vous dans votre frigo?'")
    return ma_loop(value)


def hello(value=None):
    #os.system('open -a "Google Chrome" http://bit.ly/bolognaisePy')
    if excec['hello'] is 1:
        value = raw_input("Bonjour! Je suis Gisèle, votre conseillère pour la préparation de votre dîner. Pour m'activer, taper On mange quoi ce soir")
    elif excec['hello'] is 2:
        value = raw_input("Tout d'abord qu'avez vous dans votre frigo?")
    elif excec['hello'] is 3:
        value = raw_input("Oui, je vous écoute qu'avez vous dans votre frigo ?")
    elif excec['hello'] is 4:
        value = raw_input("Oui, je vous écoute qu'avez vous dans votre frigo ?")
    elif excec['hello'] is 5:
        value = raw_input("Désolé mais déjà 5 fois que je ne peux répondre à votre demande, je vous conseille : http://bit.ly/derniereSolution")
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
def pate(value=None):
    raw_input("Faisons des pates! (Appuyez sur entrée ⏳)")
    timer = time()
    if '10' in timer:
        value = raw_input("Je vous propose les recettes suivantes : PatePesto / MacNCheese (Copier coller le plat choisi) ")
        if 'PatePesto' in value:
            exec patepesto()
        elif 'MacNCheese' in value: 
            exec macncheese()
    elif '20' in timer:
        value = raw_input("Je vous propose les recettes suivantes : PateBolognaise ")
        if 'PateBolognaise' in value:
            exec patebolognaise()
    elif '30' in timer:
        value = raw_input("Je vous propose les recettes suivantes : PateCurry / PateCarbonara")
        if 'PateCurry' in value:
            exec patecurry()
        elif 'PateCarbonara' in value: 
            exec patecarbonara()

def salade(value=None):
    raw_input("Faisons une salade composée! (Appuyez sur entrée ⏳)")
    timer = time()
    if '10' in timer:  
        value = raw_input("Seulement 10 minutes... Je vous propose les recettes suivantes : SaladeGrec / TomateMozzarella (Copier coller le plat choisi)") 
        if 'SaladeGrec' in value:
            exec saladegrec()
        elif 'TomateMozzarella' in value:
            exec tomatemozza()
    elif '20' in timer:
        value = raw_input("20 minutes? De quoi préparer quelque chose de bon! Je vous propose les recettes suivantes : SaladeCesar / SaladeNicoise (Copier coller le plat choisi)")
        if 'SaladeCesar' in value:
            exec saladecesar()
        elif 'SaladeNicoise' in value: 
            exec saladenicoise()
    elif '30' in timer:
        value = raw_input("30 minutes! Nous avons le temps de cuisiner et refaire le monde! Je vous propose les recettes suivantes : SaladeMexicaine (Copier coller le plat choisi)")
        exec saladecesar()


def tarte(value=None):
    materiel = four()
    raw_input("Super! Faisons une tarte. (Appuyez sur entrée ⏳)")
    if 'oui' in materiel:
        timer = time()
        if '10' in timer:
            value = raw_input("Je vous propose les recettes suivantes : Flamenkuech /  TarteThon (Copier coller le plat choisi)")
            if 'Flamenkuech' in value:
                exec flamenkuech()
            elif 'TarteThon' in value: 
                exec tartethon()
        elif '20' in timer:
            value = raw_input("Je vous propose les recettes suivantes : TarteTomate / Pizza (Copier coller le plat choisi)")
            if 'TarteTomate' in value:
                exec tartetomate()
            elif 'Pizza' in value: 
                exec pizza()
        elif '30' in timer:
            value = raw_input("Je vous propose les recettes suivantes : QuicheLorraine / TatinPommeDeTerre (Copier coller le plat choisi)")
            if 'QuicheLorraine' in value:
                exec quichelorraine()
            elif 'TatinPommeDeTerre' in value: 
                exec tatinpdt()
    elif 'non' in materiel:
        raw_input("Désolé... Mais avec ces ingrédients nous avons besoin d'un four! Peut tu entrer d'autre ingrédient?")
        return ma_loop(value)

#Sandwich-------
def panini(value=None):
    value = raw_input("Voilà la recette du Panini : http://bit.ly/paniniPy")
    exec fin()



#Pate-------
def patepesto(value=None):
    value = raw_input("Voilà la recette des pâtes pesto : http://bit.ly/patePestoPy ! Appuyez sur Entrée pour ouvrir la recette sur internet")
    os.system('open -a "Google Chrome" http://bit.ly/patePestoPy')
    exec fin()

def macncheese(value=None):
    value = raw_input("Voilà la recette du Mac'n'Cheese (arrêtez vous à l'étape 4) : http://bit.ly/macNCheesePy ! Appuyez sur Entrée pour ouvrir la recette sur internet")
    os.system('open -a "Google Chrome" http://bit.ly/macNCheesePy')
    exec fin()

def patebolognaise(value=None):
    value = raw_input("Voilà la recette des pâtes à la bolognaise : http://bit.ly/bolognaisePy ! Appuyez sur Entrée pour ouvrir la recette sur internet")
    os.system('open -a "Google Chrome" http://bit.ly/bolognaisePy')
    exec fin()

def patecurry(value=None):
    value = raw_input("Voilà la recette des pa^tes au curry : http://bit.ly/pateCurryPy ! Appuyez sur Entrée pour ouvrir la recette sur internet")
    os.system('open -a "Google Chrome" http://bit.ly/pateCurryPy')
    exec fin()

def patecarbonara(value=None):
    value = raw_input("Voilà la recette des pâtes à la carbonara : http://bit.ly/carbonaraPy ! Appuyez sur Entrée pour ouvrir la recette sur internet")
    os.system('open -a "Google Chrome" http://bit.ly/carbonaraPy')
    exec fin() 

#Salade-------
def saladegrec(value=None):
    value = raw_input("Voilà la recette de la Salade Grec : http://bit.ly/saladeGrecPy ! Appuyez sur Entrée pour ouvrir la recette sur internet")
    os.system('open -a "Google Chrome" http://bit.ly/saladeGrecPy')
    exec fin()

def tomatemozza(value=None):
    value = raw_input("Voilà la recette de la Tomate Mozzarella : http://bit.ly/tomateMozzaPy  ! Appuyez sur Entrée pour ouvrir la recette sur internet")
    os.system('open -a "Google Chrome" http://bit.ly/tomateMozzaPy')
    exec fin()

def saladecesar(value=None):
    value = raw_input("Voilà la recette de la Salade César : http://bit.ly/saladeCesarPy ! Appuyez sur Entrée pour ouvrir la recette sur internet")
    os.system('open -a "Google Chrome" http://bit.ly/saladeCesarPy')
    exec fin()

def saladenicoise(value=None):
    value = raw_input("Voilà la recette de la Salade Niçoise : http://bit.ly/saladeNicoisePy ! Appuyez sur Entrée pour ouvrir la recette sur internet")
    os.system('open -a "Google Chrome" http://bit.ly/saladeNicoisePy')
    exec fin()

def salademexicaine(value=None):
    value = raw_input("Voilà la recette de la Salade Mexicaine : http://bit.ly/saladeMexicainePy ! Appuyez sur Entrée pour ouvrir la recette sur internet")
    os.system('open -a "Google Chrome" http://bit.ly/saladeMexicainePy')
    exec fin()

#Salade-------
def jambonbeurre(value=None):
    value = raw_input("Voilà la recette du sandwich Jambon Beurre : http://bit.ly/jambonBeurrePy ! Appuyez sur Entrée pour ouvrir la recette sur internet")
    os.system('open -a "Google Chrome" http://bit.ly/jambonBeurrePy')
    exec fin()

def pouletcrudite(value=None):
    value = raw_input("Voilà la recette du Sandwich Poulet Crudité : http://bit.ly/pouletCruditéPy ! Appuyez sur Entrée pour ouvrir la recette sur internet")
    os.system('open -a "Google Chrome" http://bit.ly/pouletCruditéPy')
    exec fin()

def wrappouletbacon(value=None):
    value = raw_input("Voilà la recette du Wrap Poulet Bacon : http://bit.ly/wrapPouletBacon ! Appuyez sur Entrée pour ouvrir la recette sur internet")
    os.system('open -a "Google Chrome" http://bit.ly/wrapPouletBacon')
    exec fin()

def grilledcheese(value=None):
    value = raw_input("Voilà la recette du Grilled Cheese : http://bit.ly/grilledCheesePy ! Appuyez sur Entrée pour ouvrir la recette sur internet")
    os.system('open -a "Google Chrome" http://bit.ly/grilledCheesePy')
    exec fin()

def fajitas(value=None):
    value = raw_input("Voilà la recette des Fajitas : http://bit.ly/fajitasPouletPy ! Appuyez sur Entrée pour ouvrir la recette sur internet ")
    os.system('open -a "Google Chrome" http://bit.ly/fajitasPouletPy')
    exec fin(value=None)

def burritos(value=None):
    value = raw_input("Voilà la recette des Burritos : http://bit.ly/bujitosPy ! Appuyez sur Entrée pour ouvrir la recette sur internet")
    os.system('open -a "Google Chrome" http://bit.ly/bujitosPy')
    exec fin()


#Tarte-------
#--- 10 minutes
def flamenkuech(value=None):
    value = raw_input("Voilà la recette de la Flamenkich : http://bit.ly/flammekuechePy ! Appuyez sur Entrée pour ouvrir la recette sur internet")
    os.system('open -a "Google Chrome" http://bit.ly/flammekuechePy')
    exec fin()

def tartethon(value=None):
    value = raw_input("Voilà la recette de la Tarte au Thon : http://bit.ly/tarteThonPy  ! Appuyez sur Entrée pour ouvrir la recette sur internet")
    os.system('open -a "Google Chrome" http://bit.ly/tarteThonPy')
    exec fin()

#--- 20 minutes
def tartetomate(value=None):
    value = raw_input("Voilà la recette de la Tarte à la Tomate : http://bit.ly/tarteTomatePy ! Appuyez sur Entrée pour ouvrir la recette sur internet ")
    os.system('open -a "Google Chrome" http://bit.ly/tarteTomatePy')
    exec fin()

def pizza(value=None):
    value = raw_input("Voilà la recette de la pizza : http://bit.ly/pizzaPy ! Appuyez sur Entrée pour ouvrir la recette sur internet")
    os.system('open -a "Google Chrome" http://bit.ly/pizzaPy')
    exec fin()

#--- 30 minutes
def quichelorraine(value=None):
    value = raw_input("Voilà la recette de la Quiche Lorraine : http://bit.ly/quicheLorrainePy ! Appuyez sur Entrée pour ouvrir la recette sur internet")
    os.system('open -a "Google Chrome" http://bit.ly/quicheLorrainePy')
    exec fin()

def tatinpdt(value=None):
    value = raw_input("Voilà la recette de la Tatin de Pomme de Terre : http://bit.ly/tatinPdtPy ! Appuyez sur Entrée pour ouvrir la recette sur internet")
    os.system('open -a "Google Chrome" http://bit.ly/tatinPdtPy')
    exec fin()

hello()

#-- EXEMPLE 
# def exemple(value=None):
#     materiel = four()
#     if 'oui' in materiel:
#         timer = time()
#         if '10' in timer:
#             value = raw_input("Je vous propose les recettes suivantes : xxx01 / xxx02 ")
#             if 'xxx01' in value:
#                 exec xxx01()
#             elif 'xxx02' in value: 
#                 exec xxx02()
#         elif '20' in timer:
#             value = raw_input("Je vous propose les recettes suivantes : xxx03 / xxx04")
#             if 'xxx03' in value:
#                 exec xxx03()
#             elif 'xxx04' in value: 
#                 exec xxx04()
#         elif '30' in timer:
#             value = raw_input("Je vous propose les recettes suivantes : xxx05 / xxx06")
#             if 'xxx05' in value:
#                 exec xxx05()
#             elif 'xxx06' in value: 
#                 exec xxx06()
#     elif 'non' in materiel:
#         timer = time()
#         if '10' in timer:
#             value = raw_input("Je vous propose les recettes suivantes : xxx11 / xxx12 ")
#             if 'xxx11' in value:
#                 exec xxx01()
#             elif 'xxx12' in value: 
#                 exec xxx12()
#         elif '20' in timer:
#             value = raw_input("Je vous propose les recettes suivantes : xxx13 / xxx14")
#             if 'xxx13' in value:
#                 exec xxx13()
#             elif 'xxx14' in value: 
#                 exec xxx14()
#         elif '30' in timer:
#             value = raw_input("Je vous propose les recettes suivantes : xxx15 / xxx16")
#             if 'xxx15' in value:
#                 exec xxx15()
#             elif 'xxx16' in value: 
#                 exec xxx16()
#     return ma_loop(value)

