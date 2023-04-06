#Write a Python program to enter sentence of atleast 10 words. Take user input of lengtho of word. 
#Find the word in user inputed string which has >= length of word enter by user and creaet its directory where word is key and its length is value.

# take user input for string and minimum word length
input_str = input("Enter String: ")
min_length = int(input("Minimum Word length: "))

# split the string into words
words = input_str.split()

# create a dictionary to store the words with length greater than or equal to the minimum length
word_dict = {}
for word in words:
    if len(word) >= min_length:
        word_dict[word] = len(word)

# print the dictionary
print(word_dict)
