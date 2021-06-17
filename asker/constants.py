# -*- coding: utf-8 -*-


#-----------------------------------------DTBCONFIG-----------------------------------------

user = {
    'user' : 'root',
}

init_Dtb = ('''DROP DATABASE IF EXISTS projet5;''',
    '''CREATE DATABASE IF NOT EXISTS projet5;''')

init_Tables = (
    '''CREATE TABLE IF NOT EXISTS category
        (
            id SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100) NOT NULL UNIQUE,
            url VARCHAR(100) NOT NULL
        )
        ENGINE=INNODB;''',
    '''CREATE TABLE IF NOT EXISTS product 
        (
            id_product SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
            name_product VARCHAR(150) NOT NULL,
            category_ID SMALLINT UNSIGNED NOT NULL,
            nutrition_grades_product VARCHAR(1) NOT NULL,
            store_product VARCHAR(100),
            description_product VARCHAR(1000) NOT NULL,
            url_product VARCHAR(1000) NOT NULL,
            CONSTRAINT fk_product_category_ID FOREIGN KEY (category_ID) REFERENCES category(id) ON DELETE CASCADE
        )
        ENGINE=INNODB;''',
    '''CREATE TABLE IF NOT EXISTS substituted 
        (
            id_substituted SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
            original_product_ID SMALLINT UNSIGNED NOT NULL,
            substituted_product_ID SMALLINT UNSIGNED NOT NULL,
            CONSTRAINT fk_original_product_ID FOREIGN KEY (original_product_ID) REFERENCES product(id_product) ON DELETE CASCADE,
            CONSTRAINT fk_substituted_product_ID FOREIGN KEY (substituted_product_ID) REFERENCES product(id_product) ON DELETE CASCADE,
            UNIQUE INDEX ind_original_product_ID_substituted_product_ID (original_product_ID, substituted_product_ID)
        )
        ENGINE=INNODB;''')

use_dtb = "USE projet5"

categories = ["snacks", "boissons", "pates", "pizzas"]

#-------------------------------------------Questions-------------------------------------------
#Messages
home_msg = "Bienvenue sur notre application de substitution des aliments."
home_user_msg = "Lancement de l'interface utilisateur\n      <<APPUYEZ SUR ENTREE>>>"
leaving = "Merci d'avoir utiliser notre application! A bientôt !"


#Questions
q1 = "==>   Veuillez choisir parmi les options suivantes :\n\
            (Entrez un nombre)\n"
q2 = "==>   Voici les différentes méthodes de recherche :\n"
q3 = "==>   Veuillez choisir parmi les catégories suivantes :\n"
q3_1 = "==> Veuillez sélectionner l'identifiant du produit de votre choix :"
q4 = "==>   Veuillez indiquer le nom de l'aliment à substituer :\n"

#Choices
c1 = ["Remplacer un aliment.", "Retrouver mes aliments substitués.", "Quitter."]
c2 = ["Choisir en fonction de la catégorie.", "Choisir en fonction de l'aliment.", "Retour au menu principal.", "Quitter."]
c3 = ["Snacks.","Pâtes.", "Boissons.", "Pizzas.", "Retour au menu principal.", "Quitter."]
c3_1 = []
c4 = ["", "Retour au menu principal.", "Quitter."]

#Answers
ans_1 = "\nVotre choix : "
ans_2 = "\nVotre méthode : "
ans_3 = "\nVotre catégorie : "
ans_4 = "\nVotre aliment : "

questioner = {
    q1 : [c1, ans_1],
    q2 : [c2, ans_2],
    q3 : [c3, ans_3],
    q3_1 : [c3_1, ans_4],
    q4 : [c4, ans_4]
}

dict_action = ["Quitter.","Remplacer un aliment.","Retrouver mes aliments substitués.",\
                "Retour au menu principal.","Par catégorie.","Par aliment.","Snacks.",\
                "Pâtes.","Boissons.","Pizzas." ]