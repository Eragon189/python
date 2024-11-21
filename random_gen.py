import random

password_legth = 10
password = []
new_char = ""
i = 0
uper_case_charactors = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
lower_case_charactors = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
special_characters = ["~","`","!","@","#","$","%","^","&","*","(",")","-","_","=","+","{","}","[","]","|","\\","/",":",";","\"","\'","<",">",",",".","?"]
random_number1 = 0
for i in range (password_legth):
    random_number = random.randint(1, 3)  #Generates a random number between 1 and 100
    if random_number == 1:
        random_number1 = random.randint(1, 32)
        new_char = special_characters[random_number1]
    if random_number == 2:
        random_number1 = random.randint(1, 26)
        new_char == lower_case_charactors[random_number1]
    if random_number == 3:
        random_number1 = random.randint(1, 26)
        new_char == uper_case_charactors[random_number1]
    password.push(new_char)
print("Your password is " + password)