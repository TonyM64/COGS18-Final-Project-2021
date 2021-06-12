#In order to be able to test my functions, I first need to import them from the "functions" file.
from functions import maximum_score 
from functions import begin_test
from functions import multiple_choice

# This will test the begin_test function
'''For this function test, I recieved help from a student named Caitlin. She helped me in understanding mock and helped me code this test.''' 
from unittest import mock
from unittest import TestCase
import functions
from classes import Questions

class DictCreateTests(TestCase):
    @mock.patch('functions.input', create=True)
    def test_begin_test(self, mocked_input):
        mocked_input.side_effect = ['b', 'a', 'd', 'c', 'a', 'd', 'a', 'd', 'b', 'c']
        questions_multiple_choice = ["What race is Goku?\n(a) Namekian\n(b) Saiyan\n(c) Earthling\n(d) Kryptonian\n\n",
                             "What path leads to King Kai's house?\n(a) Snake Way\n(b) Tiger Path\n(c) The Yellow Brick Road\n(d) Dragon Road\n\n",
                             "Who was the second person to kill Goku?\n(a) Raditz\n(b) Vegeta\n(c) Piccolo\n(d) Cell\n\n",
                             "Who created the dragon balls on Earth?\n(a) Grand Elder Guru\n(b) Supreme Kai\n(c) Kami\n(d) King Kai\n\n",
                             "What can be eaten to recover all wounds?\n(a) Senzu Beans\n(b) Dragon Balls\n(c) Steriods\n(d) Namekian Egg\n\n",
                             "How did imperfect Cell get stronger after arriving from the future?\n(a) Dragon Balls\n(b) Training\n(c) Solar Power\n(d) Absorbing Humans\n\n",
                             "Knowing he needed more power to fight the Androids, with whom did Piccolo fuse?\n(a) Kami\n(b) Goku\n(c) Thanos\n(d) Vegeta\n\n",
                             "What is the name of Vegeta's dad?\n(a) Bardock\n(b) Lord Frieza\n(c) Captain Ginyu\n(d) King Vegeta\n\n",
                             "What happens when a Saiyan with a tail sees the Moon?\n(a) Turns into a Werewolfe\n(b) Turn into a Great Ape\n(c) Nothing\n(d) Turns into a Sailor Scout\n\n",
                             "Who is the strongest character in the series?\n(a) Akira Toriyama\n(b) Whis\n(c) The Omni King\n(d) Beerus\n\n"]
        questions = [Questions(questions_multiple_choice[0],"b"),
            #Assigning the string in the 0 index from the "questions_multiple_choice", and assigning "d" as correct answer.
            Questions(questions_multiple_choice[1],"a"),
            #Assigning the string in the 1 index from the "questions_multiple_choice", and assigning "d" as correct answer. 
            Questions(questions_multiple_choice[2],"d"),
            #Assigning the string in the 2 index from the "questions_multiple_choice", and assigning "a" as correct answer. 
            Questions(questions_multiple_choice[3],"c"),
            #Assigning the string in the 3 index from the "questions_multiple_choice", and assigning "b" as correct answer. 
            Questions(questions_multiple_choice[4],"a"),
            #Assigning the string in the 4 index from the "questions_multiple_choice", and assigning "a" as correct answer. 
            Questions(questions_multiple_choice[5],"d"),
            #Assigning the string in the 5 index from the "questions_multiple_choice", and assigning "d" as correct answer. 
            Questions(questions_multiple_choice[6],"a"),
            #Assigning the string in the 6 index from the "questions_multiple_choice", and assigning "a" as correct answer. 
            Questions(questions_multiple_choice[7],"d"),
            #Assigning the string in the 7 index from the "questions_multiple_choice", and assigning "d" as correct answer. 
            Questions(questions_multiple_choice[8],"b"),
            #Assigning the string in the 8 index from the "questions_multiple_choice", and assigning "b" as correct answer. 
            Questions(questions_multiple_choice[9],"c")]
            #Assigning the string in the 9 index from the "questions_multiple_choice", and assigning "c" as correct answer.
        

        self.assertEqual(functions.begin_test(questions), None)
        


# This will test the maximum_score function. 
# First it will check if the function is callable and then check that the input score is a intager.
def test_maximum_score():
    assert callable(maximum_score)
    assert isinstance(maximum_score(10), int)
    
# This test is written for the multiple_choice function. 
# First it will check if the function is callable and then check that the input score is a intager.
def test_multiple_choice():
    assert callable(multiple_choice)
    assert isinstance(0, int)
    
'''Using what I learned from Caitlin about mock, I created my own mock test for my function multiple_choice.'''    
from unittest import mock
from unittest import TestCase
import functions
from classes import Questions

class DictCreateTests(TestCase):
    @mock.patch('functions.input', create=True)
    def test_multiple_choice(self, mocked_input):
        mocked_input.side_effect = ['b', 'a', 'd', 'c', 'a', 'd', 'a', 'd', 'b', 'c']
        self.assertEqual(functions.multiple_choice(0), None)
        
    
    


                 
    