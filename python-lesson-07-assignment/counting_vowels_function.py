# Counting vowels in a string - define function

def vowel_counting(string_input):

    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    count = 0

    for letter in string_input:
        if letter in vowels:
            count = count + 1
        
    return count
    
