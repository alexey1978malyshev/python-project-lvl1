#!/usr/bin/env python

import prompt

def welcome_user():
	name = prompt.string('May I have your name? ')
	print('Hello, {0}!'.format(name))
print(welcome_user())
