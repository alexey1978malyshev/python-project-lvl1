#!/usr/bin/env python3
import sys  
sys.path.insert(0, '/brain_games.cli/')  
 
from cli import welcome_user

def main():
    """Make a user intreface."""
    print('Welcome to the Brain Games!')
    
if __name__ == '__main__':
    main()
welcome_user()
