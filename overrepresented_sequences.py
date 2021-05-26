#بسم الله الرحمن الرحمن الرحيم
#--------overrepresented Sequences--------
file_path=input("Enter file path")
adapter_file=input("Enter adapter file")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''
    Description: reading fastq file and extract reads sequences.
    Input: fastq file.
    Output: 1 array to store reads(sequences).
'''
def readFastq_seq(filename):
    sequences= []
    with open(filename) as file_obj:
        while True:
            file_obj.readline() # skip first line in read _starting with '@'_ 
            seq= file_obj.readline().strip() # sequence line
            file_obj.readline() # skip third line in read _starting with '+'_ 
            file_obj.readline() # skip forth line in read _quality score line_
            if not seq:
                break
            sequences.append(seq)
    total_sequences= len(sequences)
    if total_sequences>1500:
        sequences= sequences[:1500]
    return sequences
'''
    Description: reading file containing adapters and extract adapters sequences.
    Input: fasta file.
    Output: 1 array containing adapters sequences.
'''
def readAdapters(filename):
    adapters_seq= []
    with open(filename) as file_obj:
        while True:
            file_obj.readline()
            seq= file_obj.readline().strip()
            if not seq:
                break
            adapters_seq.append(seq)
    return adapters_seq
'''
    Description: detect duplication of sequences and their count, and try to predict source of duplication.
    Input: array of sequences.
    Output: dictionary of duplicated sequences (as keys), their count and source of duplication (as values).
'''
def duplication_sequences(sequences):
    duplication_sequences_dect= {}
    for sequence in sequences: 
        if sequence not in duplication_sequences_dect:
            duplication_sequences_dect[sequence] = [1]
            if sequence in adapters_seq:
                duplication_sequences_dect[sequence].append('Adapter Sequence')  
            else:
                duplication_sequences_dect[sequence].append('No Hit')     
        else:  
            duplication_sequences_dect[sequence][0] += 1
    return duplication_sequences_dect
'''
    Description: detect overrepresented sequences according to threshold (user input).
    Input: dictionary of duplicated sequences (as keys), their count and source of duplication (as values), threshold.
    Output: array of arrays, each sub-array contains the overrepresented, number of occurences, percentage of this number, predicted source of duplication.
'''
def overrepresented_seq(duplication_sequences_dect, threshold):
    new_data_list= []
    for sequence in duplication_sequences_dect:
        new_list= duplication_sequences_dect[sequence]
        if new_list[0] > threshold:
            data_percentage= round((new_list[0]/total_sequences)*100, 2)
            new_data_list.append([sequence, new_list[0], data_percentage, new_list[1]])
    return new_data_list
'''
    Description: creating dataFrame containing 4 columns, for overrepresented sequences, number of occurences, percentage of this number, predicted source of duplication.
    Input: array of arrays, each sub-array contains the overrepresented, number of occurences, percentage of this number, predicted source of duplication.
    Output: dataFrame.
'''
def creating_dataFrame(new_data_list):
    if len(new_data_list)!=0:
        data= pd.DataFrame(new_data_list, columns= ['Sequence', 'Count', 'Percentage', 'Possible Source'])
        data= data.sort_values(by=['Count'], ascending=False)  
        #print(data)
       # ff=data.astype(str)
        #file = open('filename', 'w')
        #file.write(ff)
        #file.close()
        with open('filename', 'a') as f:
               f.write(data.to_string(header = False, index = False)
    )
    else:
        print('There is no overrepresnted sequences according to your threshold.')
        file = open('filename', 'w')
        file.write('There is no overrepresnted sequences according to your threshold.')
        file.close()
if __name__ == '__main__':
    '''Reading sequences'''
    sequences= readFastq_seq(file_path)
    total_sequences= len(sequences)
    '''Reading adapters'''
    adapters_seq= readAdapters(adapter_file)
    '''Calling duplication_sequences function'''
    duplication_sequences_dect= duplication_sequences(sequences)
    '''Calling overrepresented_seq function'''
    new_data_list= overrepresented_seq(duplication_sequences_dect, 2)
    '''Calling creating_dataFrame function'''
    creating_dataFrame(new_data_list)
