# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
first_name_l1 = name1.lower().count("t") 
first_name_l2 = name1.lower().count("r")
first_name_l3 = name1.lower().count("u")
first_name_l4 = name1.lower().count("e")

sum_first_name = first_name_l1 + first_name_l2 + first_name_l3 + first_name_l4

second_name_l1 = name2.lower().count("l")
second_name_l2 = name2.lower().count("o")
second_name_l3 = name2.lower().count("v")
second_name_l4 = name2.lower().count("e")

sum_second_name = second_name_l1 + second_name_l2 + second_name_l3 + second_name_l4

join_part1 = str(sum_first_name)
join_part2 = str(sum_second_name)
join_finish = (join_part1 + join_part2)

join_convert = int(join_finish)

print(join_finish)