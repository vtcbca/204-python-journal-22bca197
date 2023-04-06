#Write a python menu driven script to create 2d array of 5 student marks of 5 subject to perform following operation. 
#1.Print the minimum marks of each subject.
#2.Print the maximum marks of each subject.
#3. Print the average marks of each subject.
#4. Print the marks which are most student get or repeated in subject. 
#5. Find the variance value for each subject marks.
#6.  Print the total of  each student.

import numpy as np

# Create 2D array of student marks
marks = np.zeros((5, 5))

# Get input from user
for i in range(5):
    print("Enter marks for student", i+1)
    for j in range(5):
        marks[i][j] = float(input("Enter marks for subject " + str(j+1) + ": "))

# Menu-driven program
while True:
    print("\nMenu:")
    print("1. Print the minimum marks of each subject")
    print("2. Print the maximum marks of each subject")
    print("3. Print the average marks of each subject")
    print("4. Print the marks which are most student get or repeated in subject")
    print("5. Find the variance value for each subject marks")
    print("6. Print the total of each student")
    print("7. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        # Minimum marks of each subject
        print("Minimum marks of each subject:")
        for j in range(5):
            print("Subject", j+1, ":", min(marks[:,j]))

    elif choice == 2:
        # Maximum marks of each subject
        print("Maximum marks of each subject:")
        for j in range(5):
            print("Subject", j+1, ":", max(marks[:,j]))

    elif choice == 3:
        # Average marks of each subject
        print("Average marks of each subject:")
        for j in range(5):
            print("Subject", j+1, ":", np.mean(marks[:,j]))

    elif choice == 4:
        # Marks which are most repeated in each subject
        print("Marks which are most repeated in each subject:")
        for j in range(5):
            unique_marks, counts = np.unique(marks[:,j], return_counts=True)
            max_count_index = np.argmax(counts)
            print("Subject", j+1, ":", unique_marks[max_count_index])

    elif choice == 5:
        # Variance of each subject marks
        print("Variance of each subject marks:")
        for j in range(5):
            print("Subject", j+1, ":", np.var(marks[:,j]))

    elif choice == 6:
        # Total of each student
        print("Total of each student:")
        for i in range(5):
            print("Student", i+1, ":", sum(marks[i,:]))

    elif choice == 7:
        # Quit program
        break

    else:
        print("Invalid choice! Try again.")




