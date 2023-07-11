import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

random_choice = random.randint(0, 2)
if random_choice == 0:
    random_game = rock
elif random_choice == 1:
    random_game = paper
else:
    random_game = scissors

my_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: ")
if my_choice in ['0', '1', '2']:
    my_choice = int(my_choice)
    if my_choice == random_choice:
        print(my_choice)
        if my_choice == 0:
            print("rock")
            print(rock)
        elif my_choice == 1:
            print("paper")
            print(paper)
        else:
            print("scissors")
            print(scissors)
        print(random_choice)
        if random_choice == 0:
            print("rock")
        elif random_choice == 1:
            print("paper")
        else:
            print("scissors")
        print(random_game)
        print("It is a draw")
    elif my_choice == 0 and random_choice == 1:
        print(my_choice)
        if my_choice == 0:
            print("rock")
            print(rock)
        elif my_choice == 1:
            print("paper")
            print(paper)
        else:
            print("scissors")
            print(scissors)
        print(random_choice)
        if random_choice == 0:
            print("rock")
        elif random_choice == 1:
            print("paper")
        else:
            print("scissors")
        print(random_game)
        print("You lose")
    elif my_choice == 1 and random_choice == 2:
        print(my_choice)
        if my_choice == 0:
            print("rock")
            print(rock)
        elif my_choice == 1:
            print("paper")
            print(paper)
        else:
            print("scissors")
            print(scissors)
        print(random_choice)
        if random_choice == 0:
            print("rock")
        elif random_choice == 1:
            print("paper")
        else:
            print("scissors")
        print(random_game)
        print("You lose")
    elif my_choice == 0 and random_choice == 2:
        print(my_choice)
        if my_choice == 0:
            print("rock")
            print(rock)
        elif my_choice == 1:
            print("paper")
            print(paper)
        else:
            print("scissors")
            print(scissors)
        print(random_choice)
        if random_choice == 0:
            print("rock")
        elif random_choice == 1:
            print("paper")
        else:
            print("scissors")
        print(random_game)
        print("You win")
    elif my_choice == 1 and random_choice == 0:
        print(my_choice)
        if my_choice == 0:
            print("rock")
            print(rock)
        elif my_choice == 1:
            print("paper")
            print(paper)
        else:
            print("scissors")
            print(scissors)
        print(random_choice)
        if random_choice == 0:
            print("rock")
        elif random_choice == 1:
            print("paper")
        else:
            print("scissors")
        print(random_game)
        print("You win")
    elif my_choice == 2 and random_choice == 0:
        print(my_choice)
        if my_choice == 0:
            print("rock")
            print(rock)
        elif my_choice == 1:
            print("paper")
            print(paper)
        else:
            print("scissors")
            print(scissors)
        print(random_choice)
        if random_choice == 0:
            print("rock")
        elif random_choice == 1:
            print("paper")
        else:
            print("scissors")
        print(random_game)
        print("You lose")
    elif my_choice == 2 and random_choice == 1:
        print(my_choice)
        if my_choice == 0:
            print("rock")
            print(rock)
        elif my_choice == 1:
            print("paper")
            print(paper)
        else:
            print("scissors")
            print(scissors)
        print(random_choice)
        if random_choice == 0:
            print("rock")
        elif random_choice == 1:
            print("paper")
        else:
            print("scissors")
        print(random_game)
        print("You win")
else:
    print("Irrelevant value provided for the choice. Please enter only 0, 1, or 2.")
