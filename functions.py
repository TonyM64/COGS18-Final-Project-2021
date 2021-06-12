#This function checks that the input for the question equals the value of correct answer
#Value would be a answer to the multiple choice question
def multiple_choice(value):
    """This function checks that the input for the question equals the value of correct answer.
    
    Parameters
    ----------
    The input is the valeu of the correct answer.
        
    Returns
    -------
    Returns an integer, each correct answer adds a point to your score.
    """ 
    yes = 0
    if value == input('Question 0'):
        value = b
        yes =+1
        return yes
    if value == input('Question 1'):
        value = a
        yes =+1
        return yes
    if value == input('Question 2'):
        value = d
        yes =+1
        return yes
    if value == input('Question 3'):
        value = c
        yes =+1
        return yes
    if value == input('Question 4'):
        value = a
        yes =+1
        return yes
    if value == input('Question 5'):
        value = d
        yes =+1
        return yes
    if value == input('Question 6'):
        value = a
        yes =+1
        return yes
    if value == input('Question 7'):
        value = d
        yes =+1
        return yes
    if value == input('Question 8'):
        value = b
        yes =+1
        return yes
    if value == input('Question 9'):
        value = c
        yes =+1
        return yes
        
#A function named maximum_score takes in their score as input and gives a message depending on how many questions they got right.
def maximum_score(score):  
    """A function named maximum_score takes in their score as input and gives a message depending on how many questions they got right.
    
    Parameters
    ----------
    Takes in their score as input
        
    Returns
    -------
    Gives a message depending on how many questions they got right
    """ 
    # using if statement to display a message if score is equal to 0.
    if score == 0:               
        print("You Yamcha'd!")
        return score
    # using if statement to display a message if score is equal to 1.
    elif score == 1:             
        print("You've had 30 years to read or see this!")
        return score
    # using if statement to display a message if score is equal to 2.
    elif score == 2:             
        print("Hey! You scored the same number as Goku's power level, as a baby.")
        return score
    # using if statement to display a message if score is equal to 3
    elif score == 3:             
        print("Don't give up! Goku has died 3 times.")
        return score
    # using if statement to display a message if score is equal to 4.
    elif score == 4:           
        print("You got the legendary 4 star dragon ball.") 
        return score
    # using if statement to display a message if score is equal to 5.
    elif score == 5:             
        print("Well... You're halfway there.")
        return score
    # using if statement to display a message if score is equal to 6.
    elif score == 6:             
        print("You got above average, but there's no curve. Try again!")
        return score
    # using if statement to display a message if score is equal to 7.
    elif score == 7:             
        print("Same number of dragon balls, in case you didn't know.")
        return score
    # using if statement to display a message if score is equal to 8.
    elif score == 8:             
        print("Ok. Ok, you're almost there!")
        return score
    # using if statement to display a message if score is equal to 9.
    elif score == 9:             
        print("Almost there, when you fall off the horse, you get back up and You Eat! That! Horse!")
        return score
    # using if statement to display a message if score is equal to 10.
    elif score == 10:            
        print("You're knowledge of this series is MAXIMUM!")
        return score
        
# Making a function, called "begin_test" that takes "questions" from above as an input.
def begin_test(questions):
    """Making a function, called "begin_test" that takes "questions" from above as an input.
    
    Parameters
    ----------
    Takes "questions" from the Notebook as an input and begins to run the test
        
    Returns
    -------
    Returns a unique message to you depending on how many points you got correct out of 10
    """ 
    # Assigning a base value of 0 to Score.
    score = 0 
    
    # Using for loop to loop through q in questions.
    for q in questions:
        
        # Stating that answer is equal to the input of q in multiple choice.
        answer = input(q.multiple_choice)
       
        # Using if statement to show if user's answer is equal to the chosen answer in questions above:
        if answer == q.answer:
            
            # If answer is correct, it adds 1 to total score value. 
            score = score + 1
        else:
            continue

              
    #Print a statement at the end of the quiz, showing the total number of correct answers.
    print("Hey! You got " + str(score) + "/" + str(len(questions)) + " correct!") 
    
    # Finally, it runs maximum_score function with score as input to display a unique message.
    maximum_score(score)            