#Write a script to create dictionary from list which contain student id , name and percentage
#Take student id and name till user choise.

# initialize an empty dictionary
student_dict = {}

# loop until the user chooses to stop entering details
while True:
    # get student details from user
    student_id = input("Enter student id: ")
    student_name = input("Enter student name: ")
    student_percentage = float(input("Enter student percentage: "))

    # add student details to dictionary
    student_dict[int(student_id)] = [student_name, student_percentage]

    # ask user if they want to enter more details
    choice = input("Do you want to enter detail for more student? (yes=Y/y,No=N/n): ")
    if choice.lower() == 'n':
        break

# print the list and dictionary
student_list = []
for key, value in student_dict.items():
    student_list.extend([key, value[0], value[1]])

print("List:", student_list)
print("Dictionary:", student_dict)


