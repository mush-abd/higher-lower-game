from art import logo, vs
from game_data import data
import os
import random

score = 0

def compare(prop_1, prop_2):
  print(logo)
  global score
  if score > 0:
    print(f"You're right! Current score: {score}")
  print(
    f"Compare A: {prop_1['name']}, a {prop_1['description']}, from {prop_1['country']}.")
  print(vs)
  print(
    f"Compare B: {prop_2['name']}, a {prop_2['description']}, from {prop_2['country']}.")
  option = input("Who has more followers? Type 'A' or 'B': ")
  if option == 'A':
    if prop_1['follower_count'] > prop_2['follower_count']:
      score += 1
      os.system('cls')
      make_prop_2(prop_1)
    else:
      os.system('cls')
      print(logo)
      print(f"Wrong Answer, Game Over. Your final score is {score}")
      return
  else:
    if prop_2['follower_count'] > prop_1['follower_count']:
      score += 1
      os.system('cls')
      make_prop_2(prop_2)
    else:
      os.system('cls')
      print(logo)
      print(f"Wrong Answer, Game Over. Your final score is {score}")
      return


def make_prop_2(prop):
  prop_1 = prop
  prop_2 = random.choice(data)
  compare(prop_1, prop_2)


make_prop_2(random.choice(data))

