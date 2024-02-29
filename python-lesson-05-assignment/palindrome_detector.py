#Palindrome detector - Checks whether a word or phrase entered by user is a palindrome or not
input_word = input("Please enter a word: ")

#Checks if word entered contains only letters and if not, asks user to enter word again
while(input_word.replace(" ","").isalpha() == False):
    print("Not all characters are alphabetic characters. Please only use letters \n")
    input_word = input("Please enter a word: ")

#Checks if word or phrase is a palindrome after exiting while loop    
input_word_lower = input_word.replace(" ", "").lower()

for i in range(len(input_word_lower)):
    if input_word_lower[i] != input_word_lower[len(input_word_lower)-i-1]:
        print("This is not a palindrome")
        break

    else:            
        print("This is a palindrome")
        break