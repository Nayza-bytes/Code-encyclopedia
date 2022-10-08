#Created by Nayza-bytes

import os, getopt
import sys
from typing import List, Dict
from cryptography.fernet import Fernet
from requests import options


#For printing colored text

class bc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'





print('')

files = []
inputfile = ''
inputdir = ''


def read_args() -> Dict[str, str]:
    """Check for valid CLI arguments and return them in a dictionary"""
    if len(sys.argv) != 3:
        print(('Usage python "Encrypt Software.py" <-h|-i|-d|-r> ["file path" -0 if no files]'))
        exit()
    
    args_dict = {
        "mode": sys.argv[1],
        "file_path": sys.argv[2]
    }

    return args_dict

def help_message(mode: str) -> None:
    """Print the help menu for this project"""
    print('''
                Usage: python uthough.py <-h|-i|-d|-r> [file| if -i]


                -h  -help               Print this help pannel
                -i   -input             Choose an input file to encrypt
                -d   -decrypt           Option for decrypting file that have been crypted by this script    
                -r                      Need password for this one my guy XD
            ''')



def main() -> None:

    args: Dict[str, str] = read_args()
    

    if args_dict[mode] == '-h':
        print('Working fine')

     

    # key = Fernet.generate_key()
    # with open('keys.key', 'wb') as keys:
    #     keys.write(key)


    # try:
    #     opts, args = getopt.getopt(sys.argv, 'hidr')
    # except getopt.GetoptError:
    #     print ('test.py --h for help')
    #     sys.exit(2)
 
    #         with open(os.path.basename(inputdir), 'rb') as thefiles:
    #             contents = thefiles.read()


    #         contents_encrypted = Fernet(key).encrypt(contents)
    #         with open(os.path.basename(inputdir), 'wb') as thefiles:
    #             thefiles.write(contents_encrypted)
                

    # for file in os.listdir():
    #     if file == 'uthough.py' or file == 'keys.key':
    #         continue
    #     if os.path.isfile(file):
    #         files.append(file)

    # # print(files)
   


    # 
    #with open('keys.key', 'rb') as key:
    #   secretkey = key.read()
    #   
    #for file in files:
    #     with open(file, 'rb') as thefiles:
    #         contents = thefiles.read()

    #     contents_decrypted = Fernet(secretkey).decrypt(contents)
    #     with open(file, 'wb') as thefiles:
    #         thefiles.write(contents_encrypted)
    #
    #
    #
    #'''
                


if __name__ == '__main__':
    main()