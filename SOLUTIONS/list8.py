#write a script to replace list's item with new value if found.take value from user which you want to replace.
# take input from user
value_to_replace = int(input("Enter value you want to replace: "))
new_value = int(input("Enter value from which you want to replace: "))

# define the list
list1 = [5, 10, 15, 20, 25, 50, 20]

# loop through the list and replace the value if found
for i in range(len(list1)):
    if list1[i] == value_to_replace:
        list1[i] = new_value

# print the updated list
print(list1)


