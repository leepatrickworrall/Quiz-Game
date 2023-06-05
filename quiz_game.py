print("Welcome to the quiz!\n")

playing = input("Would you like to play? ")
score = 0

if playing.lower() != "yes":
    quit()

answer = input("What is the best condiment? ")

if answer == "Mayonnaise" or "mayonnaise" and "mayo":
    print("\nCongratulations. That is the right, and only answer.\n")
    score += 1

else:
    print("\nThat was the incorrect answer.\n")

answer = input("When was mayonnaise first invented? ")

if answer == "1756":
    print("\nCorrect.\n")
    score += 1

else:
    print("\nIncorrect.\n")

answer = input("Who asked if mayonnaise is an instrument? ")

if answer == "Patrick" or "patrick" and "Patrick Star":
    print("\nCorrect.\n")
    score += 1

else:
    print("\nIncorrect.\n")

print("That's the end of the quiz.\n")
print("You got " + str(score) + " questions correct!\n")
print("You got " + str((score / 3) * 100) + "%.")
