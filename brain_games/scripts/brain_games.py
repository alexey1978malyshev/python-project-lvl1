#!/usr/bin/env python

from /home/alexey/python-project-lvl1 import cli
def greet(who):
    print('{}'.format(who))

def main():
    greet('Welcome to the Brain Games!')
    print(cli.welcome_user)
    
if __name__ == '__main__':
    main()

