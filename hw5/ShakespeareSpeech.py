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

AllsWell = act_isolator(story_isolator(fullText, 'Alls Well that Ends Well'))
play = re.findall("[\w'\.\!\?\-]+", AllsWell[1])
cast = AllsWell[0] 
assignLine(play,cast) 

#part of a function that will be incorporated into act_scene_isolator
# and will return the sentiment of each character in a particular act

def assignSentiment(ldict):
    Sentiment = {}
    for key in ldict:
        if len(ldict[key]) != 0: #does not add characters not in a scene to dictionary
            Lines = ""
            for word in ldict[key]: #changes lines into string sentences to be analyzed by pattern
                Lines += word + " "
            Sentiment[key] = pattern.en.sentiment(Lines) #assigns sentiment 
    return Sentiment
    

    
def plotSentiment(sdict):
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
    
        

        

   
       
                    