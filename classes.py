'''Classes used throughout project'''
'''I create a list called "questions_multiple_choice" which has a list of questions followed by 4 possible answers, labelled a, b, c, and d. Then I will assign each question in that list to the "multiple_choice" input of my "Questions" class'''
class Questions:                                       # Creating a class called Question.
    def __init__(self, multiple_choice, answer):       # Creating a method for this class, multiple choice and answer.
        self.multiple_choice = multiple_choice         # Establishing the multiple_choice attibute.
        self.answer = answer                           # Establishing the answer attibute.
        