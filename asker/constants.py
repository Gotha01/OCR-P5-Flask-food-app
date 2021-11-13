# -*- coding: utf-8 -*-

#-----------------------------------CONFIG------------------------------------
SQL_CONNECTORS = {
    'user' : 'root',
}
DTB = "pur_beurre"
CATEGORIES = ["snacks", "boissons", "pates", "pizzas"]

#----------------------------------Questions----------------------------------
#Messages
HOME_MESSAGE = ["Bienvenue sur notre application de substitution des produits.",
                "Veuillez appuyer sur 'ENTREE'."]

HOME_USER_MESSAGE = ["Lancement de l'interface utilisateur.",
                     "Veuillez appuyer sur 'ENTREE'."]

LEAVING = ["Merci d'avoir utiliser notre application !","A bientôt !"]

NO_FAV_PRODUCT = "    Aucun produit n'est enregistré dans vos produits favoris"

SEARCHING_RULE = "Veuillez entrer au minimum 3 caractères."
#Questions
Q1 = "  Veuillez choisir parmi les options suivantes :"
Q2 = "  Voici les différentes méthodes de recherche :"
Q3 = "  Veuillez choisir parmi les catégories suivantes :"
Q3_1 = "  Veuillez sélectionner l'identifiant du produit de votre choix :"
Q4 = "  Veuillez indiquer le nom du produit à substituer :"
Q5 = "  Veuillez selectionner le produit dont vous souhaitez \
plus de détails : (valeur nutritionnelle)"
Q6 = "  Voulez-vous rechercher un substitut pour ce produit?"
Q6_1 = "  Ces produits sont les mieux classés de la catégories. \
Veuillez sélectionner l'identifiant du produit de votre choix :"
Q7 = "  Votre recherche ne correspond à aucun produit."
Q8 = "  Vous pouvez enregistrer ce produit dans vos produits favoris"

#Choices
SUPRESS = "Supprimer tous les produits de la liste enregistrés."
REPLACE_PROD = "    Entrez le nom du produit que vous souhaitez remplacer : \
(3 caractères minimum)"
MAIN_MENU = "Retour au menu principal."

C_EMPTY = []
C1 = ["Remplacer un produit.", "Retrouver mes produits favoris.", "Quitter."]
C2 = [
    "Choisir un produit dans une catégorie.",
    "Choisir un produit en fonction de son nom.",
    "Retour au menu principal.",
    "Quitter."
    ]
C3 = ["Snacks.","Pates.", "Boissons.", "Pizzas.",
      "Retour au menu principal.", "Quitter."]
C4 = ["", "Retour au menu principal.", "Quitter."]
C6 = ["Oui.", "Non."]
C7 = ["Réessayer.", "Retour au menu principal."]

#Answers
ANS_1 = "\nVotre choix : "
ANS_2 = "\nVotre méthode : "
ANS_3 = "\nVotre catégorie : "
ANS_4 = "\nVotre produit : "
ANS_5 = "\nProduit sélectionné : "
ANS_6 = "\nTrouver un substitut ? "
ANS_7 = "\nVotre choix : "
ANS_8 = "\nVotre proposition : "

QUESTIONER = {
    Q1 : [C1, ANS_1],
    Q2 : [C2, ANS_2],
    Q3 : [C3, ANS_3],
    Q3_1 : [C_EMPTY, ANS_4],
    Q4 : [C4, ANS_4],
    Q5 : [C_EMPTY, ANS_5],
    Q6 : [C6, ANS_6],
    Q6_1 : [C_EMPTY, ANS_5],
    Q7 : [C7, ANS_7],
    Q8 : [C6, ANS_7],
    REPLACE_PROD: [C_EMPTY, ANS_8]
}