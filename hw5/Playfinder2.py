# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 10:39:59 2014

@author: ddiggins, koenigin
"""

import re

f = open('Shakespeare.txt')
fullText = f.read()
f.close

def story_isolator(play, title):
    """Passes in the complete works of Shakespeare, and returns only the text of
    Alls Well that Ends Well
    
    Play input play must be in the format of the plaintex Project Gutenberg document
    
    Title input must be string and an actual play that Shakespeare wrote
    """
    titlefinder = play.index(title.upper()) #Traverses works to find play title in text
    play = play[titlefinder:]
    end_of_play = play.index("THE END") #Finds end of play
    playtext = play[:end_of_play] #Isolates the full play text
    return playtext

story = story_isolator(fullText, "Alls Well That Ends Well")

#def personae_isolator(play):
#    """Finds and returns the Dramatis Personae of a Shakespearian play
#    
#    Input must be a play that has been cut out from the main text through story_isolator
#    """
#    start_of_personae= play.index("Dramatis Personae") #Finds beginning of Personae
#    end_of_personae = play.index("<<") #Project Gutenberg documents end Personae with long copyright notices
#    personae = play[start_of_personae:end_of_personae] #Isolates the personae
#    return personae
#
#
#personae = personae_isolator(story)
#
#
#def character_isolator(dramatispersonae):
#    characters = {} #Creates empty dictionary for character names
#    play = re.findall("[\w'\.\!\?\-]+", dramatispersonae)#Translates dramatis personae into list of words
#    for word in play:
#        if word == word.upper(): #Names appear in capital letters in Personae
#            if word not in characters: #Adds character if they are not yet in the dictionary
#                if word != 'THE':
#                    if word != 'OF':
#                        if word != 'A': #Getting rid of common extraneous words here
#                            characters[word] = []
#    
#    return characters
#
#
##print character_isolator(personae)

def act_isolator(playtext):
    """ Isolates Acts and Dramatis Personae
    """
    chars_and_acts = []    
    
    #Isolates the Dramatis Personae of the Play
    start_of_personae= playtext.index("Dramatis Personae") #Finds beginning of Personae
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
                            characters[word] = []
    
    chars_and_acts.append(characters)
    
    
    acts = ['I', 'II', 'III', 'IV', 'V']
    for act in range(len(acts)):
        start_of_act = playtext.index("ACT " + acts[act])
        if acts[act] == acts[-1]:
            newact = playtext[start_of_act:]
            chars_and_acts.append(newact)
        else:
            newact = playtext[start_of_act:]
            end_of_act = newact.index("<<THIS ELECTRONIC VERSION")
            newact = newact[:end_of_act]
            chars_and_acts.append(newact)    
    
    print chars_and_acts[0]
    print chars_and_acts[2]
    return chars_and_acts


print act_isolator(story)