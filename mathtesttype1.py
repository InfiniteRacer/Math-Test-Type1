def menu():

    #Introduction section

    print("Welcome to the menu!")

    print("")

    print("Press '1' to start the test.") #Give the options as a print statement
    print("Press '2' to view the rules / how to play.")
    print("Press '3' to stop the program.")

    print("")

    startup=input("Choose an option and enter number here: ") #Enter option here
    
    if startup == '1': #Setup if and elif
        print("")
        print("Test section selected.")
        print("")
        test() #send to this defined section
    elif startup == '2':
        print("")
        print("Rule section selected.")
        print("")
        rules() 
    elif startup == '3':
        print("")
        print("Program has been stopped.")
        exit() #end program
        
def rules():
    
    print("Rules and key points:") #Print rules
    print("- You must score 5 or over to pass.")
    print("- You may take the test again if you fail.")
    print("- Do NOT use commas, only the numbers. Example: 5000 NOT 5,000.")
    print("- To enter a answer, type it next to the question and click enter.")
    
    print("")
    
    rulescheckpoint=input("Finished? (Enter anything) ") #checkpoint
    
    print("")
    
    menu() #send back to menu
        
def test():
    
    global score
    global correct
    
    score = 0 #Default score
    correct = 1 #Points if question is correct
    
    print("Test will start now")
    
    testcheckpoint=input("Start? (Enter anything) ") #checkpoint
    
    question1=input("60 x 100? ") #Asks question and gives input option to user

    question1ans = '6000' #Answer assigned to a variable name

    if question1 == question1ans:
        print("")
        score = score + correct #Adds a point to total score
        print("Correct! Your score currently: " + str(score)) #States amount of points
        print("")
    else:
        print("")
        print("Your answer is wrong! It was " +question1ans)
        print("Your score currently: " +str(score))
        print("")
        
    question2=input("60 x 200? ")

    question2ans = '12000'

    if question2 == question2ans:
        print("")
        score = score + correct
        print("Correct! Your score currently: " + str(score))
        print("")
    else:
        print("")
        print("Your answer is wrong! It was " +question2ans)
        print("Your score currently: " +str(score))
        print("")
        
    question3=input("800 x 400? ")

    question3ans = '320000'

    if question3 == question3ans:
        print("")
        score = score + correct
        print("Correct! Your score currently: " + str(score))
        print("")
    else:
        print("")
        print("Your answer is wrong! It was " +question3ans)
        print("Your score currently: " +str(score))
        print("")
        
    question4=input("560 x 980? ")

    question4ans = '548800'

    if question4 == question4ans:
        print("")
        score = score + correct
        print("Correct! Your score currently: " + str(score))
        print("")
    else:
        print("")
        print("Your answer is wrong! It was " +question4ans)
        print("Your score currently: " +str(score))
        print("")
    
    question5=input("750 x 6400? ")

    question5ans = '4800000'

    if question5 == question5ans:
        print("")
        score = score + correct
        print("Correct! Your score currently: " + str(score))
        print("")
    else:
        print("")
        print("Your answer is wrong! It was " +question5ans)
        print("Your score currently: " +str(score))
        print("")
        
    question6=input("800 x 9800? ")

    question6ans = '7840000'

    if question6 == question6ans:
        print("")
        score = score + correct
        print("Correct! Your score currently: " + str(score))
        print("")
    else:
        print("")
        print("Your answer is wrong! It was " +question6ans)
        print("Your score currently: " +str(score))
        print("")
        
    question7=input("5400 x 63000? ")

    question7ans = '340200000'

    if question7 == question7ans:
        print("")
        score = score + correct
        print("Correct! Your score currently: " + str(score))
        print("")
    else:
        print("")
        print("Your answer is wrong! It was " +question7ans)
        print("Your score currently: " +str(score))
        print("")
    
    question8=input("890 x 4355? ")

    question8ans = '3875950'

    if question8 == question8ans:
        print("")
        score = score + correct
        print("Correct! Your score currently: " + str(score))
        print("")
    else:
        print("")
        print("Your answer is wrong! It was " +question8ans)
        print("Your score currently: " +str(score))
        print("")
        
    question9=input("860 x 5350? ")

    question9ans = '4601000'

    if question9 == question9ans:
        print("")
        score = score + correct
        print("Correct! Your score currently: " + str(score))
        print("")
    else:
        print("")
        print("Your answer is wrong! It was " +question9ans)
        print("Your score currently: " +str(score))
        print("")
        
    print("Last question!")
    
    print("")
        
    question10=input("25100 x 600? ")

    question10ans = '15060000'

    if question10 == question10ans:
        print("")
        score = score + correct
        print("Correct! Your score currently: " + str(score))
        print("")
    else:
        print("")
        print("Your answer is wrong! It was " +question10ans)
        print("Your score currently: " +str(score))
        print("")
        
    print("Test complete!") #States test it complete
    
    print("")
    
    endtestcheckpoint=input("Check results? (Enter anything) ") #Checkpoint
    
    testresultmenu() #Takes to next section
    
def testresultmenu():
    
    global status
    
    print("")
    
    print("Well done for completing the test!")
    
    print("")
    
    print("Your final score is: " +str(score)) #Printsfinal score
    
    print("")
    
    status = ''

    if score < 5: #Finds if status is pass or fail
        status = 'Fail'
    elif score > 5:
        status = 'Pass'

    print("")

    print("Your status is: " +status) #states his/hers status
    
    resultmenucheckpoint=input("Back to menu? (Enter anything) ") #Checkpoint
    
    print("")
    
    menu()
    
menu() #Starts the program in the menu