#Palindrome word checker - Checks whether a word entered by the user is a palindrome or not

input_word = input("Please enter a word: ")

#Creates a string from input word and reverses it
input_word_lower = input_word.lower()

input_word_no_spaces = input_word_lower.replace(" ", "")

letters_in_word = list(input_word_no_spaces)

letters_in_word.reverse()

input_word_reversed = ''.join(letters_in_word)


#If original word is equal to the word in reverse, then prints "This is a palindrome", else prints "This is not a palindrome"

if(input_word_no_spaces) == (input_word_reversed):
    print("This is a palindrome")
else:
    print("This is not a palindrome")

