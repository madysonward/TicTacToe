#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:52:19 2019

@author: madyward

Topic: TicTacToePy
"""

import random

def game(slot):
    print(' | |')
    print(' ' + slot[7] + ' | ' + slot[8] + ' | ' + slot[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + slot[4] + ' | ' + slot[5] + ' | ' + slot[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + slot[1] + ' | ' + slot[2] + ' | ' + slot[3])
    print('   |   |')

def humanChoice():
    choice = ''
    while not (choice == 'X' or choice == 'O'):
        print('Do you want to be X or O?')
        choice = input().upper()
        
    if choice == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
    
# Randomly decides who goes first
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'machine'
    else:
        return 'human'

# Prevent a never ending game....
def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(slot, choice, move):
    slot[move] = choice

# Slots 1-9, starting bottom left
def isWinner(sl, ch):
    return ((sl[7] == ch and sl[8] == ch and sl[9] == ch) or
    (sl[4] == ch and sl[5] == ch and sl[6] == ch) or
    (sl[1] == ch and sl[2] == ch and sl[3] == ch) or
    (sl[7] == ch and sl[4] == ch and sl[1] == ch) or
    (sl[8] == ch and sl[5] == ch and sl[2] == ch) or
    (sl[9] == ch and sl[6] == ch and sl[3] == ch) or
    (sl[7] == ch and sl[5] == ch and sl[3] == ch) or
    (sl[9] == ch and sl[5] == ch and sl[1] == ch))

def getSlotsCopy(slot):
    dupeSlot = []
    
    for i in slot:
        dupeSlot.append(i)
    return dupeSlot

def isSlotOpen(slot, move):
    return slot[move] == ' '

def getHumanMove(slot):
    move = ' '
    
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSlotOpen(slot, int(move)):
        print("What's your next move? (1-9)")
        move = input()
        
    return int(move)

def getRandomMove(slot, movesList):
    moveOptions = []
    
    for i in movesList:
        if isSlotOpen(slot, i):
            moveOptions.append(i)
    
    if len(moveOptions) != 0:
        return random.choice(moveOptions)
    else:
        return None

def getMachineMove(slot, machineChoice):
    if machineChoice == 'X':
        humanChoice = 'O'
    else:
        humanChoice = 'X'
        
    for i in range(1, 10):
        copy = getSlotsCopy(slot)
        
        if isSlotOpen(copy, i):
            makeMove(copy, machineChoice, i)
            
            if isWinner(copy, machineChoice):
                return i
                
    for i in range(1, 10):
        copy = getSlotsCopy(slot)
        
        if isSlotOpen(copy, i):
            makeMove(copy, humanChoice, i)
            
            if isWinner(copy, humanChoice):
                return i
            
    move = getRandomMove(slot, [1, 3, 7, 9])
    if move != None:
        return move
    
    if isSlotOpen(slot, 5):
        return 5
            
    return getRandomMove(slot, [2, 4, 6, 8])
                        
def areSlotsFull(slot):
    for i in range(1, 10):
        if isSlotOpen(slot, i):
            return False
        return True

print("Let's play Tic Tac Toe!")
    
while True:
    theSlot = [' '] * 10
    humanChoice, machineChoice = humanChoice()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'human':
            game(theSlot)
            move = getHumanMove(theSlot)
            makeMove(theSlot, humanChoice, move)
            if isWinner(theSlot, humanChoice):
                game(theSlot)
                print('You won!')
                gameIsPlaying = False
            else:
                if areSlotsFull(theSlot):
                    game(theSlot)
                    print('The game tied.')
                    break
                else:
                    turn = 'machine'
        else:
            move = getMachineMove(theSlot, machineChoice)
            makeMove(theSlot, machineChoice, move)
            if isWinner(theSlot, machineChoice):
                game(theSlot)
                print('The machine won! You lose.')
                gameIsPlaying = False
            else:
                if areSlotsFull(theSlot):
                    game(theSlot)
                    print('The game tied.')
                    break
                else:
                    turn = 'human'
                    if not playAgain():
                        break
                    