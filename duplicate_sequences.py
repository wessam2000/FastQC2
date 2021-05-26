#بسم الله الرحمن الرحيم
#-----------Duplicate Sequences---------
file_path=input("Enter file path")
adapter_file=input("Enter adapter file path")
import matplotlib.pyplot as plt
import numpy as np
'''
    Description: reading file containing adapters and extract adapters sequences.
    Input: fasta file.
    Output: 1 array containing adapters sequences.
'''
def readAdapters(adapter_file):
    adapters_seq= []
    with open(adapter_file) as file_obj:
        while True:
            file_obj.readline()
            seq= file_obj.readline().strip()
            if not seq:
                break
            adapters_seq.append(seq)
    return adapters_seq
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
    Description: detect duplication of sequences and their count, and the whole number of duplicated sequences due to adapter content.
    Input: array of sequences.
    Output: dictionary of duplicated sequences and adapter flag.
'''
def duplication_sequences(sequences):
    duplication_sequences_dect= {}
    adapter_flag= 0
    for sequence in sequences: 
        if sequence not in duplication_sequences_dect:
            duplication_sequences_dect[sequence]= 1
        else:
            duplication_sequences_dect[sequence] += 1
            if sequence in adapters_seq:
                adapter_flag += 1
    return duplication_sequences_dect, adapter_flag
'''
    Description: calculating frequencies of duplicated sequences.
    Input: dictionary of duplicated sequences.
    Output: array of percentage frequencies of duplicated sequences.
'''
def mod_duplication_sequences(duplication_sequences_dect):
    mod_duplication_sequences_arr1= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '>10', '>100', '>1k', '>5k']
    mod_duplication_sequences_arr2= [0]*len(mod_duplication_sequences_arr1)
    total_sequences= len(sequences)
    for value in duplication_sequences_dect.values():
        if value==1:
            mod_duplication_sequences_arr2[0] += 1
        elif value==2:
            mod_duplication_sequences_arr2[1] += 1
        elif value==3:
            mod_duplication_sequences_arr2[2] += 1
        elif value==4:
            mod_duplication_sequences_arr2[3] += 1
        elif value==5:
            mod_duplication_sequences_arr2[4] += 1
        elif value==6:
            mod_duplication_sequences_arr2[5] += 1
        elif value==7:
             mod_duplication_sequences_arr2[6] += 1
        elif value==8:
            mod_duplication_sequences_arr2[7] += 1
        elif value==9:
            mod_duplication_sequences_arr2[8] += 1
        elif value>=10 and value<100:
            mod_duplication_sequences_arr2[9] += 1
        elif value>=100 and value<1000:
            mod_duplication_sequences_arr2[10] += 1
        elif value>=1000 and value<5000:
            mod_duplication_sequences_arr2[11] += 1
        elif value>=5000:
            mod_duplication_sequences_arr2[12] += 1
        new_percentage= [0]*len(mod_duplication_sequences_arr2)
        for i in range(len(mod_duplication_sequences_arr2)):
            new_percentage[i]= round((mod_duplication_sequences_arr2[i] /total_sequences*100), 2)
    return new_percentage
'''
    Description: drawing a graph to show frequencies of duplicated sequences.
    Input: array of duplicated sequences percentage.
    Output: graph of Sequence Duplication Level.
'''
def draw_hist(new_percentage):
    plt.style.use('bmh')
    x= np.arange(13)
    axes= plt.gca()
    axes.set_ylim([0,100])
    x= ["1", '2', '3', '4', '5', '6', '7', '8', '9', '>10', '>100', '>1k', '>5k']
    axes.xticks= (np.arange(13), x)
    plt.xlabel('Sequence Duplication Level')
    plt.ylabel('Frequency')
    plt.title('Including total of {} adapter content'.format(adapter_flag))
    axes.plot(x, new_percentage, label= 'Duplicated sequences')
    plt.legend(loc= 'upper right')
    plt.savefig('box plot7.JPG', transparent=True, dpi=100)
    #plt.show()
if __name__ == '__main__':
    '''Reading sequences'''
    sequences= readFastq_seq(file_path)
    adapters_seq= readAdapters(adapter_file)
    '''Calling duplication_sequences function'''
    duplication_sequences_dect, adapter_flag= duplication_sequences(sequences)
    '''Calling mod_duplication_sequences function'''
    new_percentage= mod_duplication_sequences(duplication_sequences_dect)
    '''Drawing graph'''
    draw_hist(new_percentage)
    ########################################################################
