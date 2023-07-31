import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors: ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices
  # return player_choice
  # return computer_choice
choices = get_choices()
print(choices)

food = ["pizza", "carrots", "eggs"]
dinner = random.choice(food)










































































































































# def greeting():
#     return "Hi"
#
# responce = greeting()
# print(responce)