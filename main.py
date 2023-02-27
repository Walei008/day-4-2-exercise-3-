# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆
num_items=len(names)
random_number=random.randint(0,num_items-1)
person_to_pay=names[random_number]
print(f"{person_to_pay} is going to pay")
#Write your code below this line 👇



