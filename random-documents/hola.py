#---
'''
TODO @leosanchezsoler
'''
#---
import argparse

#import the json file that contains the data

'''
# TO RUN:
# RUN ON TERMINAL
#python + absolute-path

# 1
# python or python3
# 2
# route to the file
# 3
# arg(s): introduce the argument(s) and its value
# --help: provides information about the arguments

# 'python' 'route' 'args'
'''

class Console():
    def __init__(self, password=None):
        self.password = password
        parser = argparse.ArgumentParser()
        parser.add_argument('-j','--j', type=int, help='the password')
        args = vars(parser.parse_args())

        print('####################\n')
        print(type(args))
        print(args)

        password = args['j']

        if password == 18:
            print ('Hello')
        #here goes the function that downloads the json file

        else:
            print('\nIncorrect password.' +
            '\nPlease, check if you have the correct password.' +
            '\nIf the error persists, please contact @RMolleda, @alfonsogarcia-git or @leosanchezsoler.')

        #print('\nThe final data is' + str(data))
        print('\n####################')

#Define an empty instance to run it
Console()