<<<<<<< HEAD
#!/usr/bin/env python3
import sys  
sys.path.insert(0, '/brain_games.cli/')  
 
from cli import welcome_user

def main():
    """Make a user intreface."""
    print('Welcome to the Brain Games!')
=======
#!/usr/bin/env python

from /home/alexey/python-project-lvl1 import cli
def greet(who):
    print('{}'.format(who))

def main():
    greet('Welcome to the Brain Games!')
    print(cli.welcome_user)
>>>>>>> bb231eb4fe889a13e94ab9f6d0f7903bab9d0a72
    
if __name__ == '__main__':
    main()
welcome_user()
