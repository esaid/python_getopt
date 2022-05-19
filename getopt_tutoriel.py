# -*- coding: utf-8 -*-
import sys
import getopt
# utilisation de getopt pour pouvoir passer en ligne de commande des parametres et les gerer
# Template Help

help ='\n*****************************************************************************' + \
'\n* le parametre -v ( version )    ou --Version                               *' + \
'\n* python getopt_tutoriel.py -v                                              *' + \
'\n* le parametre -h ( help )    ou --Help                                     *' + \
'\n* python getopt_tutoriel.py -h                                              *' + \
'\n* le parametre -d ( distribution ) True                                     *' + \
'\n* le parametre -f ( file ) nomdefichier                                     *'+ \
'\n* exemple:  python getopt_tutoriel.py -d True -f monfichier                 *' + \
'\n*****************************************************************************\n\n'


# liste des arguments
argumentList = sys.argv[1:]
# print(argumentList)
# Options
#   h  v  pas de parametres attendu
# d: 1 parametre
# f: 1 parametre
options = "hvd:f:"
# Long options
long_options = ["Help",  "Version", "Distribution=" ,"FileName="]

# parametre par defaut
version = 1.9
distribution = True
OutFile = True
accel = ''
filename = ''

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
except getopt.error as err:
    # output error, and return with an error code
    print(str(err))

    # checking each argument
for currentArgument, currentValue in arguments:
    if currentArgument in ("-h", "--Help"):
        print("\nDisplaying Help\n", help)
        sys.exit()
    elif currentArgument in ("-v", "--Version"):
        print("Version: " , version)
        sys.exit()
    elif currentArgument in ("-d", "--Distribution"):
        distribution = eval(currentValue)
    elif currentArgument in ("-f", "--File"):
        filename = currentValue

print("Distribution: ", distribution)
print("File :  ", filename )
print('nombre de parametres :  ', len(sys.argv)-1)
# argument ok ?
if len(sys.argv)-1 != 4:
    # print(len(sys.argv) , '  ' ,sys.argv)
    print('pas le bon nombre de parametres en ligne de commande ')
    sys.exit()
