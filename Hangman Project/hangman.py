import platform
import random
import os


#Function for the core game 
def core():

    #Setup for the game

    word_list = ['short', 'banana', 'mango', 'car', 'hamburger', 'adventure', 'bank']
    word_chosen = random.choice(word_list)
    guesses = 7
    lenght = len(word_chosen)
    display = '_' * lenght
    letter_in = ""
    letter_pos = 0

    #Communication between the user and the code

    print(f'Welcome {os.name}, plateform : {platform.system()}, version : {platform.release()}')
    print(display)
    print(f'you have {guesses} tries.')

    #core functionnalities

    while guesses < 6:
        user_guesse = input('Choose a letter -> ')

        if user_guesse in word_chosen and not letter_in:
            letter_in += ',' + user_guesse
            print('You have guessed right ! keep on going !')

            for i in range(word_chosen):
                pos = letter_in == word_chosen[i]
                
                return pos 
            


if __name__ == '__main__':
    def main():
        core()


        
