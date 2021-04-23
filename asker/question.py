# -*- coding: utf-8 -*-


class Question_m:
    """Object who returns an answer for a multiple choices question"""
    def __init__(self, questions, choices, return_choice):
        """initialize a question"""
        self.questions = questions
        self.return_choice = return_choice
        self.choices = []
        if type(choices) is list:
            for element in choices:
                self.choices.append(element)

    def __str__(self):
        """return your question"""
        choiceslen = len(self.choices)
        print(f"{self.questions}")
        for element in self.choices:
            print(element)
        while True:
            try:
                answer = int(input(self.return_choice))
                if answer in range(0, choiceslen):
                    return self.choices[answer]
                else:
                    print("Please, choose a number in the list!")
            except ValueError:
                print("Please, choose a number in the list!")