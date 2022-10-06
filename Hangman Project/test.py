#This is only a temporary test file


word_chosen = 'banana'
lenght = len(word_chosen)
display = '_' * lenght
disp_list = list(display)
letter_in =''
lenght_disp = len(display)

print(display)
choose = input('letter => ')

if choose in word_chosen :
    letter_in += choose
    print('You have guessed right ! keep on going ! \n')

    for i in range(lenght):
        pos = letter_in == word_chosen[i]
        #print(pos)

        if pos == True:
            letter_r = letter_in in word_chosen[i]
            disp_list[i] = letter_in


            print(''.join(disp_list))
        else:
            disp_list[i] = '_'

            
    

