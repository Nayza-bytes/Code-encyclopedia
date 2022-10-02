import platform
import random
import os



word_list = ['short', 'banana', 'mango', 'car', 'hamburger', 'adventure', 'bank']
word_chosen = random.choice(word_list)
essai = 9
word_found = False
letters = []
nb_letters = 0

print(f'Welcome {os.name}, plateform : {platform.system()}, version : {platform.release()}')
print(f'The word have {len(word_chosen)} letters, try to guess it, you have {essai} tries.')

while word_found == False or essai == 0:
    letter = input('choose a letter: ')

    if letter in word_chosen:
        letters.append(letter)
        nb_letters += 1
        print('One found')
    elif letter == ' ' or letter == '':
        print("Come on man, choose one letter space isn't one")
    else:
        essai -= 1
        print(f'{essai} remaining')

    if nb_letters == len(word_chosen) and True in [i in word_chosen for i in letters]:
        word_found == True
        
