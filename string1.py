
#Script To Check String Is Palindrome Or Not

def is_palindrome(word):
    return word == word[::-1]

# Get input from the user
word = input("Enter a word: ")

# Check if the word is a palindrome using the is_palindrome() function
if is_palindrome(word):
    print(f"{word} is a palindrome word.")
else:
    print(f"{word} is not a palindrome word.")
