# -*- coding: utf-8 -*-


#-----------------------------------------DTBCONFIG-----------------------------------------

user = {
    'user' : 'root',
}
dtb = "projet5"
categories = ["snacks", "boissons", "pates", "pizzas"]

#-------------------------------------------Questions-------------------------------------------
#Messages
home_msg = "Bienvenue sur notre application de substitution des aliments.\n      <<APPUYEZ SUR ENTREE>>>"
home_user_msg = "Lancement de l'interface utilisateur\n      <<APPUYEZ SUR ENTREE>>>"
leaving = "Merci d'avoir utiliser notre application! A bientôt !"


#Questions
q1 = "==>   Veuillez choisir parmi les options suivantes :\n\
            (Entrez un nombre)\n"
q2 = "==>   Voici les différentes méthodes de recherche :\n"
q3 = "==>   Veuillez choisir parmi les catégories suivantes :\n"
q3_1 = "==> Veuillez sélectionner l'identifiant du produit de votre choix :\n"
q4 = "==>   Veuillez indiquer le nom de l'aliment à substituer :\n"
q5 = "==>   Veuillez selectionner l'aliment dont vous souhaitez plus de détails :\n"

#Choices
c1 = ["Remplacer un aliment.", "Retrouver mes aliments substitués.", "Retrouver mes produits favoris.", "Quitter."]
c2 = ["Choisir en fonction de la catégorie.", "Choisir en fonction de l'aliment.", "Retour au menu principal.", "Quitter."]
c3 = ["Snacks.","Pates.", "Boissons.", "Pizzas.", "Retour au menu principal.", "Quitter."]
c3_1 = []
c4 = ["", "Retour au menu principal.", "Quitter."]
c5 = []

#Answers
ans_1 = "\nVotre choix : "
ans_2 = "\nVotre méthode : "
ans_3 = "\nVotre catégorie : "
ans_4 = "\nVotre aliment : "
ans_5 = "\nAliment sélectionné: "

questioner = {
    q1 : [c1, ans_1],
    q2 : [c2, ans_2],
    q3 : [c3, ans_3],
    q3_1 : [c3_1, ans_4],
    q4 : [c4, ans_4],
    q5 : [c5, ans_5]
}