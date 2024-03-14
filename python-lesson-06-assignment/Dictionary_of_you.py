#Dictionary of you

#Creates dictionary with key and value information

christie = {
    'My occupation is': 'Agricultural Scientist', 
    'I work at': 'AgricuLture Victoria', 
    'My hobbies are': 'cooking and gardening', 
    'My favourite food is': 'eggplant parmigiana'}

#Update to add favourite animal

christie['My favourite animals are'] = 'guinea pigs'

print("This is a dictionary about Christie")

for key, value in christie.items():
   
    print(f"{key} {value}")
   