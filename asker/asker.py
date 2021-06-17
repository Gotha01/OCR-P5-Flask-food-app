# -*- coding: utf-8 -*-

from os import system

import question as qst
import constants as cst
import products as pdt


class Asker_p5:
    def __init__(self):
        self.go = True
        self.dict_term = {
            "Quitter." : self.leave_Loop, 
            "Remplacer un aliment." : self.remove_aliment,
            "Retrouver mes aliments substitués." : self.show_already_remove_products,
            "Retour au menu principal." : self.asker_Loop,
            "Choisir en fonction de la catégorie." : self.select_category,
            "Choisir en fonction de l'aliment." : self.print_something,
            "Snacks." : self.find_five,
            "Pâtes." : self.find_five, 
            "Boissons." : self.find_five, 
            "Pizzas." : self.find_five
            }
        self.home_user()
        self.asker_Loop()

    def print_something(self):
        print("something")
        self.go = False

    def home():
        qst.Question(cst.home_msg, clean=1)
        system('cls')
        
    def home_user(self):
        qst.Question(cst.home_user_msg, clean=1)
    
    def leave_Loop(self):
        print(cst.leaving)
        self.go = False
        
    def remove_aliment(self):
        self.answer = qst.Question(cst.questioner, cst.q2, clean=1).answer
        return self.answer

    def select_category(self):
        self.answer = qst.Question(cst.questioner, cst.q3, clean=1).answer
        return self.answer

    def find_five(self):
        lower_category = self.answer.lower()
        use_category = lower_category.replace(".","")
        best_five = pdt.Product.check_for_five_products(use_category)
        for element in best_five:
            cst.c3_1.append(element[0])
        cst.c3_1.append("Retour au menu principal.")
        cst.c3_1.append("Quitter.")
        self.answer = qst.Question(cst.questioner, cst.q3_1, clean=1).answer
        return self.answer
        
    def show_already_remove_products(self):
        pass

    def asker_Loop(self):
        first_question = qst.Question(cst.questioner, cst.q1, clean=1).answer
        while self.go:
            for element in self.dict_term:
                if element == first_question:
                    first_question = self.dict_term[element].__call__()