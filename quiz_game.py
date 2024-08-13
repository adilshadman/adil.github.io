print("WELCOME TO PYTHON QUIZ")

playing=input("Do you want to play?\n")

if playing.lower()!="yes":
    quit()
    
print("Okay!lets play!")
score=0


answer=input("1.Who created python?\n")
if answer.lower()=="guido van rossum":
    print("Correct!")
    score+=1
else:
    print("Incorrect!\nThe correct answer is guido van rossum.")

answer=input("2.In which year python was created?\n")
if answer.lower()=="1991":
    print("Correct!")
    score+=1
else:
    print("Incorrect!\nThe correct answer is 1991.")

answer=input("3.What type language is python?\n")
if answer.lower()=="dynamically typed":
    print("Correct!")
    score+=1
else:
    print("Incorrect!\nThe correct answer is dynamically typed.")

answer=input("4.why python?\n")
if answer.lower()=="because python takes less coding time.":
    print("Correct!")
    score+=1
else:
    print("""Incorrect!\nThe correct answer is
because python takes less coding time.""")

answer=input("5.What is pythons translator name?\n")
if answer.lower()=="interpreter":
    print("Correct!")
    score+=1
else:
    print("Incorrect!\nThe correct answer is interpreter.")

print("Total correct answer is " + str(score) + " out of 5 questions")
print("You got " + str((score/5)*100) + "%.")

    
    
    









    
    


