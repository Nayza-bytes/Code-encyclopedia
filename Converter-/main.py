
#/////////////////////////////////////////////////////
#
# Type : Terminal based app
# Made by Nayzalix for mastering Python
#
#/////////////////////////////////////////////////////


#----Modules----#
from pycenter import center


#----Ascii Thing----#
title = """

     _____                      __            __    __ 
    / ___/__  ___ _  _____ ____/ /____ ______/ /___/ /_
   / /__/ _ \/ _ \ |/ / -_) __/ __/ -_) __/_  __/_  __/
   \___/\___/_//_/___/\__/_/  \__/\__/_/   /_/   /_/   
<-------------------------------------------------------->
                                                    
"""
opt = """
[1] Convert Fahrenheit to Celsius   | [5] Calculate Resistance
[2] Convert Celsuis to Fahrenheit   | [6] Calculate Current
[3] Euro to Dollar                  | [7] Calculate Voltage
[4] Dollar to euro                  |
"""

print(center(title))
print(opt)


#----Convertion Function----#
def FtoC(Faren):
    Celsius = (Faren - 32) * 5/9
    print(Celsius)

def CtoF(Cels):
    faren = Cels * 9/5 + 32
    print(faren)

def EurToDol(euro):
    dol = euro * 0.86
    print(f"[!] Around {dol} Dollars")

def DolToEur(dollar):
    eur = dollar * 1.16
    print(f"[!] Around {eur} Euros")

def calcResistance(I, E):
    Resistance = E/I
    print(f'Resistance : {Resistance} Ohm')

def calcCurrent(R, E):
    Current = E/R
    print(f'Resistance : {Current} Ohm')

def calcVoltage(I, R):
    Voltage = I*R
    print(f'Resistance : {Voltage} Ohm')
#----Variables----#
count = 0

#----Main code----#
if __name__ == '__main__':
    while True:
        choice = input("Choose a option -> ")
        try:
            match choice:
                case '1':
                    FtoC(int(input('[!]=> Input Fahrenheit : ')))
                case '2':
                    CtoF(int(input('[!]=> Input Celsuis : ')))
                case '3':
                    EurToDol(int(input('[!]=> Input Euro : ')))
                case '4':
                    DolToEur(int(input('[!]=> Input Dollars : ')))
                case '5':
                    calcResistance(int(input('[!]=> Input Voltage : ')), int(input('[!]=> Input Currents : ')))
                case '6':
                    int(input('[!]=> Input Voltage : ')), int(input('[!]=> Input Resistance : '))
                case '7':
                    int(input('[!]=> Input Current : ')), int(input('[!]=> Input Resistance : '))
                case 'quit':
                    break
                case _:
                    print('[!]=> Oops an error as occured, please try again !')
                
        except Exception as e:
            print(f"[!]Warning !! An error was found during the execution of the script -> {e}")

        if count == 2:
            print("Are you dumb !!\n")
        elif count == 3:
            print("Close this terminal bro please, for everyone !\n")
        elif count == 20: 
            print("Ok i close it for you\n")
            break