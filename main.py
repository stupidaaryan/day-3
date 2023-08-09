# Travel India

import random

statesAndTerritories_of_India = ["Arunachal Pradesh", "Assam", "Andhra Pradesh", "Bihar", "Chhatisgarh", "Manipur", "Sikkim", "Tripura", "Meghalaya", "Nagaland", "Mizoram", "Jharkhand", "Odisha", "Tamil Nadu", "Kerala", "Karnataka", "Goa", "Maharastra", "Gujrat", "Rajasthan", "Punjab", "Himachal Pradesh", "Jammu & Kashmir", "Laddakh", "Delhi", "Uttrakhand", "Uttar Pradesh", "Madhya Pradesh", "West Bengal", "Telangana", "Andman & Nicobar", "LakshDweep", "Daman & Diu", "Dadra & Nagar Haveli", "Pondicherry" ]

Random_Travel = random.randint(0, 36)

ask = input("Do You wanna go to Travel to India ? Type Y for yes and N for no").lower()

if ask == "y":
  print(f"You Should go to Travel to {statesAndTerritories_of_India[Random_Travel]}.")
elif ask == "n":
  print("Fuck you! Go to Travel Ecuador then!")
else:
  print("Don't You have Brain? Y or N")


# HeadOrTails

import random

random_num = random.randint(1, 101)
print(random_num)
if random_num % 2 == 0:
  print("It's Head!")
elif random_num % 2 != 0:
  print("It's Tail")

# who will pay the bill?

import random

names = input("Tell me name so of people? ex- Aaryan, Iron Man, Spiderman \n")

names_list = names.split(",")

lenOfList = len(names_list) - 1

random = random.randint(0, lenOfList)
print(random)
print(f"{names_list[random]} will pay the bill.")
