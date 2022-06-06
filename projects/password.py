import random

print('Welcome to our password generator')
char = 'Cocomelon~4'
num_passwords=int(input('How many passwords would you like to generate?'))
len_passwords=int(input('How many characters would you like the passswords to be ?'))

print('\n Here are your passwords:')
for pwd in range (num_passwords):
    password = ' '
    for c in range(len_passwords):
        password += random.choice(char)
    print(password)