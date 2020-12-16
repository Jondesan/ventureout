#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 00:33:19 2020

@author: joonahuh
"""
import userinterface as UI

e = 1

while e != 0:
    e = UI.userInterface()
    
    if e == 0:
        print('Exit code 0 returned. Execution stopped.')
    