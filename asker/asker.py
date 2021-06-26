# -*- coding: utf-8 -*-

from favourites import Favourites
from os import system
from question import Question
from constants import *
from products import Product
from categories import Categories


class Asker_p5:
    def __init__(self):
        self.go = True
        self.dict_term = {
            "Quitter." : self.leave_Loop,
            "Retour au menu principal." : self.home_question,
            "Remplacer un aliment." : self.remove_aliment,
            "Retrouver mes aliments substitués." : self.show_already_remove_products,
            "Retrouver mes produits favoris." : self.display_favorite,
            "Choisir en fonction de la catégorie." : self.select_category,
            "Choisir en fonction de l'aliment." : self.search_product_to_replace,
            "Snacks." : self.search_five_products_like_category,
            "Pates." : self.search_five_products_like_category,
            "Boissons." : self.search_five_products_like_category,
            "Pizzas." : self.search_five_products_like_category
            }
        self.home_user()
        self.asker_Loop()

    def home():
        #Function to print home message before database init.
        Question(home_msg, clean=1)
        system('cls')
        
    def home_user(self):
        #Function to start user interactions.
        Question(home_user_msg, clean=1)
    
    def leave_Loop(self):
        #Function to leave "Asker loop".
        print(leaving)
        self.go = False
        
    def remove_aliment(self):
        #Function to choose how to search for a product.
        self.answer = Question(questioner, q2, clean=1).answer
        return self.answer

    def select_category(self):
        #Function to choose a category.
        self.answer = Question(questioner, q3, clean=1).answer
        return self.answer

    def search_five_products_like_category(self):
        category_to_check = self.answer.lower().replace(".","")
        category_id = Categories.read_column_sql("id", f"WHERE name='{category_to_check}'")
        five_products = Product.display_product(["name_product"], 'category_ID', category_id[0], "nutrition_grades_product", "5", "ASC")
        for element in five_products:
            c3_1.append(element[0])
        first_question = Question(questioner, q3_1, clean=1).answer
        favourite = Product.display_product(["*"], "name_product", first_question)[0]
        system("cls")
        input(f"""Vous avez choisi :\n   {favourite[1]}\
            \nDescription :\n    {favourite[5]}\
            \nURL :\n    {favourite[6]}\
            \nMagasins :\n    {favourite[4].replace("[", "").replace("]", "").replace(",", ", ")}\
            \n\nRetour au menu principal.\
            \nCe aliment a été ajouté à vos favoris.""")
        Favourites.record_aliment(favourite[0],favourite[2])
        c3_1.clear()
        return "Retour au menu principal."
        
    def display_favorite(self):
        all_fav = Favourites.display_all_favourite_product()
        for element in all_fav:
            c5.append(Product.display_product(["name_product"], "id_product", element[0])[0][0])
        qst_all_five = Question(questioner, q5, 1).answer
        favourite = Product.display_product(["*"], "name_product", qst_all_five)[0]
        system("cls")
        input(f"""Vous avez choisi :\n   {favourite[1]}\
            \n\nDescription :\n    {favourite[5]}\
            \n\nURL (maintenez 'ctrl' et cliquez sur le lien pour vous rendre sur la page du produit) :\n    {favourite[6]}\
            \n\nMagasins :\n    {favourite[4].replace("[", "").replace("]", "").replace(",", ", ")}\
            \n\n\n Appuyez sur entrée pour revenir au menu principal""")
        c5.clear()
        return "Retour au menu principal."

    def home_question(self):
        first_question = Question(questioner, q1, clean=1).answer
        return first_question

    def search_product_to_replace(self):
        product_to_replace = Question("Entrez le nom du produit que vous souhaitez remplacer :", "Vous voulez trouver un remplaçant au produit :", 1).answer
        prod_find = Product.display_product(["name_product"],'name_product', "%" + product_to_replace + "%", "nutrition_grades_product", "5", "ASC")
        print(prod_find)
        for element in prod_find:
            c5.append(element[0])
        substituted_prod = Question(questioner, c5, 1)

    def show_already_remove_products(self):
        #Function to find previously replaced products
        pass

    def asker_Loop(self):
        #Main loop
        first_question = self.home_question()
        while self.go:
            for element in self.dict_term:
                if element == first_question:
                    first_question = self.dict_term[element].__call__()
Asker_p5()