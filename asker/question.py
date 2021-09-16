# -*- coding: utf-8 -*-

from display import display
from os import system


class Question():
    def __init__(self, question, q_key="", clean=0):
        """Class which ask a question or a multiple choice question depending on the type of "question".

            Args:
                question (dict, str): if dict: question = {the_question : [[choices_list], "call_for_response"]}.
                                  if str : question = "the_question".
                q_key (str, optional): [description]. Defaults to "".
                clean (int, optional): [check if the terminal has to be cleaned before asking question]. Defaults to 0.
        """
        
        self.question = question
        self.q_key = q_key
        self.clean = clean
        if clean == 1:
            system("cls")
        if isinstance(self.question, str) or isinstance(self.question, list):
            self.answer = self.ask_question()
        elif isinstance(self.question, dict):
            self.answer = self.ask_multiple_choice_question()

    def ask_question(self):
        if isinstance(self.question, list):
            " ".split()
        print(self.question)  
        result = input("")
        return result  

    def ask_multiple_choice_question(self):
        for_display = [self.q_key]
        choices = self.question[self.q_key][0]
        for i, element in enumerate(choices, start=1):
            for_display.append(str(i) + "/ " +  element)
        print(display(150, "=", for_display, 1, "|", "left"))
        while True:
            try:
                choices_list = self.question[self.q_key][0]
                self.choice = int(input(self.question[self.q_key][1])) - 1
                if choices_list[self.choice]:
                    return str(choices_list[self.choice])
            except ValueError:
                print("S'il vous plait, choisissez un nombre figurant dans la liste!")
            except IndexError:
                print("S'il vous plait, choisissez un nombre figurant dans la liste!")