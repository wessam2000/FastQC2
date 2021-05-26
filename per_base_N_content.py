#بسم الله الرحمن الرحيم
#-----------Per base N content--------
file_path=input("enter file path")
import matplotlib.pyplot as plt
import numpy as np
from itertools import zip_longest
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
    Description: transposing sequences to get bases per position and then count N values per position and the whole number of Ns.
    Input: array of sequences.
    Output: array of N percentage per position and the whole number of Ns.
'''
def per_position_N_content(sequences):
    per_position_seq= [list(filter(None, i)) for i in zip_longest(*sequences)]
    total_sequence= len(sequences)
    count_N= []
    whole_N= 0
    for position in per_position_seq:
        count_N_per_position= position.count('N')
        count_N.append(count_N_per_position)
        whole_N += count_N_per_position
    new_percentage= [0]*len(count_N)
    for i in range(len(count_N)):
        new_percentage[i]= round((count_N[i]/total_sequence)*100, 2)
    return new_percentage, whole_N
'''
    Description: drawing a graph to show frequencies of N per position.
    Input: array of N percentage per position.
    Output: graph of N content across all bases.
'''
def draw_hist(new_percentage):
    plt.style.use('bmh')
    x= np.arange(max_len)
    axes= plt.gca()
    axes.set_ylim([0,100])
    plt.xlabel('Position in read (bp)')
    plt.ylabel('Frequency')
    plt.title('N content across all bases')
    plt.plot(x, new_percentage, label='N%')
    plt.legend(loc= 'upper right')
    plt.savefig('box plot5.JPG', transparent=True, dpi=100)
    #plt.show()
if __name__ == '__main__':
    '''Reading sequences'''
    sequences= readFastq_seq(file_path)
    max_len= max(len(read) for read in sequences)
    '''Calling per_position_N_content function'''
    new_percentage, whole_N= per_position_N_content(sequences)
    '''Drawing graph'''
    draw_hist(new_percentage)
    ############################################################################3
