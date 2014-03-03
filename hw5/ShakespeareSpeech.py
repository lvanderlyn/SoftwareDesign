# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:58:46 2014

@author: koenigin
"""
import re
import pattern.en
from Playfinder2 import master_isolator
import numpy
import matplotlib.pyplot as plt

f = open('Shakespeare.txt')
fullText = f.read()
f.close


def assignLine(play, d):
    """Takes in a play as a list of words and a dictionary of charactars in 
    the play and assigns the lines to each character in the play"""
    index = 0
    while index < (len(play) -1):
        if play[index] in d:                    #finds first character
            speech = []
            character = play[index]            
            for place in range(index+1, len(play)):       #adds from one character's name until next (exlculsive)
                if play[place] not in d and play[place] != 'Exuent':
                    speech.append(play[place])
                    if place == len(play)-1:            #If no next character, closes  and adds to speech
                        d[character] += speech
                        index = place 
                        break
                else:                               #closes speech and adds lines to dictionary
                    d[character] += speech
                    index = place
                    break
        else:
            index += 1      #increases index to check next one for start codon   
    return d


def selectPlay(name, Acts):
    '''Takes in the name of a play and an integer of the number of Acts 
    inluded or the string "all" and returns a list containing all the words 
    in those sections'''
    play = [] 
    split = master_isolator(fullText, name)
    if Acts == 'all' or Acts == 'All' or Acts == 'All':
        for act in range(5):
            text = re.findall("[\w'\.\!\?\-]+", split[act+1])
            play += text
    else:
        for act in range(Acts):
            text = re.findall("[\w'\.\!\?\-]+", split[act+1])
            play += text
    return [split [0], play]
    

def assignSentiment(ldict):
    '''takes in a dictionary with characters as keys and their lines as values
    and returns a dictionary with the sentiment as values'''
    Sentiment = {}
    for key in ldict:
        if len(ldict[key]) != 0: #does not add characters not in a scene to dictionary
            Lines = ""
            for word in ldict[key]: #changes lines into string sentences to be analyzed by pattern
                Lines += word + " "
            Sentiment[key] = pattern.en.sentiment(Lines) #assigns sentiment 
    return Sentiment
    

    
def plotSentiment(sdict):
    '''takes in a dictionary of character names and sentiment and plots
    objectivity against positiviy'''
    X = []
    Y = []
    n = []
    for key in sdict:
        x = float(sdict[key][0])              #creats list so can be plotted
        y = float(sdict[key][1])
        n.append(key)
        X.append(x)
        Y.append(y)
    
    fig, ax = plt.subplots()
    ax.scatter(X,Y)    
    for i, txt in enumerate(n):              #adds labels b/c they're classy
        ax.annotate(txt, (X[i], Y[i]))
    plt. xlabel('positivity')
    plt.ylabel('objectivity')
    plt.axis([-0.5,1,0,1])
    plt.show()
    
    
   
    
def characterGrowth(playName, character):
    '''takes in a play and a character in the play (written in caps) and 
    plots the change in the characters positivity throughout the play'''
    p = []  
    acts = []
    character = character.upper()
    character +="."
    for index in range(5):
        play = selectPlay(playName, index)[1]
        cast = selectPlay(playName, index)[0]
        lines = assignLine(play, cast)[character]
        if len(lines) > 0:
            Lines = ''
            for word in lines: #changes lines into string sentences to be analyzed by pattern
                Lines += word + " "
            happy = float(pattern.en.sentiment(Lines)[0]) #assigns sentiment 
            p.append(happy)
            acts.append(index+1)

    fig, ax = plt.subplots()
    ax.scatter(acts, p)
    plt.title(character + 'Growth')
    plt.xlabel('Act')
    plt.ylabel('Positivity')
    plt.axis([1,5, -1, 1])
    plt.show()
    
#characterGrowth('Twelfth Night', 'VIOLA.')

 
    
def allPlays(playList, acts):
    '''Takes in list of plays and plots a graph of sentiment of characters
    over entire play'''
    play = []
    cast = {}
    for index in range(len(playList)): #joins multiple plays into single list/dictionary
        play += (selectPlay(playList[index], acts)[1])
        cast.update(selectPlay(playList[index], acts)[0])
    plotSentiment(assignSentiment(assignLine(play, cast)))
    
    
#playList = ['Alls Well that Ends Well', "Midsummer Night's Dream", "The Tempest", "Twelfth Night", "Othello"]
#allPlays(playList, 1)

def soul():
    '''wrapper function that allows user to input whether they want to view
    characters in a single play, characters from multiple plays, or a single
    character over the course of a play'''
    choice = raw_input('Please select a function (by typing 1, 2, or 3): \r1. Plot sentiment of all characters in a play \r2. Plot sentiment of characters over multiple plays \r3. Plot character growth over one play : ')
    if int(choice) == 1:
        playSelect = raw_input("choose a play : ")
        actSelect = int(raw_input('choose number of acts to analyze : '))
        play = selectPlay(playSelect, actSelect)[1]
        cast = selectPlay(playSelect, actSelect)[0]
        plotSentiment(assignSentiment(assignLine(play, cast)))
    elif int(choice) == 2: 
        playSelect = []
        numPlays = raw_input('choose number of plays to analyze : ')
        for it in range(int(numPlays)):
            playChoice = raw_input("choose play" + " " + str(it+1) + " : ")
            playSelect.append(playChoice)
        actSelect = int(raw_input('choose the number of acts to analyze : '))
        allPlays(playSelect, actSelect)
    elif int(choice) == 3:
        playSelect = raw_input("choose a play : ")
        characterSelect = raw_input('choose a character : ')
        characterGrowth(playSelect, characterSelect)
    else:
        print 'Incorrect selection, plase enter: 1, 2, or 3'
        
soul()
    
    
            

        

   
       
                    