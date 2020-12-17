#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 02:13:01 2020

@author: joonahuh
"""



temp = open('resources/menu.dat', 'r')
temp = temp.read()
temp = temp.split('\n')




def init_menus():
    sort_menu_screens()
    

def sort_menu_screens():
    menuData = []
    tempList = []
    
    k = 0
    for i in range(len(temp)):
        if '^ME' in str(temp[i]):
            menuData.append(tempList)
            tempList = []
            k += 1
        else:
            tempList.append(temp[i])
    return menuData

def get_menu():
    return sort_menu_screens()

def print_menu(menuIndex):
    for i in range(len(get_menu()[menuIndex])):
        print(get_menu()[menuIndex][i])



#%%
#   DEV TOOLS

#print_menu(0)