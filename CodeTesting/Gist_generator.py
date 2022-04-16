import pandas
import GGG_probmatrix as GGG_prob

test_text = "This should be some string containing some words repeated over and over again word for word so that we can analyse how the words follow each other."

#GGG_prob.make_pmatrix(test_text)

def Clean_data(file_name): #Output: likely just STRING
    '''
    This function will take an input, either raw text or a dataframe,
    or maybe even filename, and then clean it and prepare it for analysis.
    
    This procedure will include:
    Removing certain characters, like some punctuations
    Combining many input strings into a single string ready for analysis.
    De-capitalizing letters
    Inserting a \"text-stop\" identifying character after all data strings.
    '''

    #deprecated, until we proceed to read data with SQL
    #df = pandas.read_csv(file_name, header=None)

    #filepath = "T3G_TheGeneralGistGenerator\CodeTesting\\" + file_name
    file = open(file_name, "r")
    combined_text = "".join(file.read()) #combine all text in the file
    
    #Cleaning text
    combined_text = combined_text.lower()
    combined_text = combined_text.replace("\n", " ")

    print(combined_text)
    print("completed")

def generate_gist(text_input):
    #Clean_data()
    pmatrix = GGG_prob.make_pmatrix(text_input)

    print("Finished generating gist")
    #print(pmatrix)

#generate_gist(test_text)

Clean_data("CodeTesting/Text_test.txt")
