# -*- coding: utf-8 -*-


from os import system

from question import Question
from constants import *
from products import Product
from categories import Categories
from favourites import Favourites
from display import display

class Asker:
    def __init__(self):
        self.go = True
        self.dict_term = {
            MAIN_MENU : self.home_question,
            C1[0] : self.remove_product,
            C1[1] : self.display_favorite,
            C1[2] : self.leave_Loop,
            C2[0] : self.select_category,
            C2[1] : self.search_product_to_replace,
            C3[0] : self.search_products_like_category,
            C3[1] : self.search_products_like_category,
            C3[2] : self.search_products_like_category,
            C3[3] : self.search_products_like_category
            }
        self.home_user()
        self.asker_Loop()

    def display_details(self, product):
        system("cls")
        store_prod = product[4].replace("[", "").replace("]", "")
        input(display(150, "=", [f"Produit favoris : {product[1]}",
            "Description : ", f"{product[5]}",
            "Valeur nutritionnelle : ", f"{product[3]}",
            "URL : ", f"{product[6]}",
            "Magasins : ", f"""{store_prod.replace(",", ", ")}"""],
            1,"|"))

    def home():
        #Function to print home message before database init.
        Question(display(150, "=", HOME_MESSAGE, 3, "|"), clean=1)
        system('cls')
        
    def home_user(self):
        #Function to start user interactions.
        Question(display(150, "=", HOME_USER_MESSAGE, 3, "|"), clean=1)

    def home_question(self):
        first_question = Question(QUESTIONER, Q1, clean=1).answer
        return first_question   

    def leave_Loop(self):
        #Function to leave "Asker loop".
        Question(display(150, "=", LEAVING, 2, "|"), clean=1)
        self.go = False

    def remove_product(self):
        #Function to choose how to search for a product.
        self.answer = Question(QUESTIONER, Q2, clean=1).answer
        return self.answer

    def select_category(self):
        #Function to choose a category.
        self.answer = Question(QUESTIONER, Q3, clean=1).answer
        return self.answer

    def ask_found_better(self, category_id):
        better_prod = Question(QUESTIONER, Q6, 1).answer
        if better_prod == "Oui.":
            C_EMPTY.clear()
            prod_search = Product.display_product(
                ["name_product", "id_product"], 
                 "category_ID", category_id[0],
                 order_by="nutrition_grades_product", numlimit="5")
            for found_prod in prod_search:
                C_EMPTY.append(found_prod[0])
            fav_prod = Question(QUESTIONER, Q6_1, 1).answer
            fav_prod_details = Product.display_product(["*"], "name_product", fav_prod)[0]
            self.display_details(fav_prod_details)
            C_EMPTY.clear()
            return fav_prod_details[0]
        else:
            return MAIN_MENU

    def ask_add_favourite(self, favourite, substituted):
        answer = Question(QUESTIONER, Q8, 1).answer
        if answer == "Oui.":
            Favourites.record_product(favourite, substituted)
            system("cls")
            input(display(150, "=", ["Produits enregistrés aux favoris.",
              "Appuyez sur 'entrée' pour revenir au menu principal."], 2, "|"))
            return MAIN_MENU  
        else:
            return MAIN_MENU

    def search_products_like_category(self):
        cat_prod_dict = {}
        category_to_check = self.answer.lower().replace(".","")
        category_id = Categories.read_column_sql("id", f"WHERE name='{category_to_check}'")
        cat_products = Product.display_product(["name_product", "id_product"], 'category_ID', category_id[0])
        for element in cat_products:
            cat_prod_dict[element[0]] = element[1]
            C_EMPTY.append(element[0])
        first_question = Question(QUESTIONER, Q3_1, clean=1).answer
        choiced_product = Product.display_product(["*"], "id_product",
            f"{cat_prod_dict[first_question]}")[0]
        C_EMPTY.clear()
        self.display_details(choiced_product)
        ids = self.ask_found_better(category_id)
        if ids != MAIN_MENU:
            self.ask_add_favourite(ids, choiced_product[0])
        return MAIN_MENU
              
    def search_product_to_replace(self):
        correct_product = True
        while correct_product:
            product_to_replace = Question(display(150, "=", REPLACE_PROD,
                                                  2, "|", "left"),
                                          clean=1).answer
            if len(product_to_replace) >= 3:
                prod_find = Product.display_product(
                    ["name_product, nutrition_grades_product"],
                    'name_product', "%" + product_to_replace + "%")
                if prod_find != []:
                    for element in prod_find:
                        C_EMPTY.append(element[0])
                    C_EMPTY.append(MAIN_MENU)
                    favourite_prod = Question(QUESTIONER, Q5, clean=1).answer
                    if favourite_prod != MAIN_MENU:
                        choiced_product = Product.display_product(["*"],
                            "name_product", favourite_prod)[0]
                        self.display_details(choiced_product)
                        ids = self.ask_found_better(str(choiced_product[2]))
                        if ids != MAIN_MENU:
                            rec = self.ask_add_favourite(ids, choiced_product[0])
                            return MAIN_MENU
                        else:
                            return MAIN_MENU
                    else:
                        return MAIN_MENU
                else:
                    no_product = Question(QUESTIONER, Q7, 1).answer
                    if no_product == "Réessayer.":
                        continue
                    else :
                        return no_product
            else:
                system("cls")
                input(display(150, "=", SEARCHING_RULE, 2, "|"))

    def display_favorite(self):
        system("cls")
        all_fav = Favourites.display_all_favourite_product()
        element_to_search = {}
        if all_fav != []:
            for element in all_fav:
                element_to_search[element[0]] = element[1]
                C_EMPTY.append(Product.display_product(
                                                    ["name_product"], 
                                                    "id_product", 
                                                    element[0]
                                                    )[0][0])
            C_EMPTY.append(MAIN_MENU)
            C_EMPTY.append(SUPRESS)
            qst_all_fav = Question(QUESTIONER, Q5, 1).answer
            if qst_all_fav != SUPRESS and qst_all_fav != MAIN_MENU:
                favourite_prod = Product.display_product(
                                    ["id_product"],
                                    "name_product", 
                                    qst_all_fav
                                    )[0][0]
                Favourites.display_favourite_product(
                    str(favourite_prod),
                    str(element_to_search[favourite_prod])
                    )
                all_fav.clear()
                C_EMPTY.clear()
            elif qst_all_fav == SUPRESS:
                Favourites.suppress_all()
                all_fav.clear()
                C_EMPTY.clear()
                return MAIN_MENU
            elif qst_all_fav == MAIN_MENU:
                C_EMPTY.clear()
                return MAIN_MENU
        else:
            Question(display(150, "=", NO_FAV_PRODUCT, 1, "|", "left"), clean=1)
        return MAIN_MENU

    def asker_Loop(self):
        #Main loop
        first_question = self.home_question()
        while self.go:
            for element in self.dict_term:
                if element == first_question:
                    first_question = self.dict_term[element].__call__()