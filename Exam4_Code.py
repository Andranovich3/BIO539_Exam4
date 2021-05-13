#!/usr/bin/env python3

import argparse
import pandas as pd

def get_kmers(input_string, k_length):
    ''' Calculate the possible kmers from an inputted string and return results. 
    
    Parameters:
    input_string -- the sequence that the user wants to analyze for kmers 
    k_length -- the length of the kmers that will be created
    
    return: a series of print lines and a Pandas DF Table showing results
    '''
    kmer_list = []  # Creates an empty list to store kmers (substrings) is

    if k_length == 1:  # Checks to see if k_length will be "1" (Single-letter substrings)
        poss_kmers = 4  # If true, possible kmers will be 4^k, or 4
    else:  # If false, possible kmers will be the length of the string minus k plus 1
        poss_kmers = len(input_string) - k_length + 1

    num_kmers = len(input_string) - k_length + 1  # Always want to create sliding windows based on k_length
    for i in range(num_kmers):  # Begin sliding window process to create substrings from inputted string
        kmer = input_string[i:i + k_length]  # Slice the string to get the kmer (substring)
        if kmer not in kmer_list:  # Checks to see if the list includes the kmer already
            kmer_list.append(kmer)  # If not, adds (appends) the kmer to the list

    complexity = float(len(kmer_list)) / float(poss_kmers) # Caluclates the complexity as a float (includes decimals)
    
    return kmer_list, poss_kmers, complexity
    
    # This block creates a Pandas DF with these column headers. It then populates the DF with the appropriate data.
    # This code was tested in Jupyter Notebook and produces the correct table/dataframe.
    kmer_table_df = pd.DataFrame(columns = ['k_length','Observed Kmers (List)','Observed Kmers (Count)','Possible Kmers (Count)', 'Linguistic Complexity'])
    kmer_table_df.loc[0] = [k_length, kmer_list, len(kmer_list), poss_kmers, complexity]
    return kmer_table_df
    
def main(args):
    ''' Runs the get_kmer() function. 
    
    Parameters:
    args -- user inputted arguments to satisfy get_kmer()
    
    return: a series of print lines and a Pandas DF Table showing results
    '''
    kmer_list = get_kmers(args.input_string, args.k_length)[0]
    poss_kmers = get_kmers(args.input_string, args.k_length)[1]
    complexity = get_kmers(args.input_string, args.k_length)[2]
    
    print('The size of k (as inputted) is: ' + str(args.k_length))  # Returns the inputted k_length value
    print('The list of observed kmers is: ' + str(kmer_list))  # Return the final list as a string
    print('The number of observed kmers is: ' + str(len(kmer_list)))  # Return the number of observed kmers in the inputted string as a string
    print('The number of possible kmers is: ' + str(poss_kmers))  # Return the number of possible kmers as a string
    print('The linguistic complexity of your string is: ' + str(complexity)) # Return the calculated linguistic complexity
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_string', type = str)
    parser.add_argument('k_length', type = int)
    args = parser.parse_args()
    main(args)
