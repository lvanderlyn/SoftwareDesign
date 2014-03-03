# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 10:39:59 2014

@author: ddiggins, koenigin
"""

import re

f = open('Shakespeare.txt')
fullText = f.read() #Turns the contents of Shakespeare.txt into a readable text file
f.close


def master_isolator(play, title):
    """ Does a whole lot of things!
    Inputs: Shakespeare.txt, and the title of the play Alls Well that Ends Well
    
    This function searches for the beginning and ending of the play and returns those. Then it takes the play that results,
    compiles a list of characters from the play's Dramatis Personae (because those are really the only ones that matter),
    and splits the play up in acts so we can track the sentiment of the characters in each act over time using ShakespeareSpeech.py
    """
    #Finds the whole text of the play
    titlefinder = play.index(title.upper()) #Traverses works to find play title in text
    play = play[titlefinder:]
    end_of_play = play.index("THE END") #Finds end of play
    playtext = play[:end_of_play] #Isolates the full play text
    
    
    chars_and_acts = []    
    
        
    #Isolates the Dramatis Personae of the Play
    if "DRAMATIS PERSONAE" in playtext:
        start_of_personae= playtext.index("DRAMATIS PERSONAE") #Finds beginning of Personae
    elif "Dramatis Personae" in playtext:
        start_of_personae= playtext.index("Dramatis Personae")
    end_of_personae = playtext.index("<<") #Project Gutenberg documents end Personae with long copyright notices
    personae = playtext[start_of_personae:end_of_personae] #Isolates
    
    #Uses isolated Personae to compile a character list
    
    characters = {} #Creates empty dictionary for character names
    play = re.findall("[\w'\.\!\?\-]+", personae)#Translates dramatis personae into list of words
    for word in play:
        if word == word.upper(): #Names appear in capital letters in Personae
            if word not in characters: #Adds character if they are not yet in the dictionary
                if word != 'THE':
                    if word != 'OF':
                        if word != 'A': #Getting rid of common extraneous words here
                            characters[word + "."] = []
    
    chars_and_acts.append(characters)
    
    #Isolates acts and separates them as different values of a list
    
    acts = ['I', 'II', 'III', 'IV', 'V'] #All of the plays compatible with this format have five acts
    for act in range(len(acts)):
        start_of_act = playtext.index("ACT " + acts[act])
        if acts[act] == acts[-1]: #Ends function if act V is reached!
            newact = playtext[start_of_act:]
            chars_and_acts.append(newact)
        else:
            newact = playtext[start_of_act:] #Sets the new act start point
            end_of_act = newact.index("<<THIS ELECTRONIC VERSION") #All acts have copyright notices between them, so this isolates them
            newact = newact[:end_of_act]
            chars_and_acts.append(newact)    
    
    return chars_and_acts #First values of char_and_acts is a list of the character names, and the rest of the values 1-5 correspond to acts I-V


#print master_isolator(fullText, "Coriolanus") #Old Unit Test