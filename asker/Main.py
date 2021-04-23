# -*- coding: utf-8 -*-

from question import Question_m
from constant import *
import requests as rqs
import os


os.system('cls')
input(Phrase_accueil)
os.system('cls')
while True:
    question_1 = str(Question_m(ask_1, choice_1, ans_1))
    if question_1 == choice_1[0]:
        os.system('cls')
        break
    elif question_1 == choice_1[1]:
        os.system('cls')
        question_2 = str(Question_m(ask_2, choice_2, ans_2))
        if question_2 == choice_2[0]:
            os.system('cls')
            continue
        elif question_2 == choice_2[1]:
            os.system('cls')
            question_3 = str(Question_m(ask_3, choice_3, ans_3))
            if question_3 == choice_3[0]:
                os.system('cls')
                continue
            elif question_3 == choice_3[1]:
                os.system('cls')
                print(f"recherche des snacks dans la base de données")
                continue
            elif question_3 == choice_3[2]:
                os.system('cls')
                print(f"recherche des pates dans la base de données")
                continue
            elif question_3 == choice_3[3]:
                os.system('cls')
                print(f"recherche des boissons dans la base de données")
                continue
            elif question_3 == choice_3[4]:  
                os.system('cls')
                print(f"recherche des pizzas dans la base de données")
                continue
        elif question_2 == choice_2[2]:
            break
        elif question_2 == choice_2[3]:
            break
    elif question_1 == choice_1[2]:
        print('f')
input(leaving)
    
    #    while True:    
        
    #if question_1_0 == choice_accueil[0]:
    #    os.system('cls')
    #    break 
    #elif question_1_0 == choice_accueil[1]: 
    #    while True:    
    #        os.system('cls')
    #        question_1_2 = str(Question_m(question_phase2, choice_phase2, question_1_2_return))
    #        if question_1_2 == choice_phase2[0]:
    #            os.system('cls') 
    #            continue
     #       elif question_1_2 == choice_phase2[1]:
      #          os.system('cls')
       #         question_category = str(Question_m(question_cat_choice, choice_cat, question_cat_return))
        #        break
         #   elif question_1_2 == choice_phase2[2]:
          #      os.system('cls')
           #     question_aliment = str(Question_m(question_ali_choice, choice_ali, question_ali_return))
            #    break
            #elif question_1_2 == choice_phase2[3]:
             #   os.system('cls')
              #  break
    #elif question_1_0 == choice_accueil[2]:
    #break