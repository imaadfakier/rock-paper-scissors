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

#print(rock)
#print(scissors)
#print(paper)

rpc_choices = [rock, paper, scissors]
#print(rpc_choices)

#my_rpc_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
#print(my_rpc_choice)
#while my_rpc_choice is not in [0, 1, 2]: <== SIDENOTE: Incorrect! (i.e. is must not be present)
my_rpc_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

while my_rpc_choice not in [0, 1, 2]:
  my_rpc_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

computer_rpc_choice = random.randint(0, 2)
#print(computer_rpc_choice)

# rock > scissors
# paper > rock
# scissors > paper
# ------------------------
# rock == rock
# paper == paper
# scissors == scissors

# rock wins
if (my_rpc_choice == 0 and computer_rpc_choice == 2):
  print(rpc_choices[my_rpc_choice] + "\n" + "Computer chose:" + "\n" + rpc_choices[computer_rpc_choice] + "\n" + "You win.")
# paper wins
elif (my_rpc_choice == 1 and computer_rpc_choice == 0):
  print(rpc_choices[my_rpc_choice] + "\n" + "Computer chose:" + "\n" + rpc_choices[computer_rpc_choice] + "\n" + "You win.")
# scissors wins
elif (my_rpc_choice == 2 and computer_rpc_choice == 1):
  print(rpc_choices[my_rpc_choice] + "\n" + "Computer chose:" + "\n" + rpc_choices[computer_rpc_choice] + "\n" + "You win.")

# rock draw
elif (my_rpc_choice == 0 and computer_rpc_choice == 0):
  print(rpc_choices[my_rpc_choice] + "\n" + "Computer chose:" + "\n" + rpc_choices[computer_rpc_choice] + "\n" + "Draw.")
# scissors draw
elif (my_rpc_choice == 1 and computer_rpc_choice == 1):
  print(rpc_choices[my_rpc_choice] + "\n" + "Computer chose:" + "\n" + rpc_choices[computer_rpc_choice] + "\n" + "Draw.")
# paper draw
elif (my_rpc_choice == 2 and computer_rpc_choice == 2):
  print(rpc_choices[my_rpc_choice] + "\n" + "Computer chose:" + "\n" + rpc_choices[computer_rpc_choice] + "\n" + "Draw.")

  # rock loses
elif (my_rpc_choice == 0 and computer_rpc_choice == 1):
  print(rpc_choices[my_rpc_choice] + "\n" + "Computer chose:" + "\n" + rpc_choices[computer_rpc_choice] + "\n" + "You lose.")
# scissors loses
elif (my_rpc_choice == 1 and computer_rpc_choice == 2):
  print(rpc_choices[my_rpc_choice] + "\n" + "Computer chose:" + "\n" + rpc_choices[computer_rpc_choice] + "\n" + "You lose.")
# paper loses
elif (my_rpc_choice == 2 and computer_rpc_choice == 0):
  print(rpc_choices[my_rpc_choice] + "\n" + "Computer chose:" + "\n" + rpc_choices[computer_rpc_choice] + "\n" + "You lose.")