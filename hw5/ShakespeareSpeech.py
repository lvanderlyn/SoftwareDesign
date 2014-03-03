# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:58:46 2014

@author: koenigin
"""
import re
import pattern.en
from Playfinder2 import story_isolator, act_isolator 
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
    split = act_isolator(story_isolator(fullText, name))
    if Acts == 'all' or Acts == 'All' or Acts == 'All':
        for act in range(5):
            text = re.findall("[\w'\.\!\?\-]+", split[act+1])
            play += text
    else:
        for act in range(Acts):
            text = re.findall("[\w'\.\!\?\-]+", split[act+1])
            play += text
    return [split [0], play]
    
Selection = selectPlay('Alls Well that Ends Well', 5)     
play = Selection[1]    
cast = Selection[0] 
assignLine(play,cast) 

#part of a function that will be incorporated into act_scene_isolator
# and will return the sentiment of each character in a particular act

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
        x = float(sdict[key][0])
        y = float(sdict[key][1])
        n.append(key)
        X.append(x)
        Y.append(y)
    
    fig, ax = plt.subplots()
    ax.scatter(X,Y)    
    for i, txt in enumerate(n):
        ax.annotate(txt, (X[i], Y[i]))
    plt. xlabel('positivity')
    plt.ylabel('negativity')
    plt.axis([-1,1,0,1])
    plt.show()


sdict = assignSentiment(assignLine(play,cast))
print sdict
plotSentiment(sdict)
    
        

        

   
       
                    