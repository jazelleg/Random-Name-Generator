import random

const = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z", "Y"]

vowel = ["A", "E", "I", "O", "U", "Y"]

planet_name = ""
ran_var = 0
ran_const = 0
ran_vowel = 0
  
create = input("Would you like to create a planet?Type 'yes' or 'no': \n")

if create == "yes":
  length = random.randint(2, 11)
  ran_var = random.randint(1, 100)
  for x in range(length):
    if (x + ran_var) % 2 == 0:
      ran_const = random.choice(const)
      planet_name += ran_const
    if (x + ran_var) % 2 == 1:
      ran_vowel = random.choice(vowel)
      planet_name += ran_vowel

else:
  print("Well, then screw off.")

print(planet_name.title())


