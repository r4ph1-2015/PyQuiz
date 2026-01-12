import time, sys
global Correct
global Questions
Correct = 0
Questions = 10
def retryq1(user):
 mood = input(f"How are you,{user}? ")
 if mood in ["Good","good","fine","Fine","amazing","Amazing","GOOD","FINE","AMAZING"]:
    print("Thats Great!")
    q2(user, Correct)
 elif mood == "No":
    print(f"Thats Sad! I hope you feel better soon,{user}")
    q2(user, Correct)
 else:
    print ("My Programming doesnt understand your text, Please Try Again!")
    retryq1(user)
def q2(user, Correct):
 answer = input("What is 12x12? ")
 if answer == "144":
    Correct = Correct + 1
    print ("Correct Answer, 12x12 is 144!")
    print (f"{Questions - Correct}/{Questions} Questions remaining, Score: {Correct}")
    q3(Correct, Questions)
 else:
    print(f"Sorry, Your Answer was {answer}, Please try again")
    print (f"{Questions - Correct}/{Questions} Questions remaining, Score: {Correct}")
    q2(user, Correct)
def q3(Correct, Questions):
 answer = input("What is the Easiest Coding Languages? ")
 if answer in ["Python","python","PYTHON"]:
    Correct = Correct + 2
    print("Thats Correct, Python is described as One of easiest programming languages, and is used in many projects!")
    print (f"{Questions - Correct}/{Questions} Questions remaining, Score: {Correct}")
    q4(Correct, Questions)
 else:
  if answer in ["Html","CSS","Javascript","Typescript","html","css","javascript","typescript","HTML","CSS","JAVASCRIPT","TYPESCRIPT","Scratch","scratch","SCRATCH"]:
      Correct = Correct + 1
      print("That is partially correct, but They are not described as a full programming language such as Java,Python,Powershell,C++")
      print (f"{Questions - Correct}/{Questions} Questions remaining, Score: {Correct}")
      q4(Correct, Questions) 
  else:
      print(f"Sorry, Your Answer was {answer}, Please Try Again!")
      print (f"{Questions - Correct}/{Questions} Questions remaining, Score: {Correct}")
      q3(Correct, Questions)
def q4(Correct, Questions):
 answer = input("What is the capital of France? ")
 if answer in ["Paris","paris","PARIS"]:
    Correct = Correct + 1
    print (f"{Questions - Correct}/{Questions} Questions remaining, Score: {Correct}")
    q5(Correct, Questions)
 else:
    print(f"Sorry, Your Answer was {answer}, Please Try Again!")
    print (f"{Questions - Correct}/{Questions} Questions remaining, Score: {Correct}")
    q4(Correct, Questions)
def q5(Correct, Questions):
 answer = input("What is the largest planet in our solar system? ")
 if answer in ["Jupiter","jupiter","JUPITER"]:
    Correct = Correct + 1
    print("Correct!, Jupiter is the largest planet in our solar system.")
    print (f"{Questions - Correct}/{Questions} Questions remaining, Score: {Correct}")
    q6(Correct, Questions)
 else:
    print(f"Sorry, Your Answer was {answer}, Please Try Again!")
    print (f"{Questions - Correct}/{Questions} Questions remaining, Score: {Correct}")
    q5(Correct, Questions)
def q6(Correct, Questions):
 answer = input("What is the chemical symbol for water? ")
 if answer in ["H2O","h2o","H2o"]:
    Correct = Correct + 1
    print("Correct!, H2O is the chemical symbol for water.")
    print (f"{Questions - Correct}/{Questions} Questions remaining, Score: {Correct}")
    q7(Correct, Questions)
 else:
    print(f"Sorry, Your Answer was {answer}, Please Try Again!")
    print (f"{Questions - Correct}/{Questions} Questions remaining, Score: {Correct}")
    q6(Correct, Questions)
def q7(Correct, Questions):
 answer = input("How old is the Creator of PyQuiz?")
 if answer in ["11","eleven","Eleven","ELEVEN"]:
    Correct = Correct + 1
    print("Correct!, The Creator of PyQuiz is 11 years old.")
    print (f"{Questions - Correct}/{Questions} Questions remaining, Score: {Correct}")
    q8(Correct, Questions)
 else:
    print(f"Sorry, Your Answer was {answer}, Please Try Again!")
    print (f"{Questions - Correct}/{Questions} Questions remaining, Score: {Correct}")
    q7(Correct, Questions)
def q8(Correct, Questions):
 answer = input("What is the square root of 144? ")
 if answer == "12":
    Correct = Correct + 1
    print("Correct!, The square root of 144 is 12.")
    print (f"{Questions - Correct}/{Questions} Questions remaining, Score: {Correct}")
    q9(Correct, Questions)
 else:
    print(f"Sorry, Your Answer was {answer}, Please Try Again!")
    print (f"{Questions - Correct}/{Questions} Questions remaining, Score: {Correct}")
    q8(Correct, Questions)
def q9(Correct, Questions):
 answer = input("What is the capital of Japan? ")
 if answer in ["Tokyo","tokyo","TOKYO"]:
    Correct = Correct + 1
    print("Correct!, The capital of Japan is Tokyo.")
    print (f"{Questions - Correct}/{Questions} Questions remaining, Score: {Correct}")
    q10(Correct, Questions, user)
 else:
    print(f"Sorry, Your Answer was {answer}, Please Try Again!")
    print (f"{Questions - Correct}/{Questions} Questions remaining, Score: {Correct}")
    q9(Correct, Questions)
def q10(Correct, Questions, user):
 answer = input("If 16 is x, then what is the square root of 2x? ")
 if answer == "6":
    Correct = Correct + 1
    print("Correct!, The square root of 2x when x is 16 is 6.")
    print (f"{Questions - Correct}/{Questions} Questions remaining, Score: {Correct}")
    print (f"Quiz Complete! Your Final Score is {Correct}/{Questions}")
    print (f"Thanks for Playing, {user}!")
 else:
    print(f"Sorry, Your Answer was {answer}, Please Try Again!")
    print (f"{Questions - Correct}/{Questions} Questions remaining, Score: {Correct}")
    q10(Correct, Questions)

print ("Hi")
print ("Welcome to PyQuiz, A Python Based Quiz Game!")
user = input("What is your Name?")
retryq1(user)

