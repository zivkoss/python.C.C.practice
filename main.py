import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors: ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices
  
def check_win(player, computer):
    return [player, computer]

a = 3
b = 5
if a == b:
   print("yes")








































































































































# def greeting():
#     return "Hi"
#
# responce = greeting()
# print(responce)