# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:58:46 2014

@author: koenigin
"""
import re
import pattern.en
from Playfinder import story_isolator

f = open('Shakespeare.txt')
fullText = f.read()
f.close

#def story_isolator(play):
#    end_of_boilerplate = play.index("all in black")
#    end_of_play = play.index("Enter PAGE")
#    playtext = play[end_of_boilerplate:end_of_play]
#    return playtext

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

scene1 = {'KING.' : [], 'DUKE.' : [], 'BERTRAM.' : [], 'LAFEU.' : [], 'HELENA.' : [], 'PAROLLES.' : [], 'FRENCH LORD.' : [], 'STEWARD.' : [], 'LAVACHE.' : [], 'PAGE.' : [], 'COUNTESS.' : [],' WIDOW.' : [], 'DIANA.' : [], 'VIOLENTA.' : [],  'MARIANA.' : []}
play = re.findall("[\w'\.\!\?\-]+", story_isolator(fullText)) 
assignLine(play,scene1) 
#print scene1['HELENA.']
#HelenaL = ""
#for word in scene1['HELENA.']:
#    HelenaL += word + " "
##print HelenaL
#HelenaS = pattern.en.sentiment(HelenaL)
#print HelenaS

for key in scene1:
    if len(scene1[key]) != 0: 
        Lines = ""
        Sentiment = {}
        for word in scene1[key]:
            Lines += word + " "
            Sentiment[key] = pattern.en.sentiment(Lines)
        print Sentiment
   
       
                    