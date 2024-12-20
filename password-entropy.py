import math

password = input("please enter your password:")
number_of_charac = len(password)
uppercase_letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
lowercase_letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
]

test_case = (list(password))
Has_lowercase = False
Has_Uppercase = False
Has_Digits = False
Has_special_characters = False


for char in password:
    if char in lowercase_letters:
        Has_lowercase = True
    if char in uppercase_letters:
        Has_Uppercase = True
    if char in digits:
        Has_Digits = True
    if char in special_characters:
        Has_special_characters = True

# Initialize N (character set size)
N = 0

if Has_lowercase == True and Has_Digits == False and Has_Uppercase == False and Has_special_characters == False:
    N = 26  # Lowercase only
elif Has_lowercase == True and Has_Digits == False and Has_Uppercase == False and Has_special_characters == True:
    N = 26 + 32  # Lowercase and special characters
elif Has_lowercase == True and Has_Digits == False and Has_Uppercase == True and Has_special_characters == False:
    N = 26 + 26  # Lowercase and uppercase
elif Has_lowercase == True and Has_Digits == False and Has_Uppercase == True and Has_special_characters == True:
    N = 26 + 26 + 32  # Lowercase, uppercase, and special characters
elif Has_lowercase == False and Has_Digits == True and Has_Uppercase == False and Has_special_characters == False:
    N = 10  # Digits only
elif Has_lowercase == False and Has_Digits == True and Has_Uppercase == False and Has_special_characters == True:
    N = 10 + 32  # Digits and special characters
elif Has_lowercase == False and Has_Digits == True and Has_Uppercase == True and Has_special_characters == False:
    N = 10 + 26  # Digits and uppercase
elif Has_lowercase == False and Has_Digits == True and Has_Uppercase == True and Has_special_characters == True:
    N = 10 + 26 + 32  # Digits, uppercase, and special characters
elif Has_lowercase == False and Has_Digits == False and Has_Uppercase == True and Has_special_characters == False:
    N = 26  # Uppercase only
elif Has_lowercase == False and Has_Digits == False and Has_Uppercase == True and Has_special_characters == True:
    N = 26 + 32  # Uppercase and special characters
elif Has_lowercase == False and Has_Digits == False and Has_Uppercase == False and Has_special_characters == True:
    N = 32  # Special characters only
elif Has_lowercase == True and Has_Digits == True and Has_Uppercase == False and Has_special_characters == False:
    N = 26 + 10  # Lowercase and digits
elif Has_lowercase == True and Has_Digits == True and Has_Uppercase == False and Has_special_characters == True:
    N = 26 + 10 + 32  # Lowercase, digits, and special characters
elif Has_lowercase == True and Has_Digits == True and Has_Uppercase == True and Has_special_characters == False:
    N = 26 + 10 + 26  # Lowercase, digits, and uppercase
elif Has_lowercase == True and Has_Digits == True and Has_Uppercase == True and Has_special_characters == True:
    N = 26 + 10 + 26 + 32  # Lowercase, digits, uppercase, and special characters
elif Has_lowercase == False and Has_Digits == False and Has_Uppercase == False and Has_special_characters == False:
    N = 0  # No characters
entropy_rough = number_of_charac * math.log2(N)
entropy = round(entropy_rough)
print(f"The Entropy for your password is : {entropy}")
if entropy >= 120:
    print("password is very strong")
elif 60 <= entropy and entropy < 120:
    print("Password is strong")
elif 36 <= entropy and entropy < 59:
    print("Password is weak")
else: print("password is very weak")
