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
  Correct = Correct + 1
  print("Thats Correct, Python is described as One of easiest programming languages, and is used in many projects!")
  print (f"{Questions - Correct}/{Questions} Questions remaining, Score: {Correct}")  
 else:
  if answer in ["Html","CSS","Javascript","Typescript","html","css","javascript","typescript","HTML","CSS","JAVASCRIPT","TYPESCRIPT"]:
   Correct = Correct + 1
   print("That is partially correct, but They are not described as a full programming language such as Java,Python,Powershell,C++")
   print (f"{Questions - Correct}/{Questions} Questions remaining, Score: {Correct}")
  else:
   print(f"Sorry, Your Answer was {answer}, Please Try Again!")
   print (f"{Questions - Correct}/{Questions} Questions remaining, Score: {Correct}")
   q3(Correct, Questions)

print ("Hi")
user = input("What is your Name?")
retryq1(user)