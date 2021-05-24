# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
first_name = name1.lower()
second_name = name2.lower()

true_two_name = (first_name + second_name)
true_1 = int(true_two_name.count("t"))
true_2 = int(true_two_name.count("r"))
true_3 = int(true_two_name.count("u"))
true_4 = int(true_two_name.count("e"))

true_name_last = (true_1+true_2+true_3+true_4)

love_two_name = (first_name + second_name)
love_1 = int(love_two_name.count("l"))
love_2 = int(love_two_name.count("o"))
love_3 = int(love_two_name.count("v"))
love_4 = int(love_two_name.count("e"))

love_name_last = (love_1+love_2+love_3+love_4)

join_part1 = str(true_name_last)
join_part2 = str(love_name_last)
join_finish = (join_part1 + join_part2)

join_convert = int(join_finish)

if join_convert <10:
  print(f"Your score is {join_convert}%, you go together like coke and mentos.")
elif join_convert >90:
  print(f"Your score is {join_convert}%, you go together like coke and mentos.")
elif join_convert ==40:
  print(f"Your score is {join_convert}%, you are alright together.")
elif join_convert <=50:
  print(f"Your score is {join_convert}%, you are alright together.")
else:
  print(F"Your score is {join_convert}%.")

