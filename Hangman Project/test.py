#This is only a temporary test file


word_chosen = 'banana'
lenght = len(word_chosen)
display = '_' * lenght
letter_in =''
lenght_disp = len(display)

print(display)
choose = input('letter => ')

if choose in word_chosen and not letter_in:
    letter_in += choose
    print('You have guessed right ! keep on going ! \n')

    for i in range(lenght):
        #pos = letter_in == word_chosen[i]
        #print(pos)

        if letter_in == word_chosen[i] == True:
            letter_r = letter_in in word_chosen[i]
            display[i] = letter_r

            print(display)

            
    

