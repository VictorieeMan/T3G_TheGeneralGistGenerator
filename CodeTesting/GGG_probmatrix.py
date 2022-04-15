# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 17:26:18 2022

@author: jorst
"""

import pandas


def make_pmatrix(raw_text): #Ca 40 rows of code
    "CREATE DATAFRAME TEMPLATE"
    a_dict = {}
    split_text = raw_text.split(" ")
    unique_words = list(dict.fromkeys(split_text))
    
    for i in unique_words:
        a_dict[i] = list(0 for i in range(len(unique_words)))
    dframe = pandas.DataFrame(a_dict, index=unique_words)
    
    output_aid("Dataframe Template", dframe)
    

    ### HEEEEEJ!!!!

    ###NU CRASHAR DIN DATOR!
    
    "COUNT OCCURENCES OF WORDS FOLLOWING OTHER WORDS"
    last_word = split_text[0]
    
    split_text_wout_first = split_text
    split_text_wout_first.pop(0) # Let's us start counting at second word.
    
    for new_word in split_text_wout_first:
        # [column][row]
        dframe[new_word][last_word] += 1
        last_word = new_word
    
    output_aid("Dataframe of COUNTS", dframe)    
    
    
    "TURN WORD COUNTS TO PROBABILITY ESTIMATES"
    row_sums = []
    for i in unique_words: #Calculate row sums
        row_sums.append(sum(dframe.loc[i]))
    row_sums = pandas.Series(row_sums, index=unique_words) #Assign row index

    output_aid("Row sums", row_sums)
    
    for word_index in unique_words:
        #call and modify rows
        #dframe.loc[word_index] = round(dframe.loc[word_index]/row_sums[word_index],2)
        
        if(row_sums[word_index] != 0):
            dframe.loc[word_index] = round(dframe.loc[word_index]/row_sums[word_index],2)
        else:
            #In the unlikely event that word_index occurs only one time,
            #and that this happens to be at the very end of the text.
            #This would otherwise cause this line to be NaN because the row sum
            #becomes zero.
            dframe.loc[word_index] = 0
    
    output_aid("FINAL PROBABILITY MATRIX", dframe)
    return(dframe)



def output_aid(description, thing):
    print("\n")
    print("--v--", description, "--v--")
    print(thing)
    print("--^--", description, "--^--")

    

make_pmatrix("Får får får? Nej får får lamm")

