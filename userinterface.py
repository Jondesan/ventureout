#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 00:34:26 2020

@author: joonahuh
"""

def userInterface():
    i = 1
    while i > 0:
        print('''####################################
#            VENTUREOUT            #
#                                  #
#      Start ...:|> start          #
#      Exit  ...:|> exit           #
#      Dev   ...:|> devstart       #
#                                  #
####################################''')
        usrCmd = input('Input your command: ')
    
        if usrCmd == 'exit':
            return 0
        elif usrCmd == 'devstart':
            print('Error while loading content. Implementation still unfinished.')
        elif usrCmd == 'start':          
            return mainMenu()
        
        
def mainMenuLoop():
    i = 1
    while i > 0:
        usrCmd = input('...:|> ')
        
        if usrCmd.startswith('god'):
            splitCmd = usrCmd.split()
            if splitCmd[1] == 'exit':
                return 0
            elif splitCmd[1] == 'help':
                print('List of god commands not yet implemented.')


def mainMenu():
    return mainMenuLoop()