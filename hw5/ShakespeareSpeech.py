# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:58:46 2014

@author: koenigin
"""
import re
import pattern.en
from Playfinder2 import story_isolator, act_isolator, character_isolator, personae_isolator
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

#Act1 = {'KING.' : [], 'DUKE.' : [], 'BERTRAM.' : [], 'LAFEU.' : [], 'HELENA.' : [], 'PAROLLES.' : [], 'FRENCH LORD.' : [], 'STEWARD.' : [], 'LAVACHE.' : [], 'PAGE.' : [], 'COUNTESS.' : [],' WIDOW.' : [], 'DIANA.' : [], 'VIOLENTA.' : [],  'MARIANA.' : []}
AllsWell = act_isolator(story_isolator(fullText, 'Alls Well that Ends Well'))
play = re.findall("[\w'\.\!\?\-]+", AllsWell[0])
cast = personae_isolator(AllsWell) 
assignLine(play,cast) 

#part of a function that will be incorporated into act_scene_isolator
# and will return the sentiment of each character in a particular act

def assignSentiment(ldict):
    for key in ldict:
        if len(ldict[key]) != 0: #does not add characters not in a scene to dictionary
            Lines = ""
            Sentiment = {}
            for word in ldict[key]: #changes lines into string sentences to be analyzed by pattern
                Lines += word + " "
#                Sentiment[key] = pattern.en.sentiment(Lines) #assigns sentiment
            print Lines
    return Sentiment
    

    
def plotSentiment(sdict):
    for key in sdict:
        x = int(sdict[key][1])
        y = int(sdict[key][2])
        plt.plot(x, y, '.', 'MarkerSize', 2)
    plt. xlabel('positivity')
    plt.ylabel('negativity')
        
        

plotSentiment(assignSentiment(assignLine(play,cast)[0]))
    
        

        

   
       
                    