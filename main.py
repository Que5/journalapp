
date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10? ")
thoughts = input("Let your thoughts be known: \n")

with open(f'{date}.txt', 'w') as file:
    file.write(mood + '\n')
    file.write(thoughts)