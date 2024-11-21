import random

# Password settings
password_length = int(input("How long of a Password do you whant:\n"))
password = []
new_char = ""
i = 0
upper_case_characters = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
lower_case_characters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
special_characters = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "{", "}", "[", "]", "|", "\\", "/", ":", ";", "\"", "\'", "<", ">", ",", ".", "?"]

# Generate password
for i in range(password_length):
    random_number = random.randint(1, 3)  # Randomly select category
    if random_number == 1:
        random_number1 = random.randint(0, len(special_characters) - 1)
        new_char = special_characters[random_number1]
    elif random_number == 2:
        random_number1 = random.randint(0, len(lower_case_characters) - 1)
        new_char = lower_case_characters[random_number1]
    elif random_number == 3:
        random_number1 = random.randint(0, len(upper_case_characters) - 1)
        new_char = upper_case_characters[random_number1]
    password.append(new_char)  # Corrected .push() to .append()

# Join password and display
password_string = "".join(password)
print(password_string)
