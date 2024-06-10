print("Pop Quiz Time!")
    

print("Does Pineapple Go On Pizza?")
pizza_awnser = input("Enter answer: ")
if pizza_awnser == "no":
    score = 1
print("- - - - - - - - - -")


print("Are Tacos the GOAT?")
taco_awnser = input("Enter answer: ")
if taco_awnser == "yes":
    score += 1
print("- - - - - - - - - -")


print("What is bigger, Earth or the Moon?")
planet_answer = input("Enter answer: ")
if planet_answer == "earth":
    score += 1
print("- - - - - - - - - -")


print("What is the powersource for coders?")
code_answer = input("Enter answer: ")
if code_answer == "caffine":
    score += 1
print("- - - - - - - - - -")


print("You Got", score, "Out of 4 Correct")