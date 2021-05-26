#بسم الله الرحمن الرحيم
#------------Per Base Quality scores------------------
file_path=input("Enter file path")
from itertools import zip_longest
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import seaborn as sns
'''
    Description: reading fastq file and extract reads sequences and corresponding bases qualities.
    Input: fastq file.
    Output: 2 arrays, one to store reads(sequences), the second to store the quality of bases in ascii(bases_qualities).
'''
def readFastq_seq_and_qual(file_path):
    sequences= []
    bases_qualities= []
    with open(file_path) as file_obj:
        while True:
            file_obj.readline()
            seq= file_obj.readline().strip()
            file_obj.readline()
            qual= file_obj.readline().strip()
            if not seq:
                break
            if len(seq)<=200:#????????????????????????????????????????????????????????????
                sequences.append(seq)
                bases_qualities.append(qual)
    total_sequences= len(sequences)
    if total_sequences>1500:
        sequences= sequences[:1500]
        bases_qualities= bases_qualities[:1500]
    return sequences, bases_qualities
'''
    Description: converting qualities encoded in ascii to the equivalent numeric values.
    Input: array of bases qualities in ascii format.
    Output: array of bases qualities in numeric format.
'''
###################################################################

###################################################################
def numeric_qualities(bases_qualities):
    int_bases_qualities= []
    for read in bases_qualities:
        read_qualities= []
        for qual in read:
            int_qual= ord(qual)-64
            read_qualities.append(int_qual)
        int_bases_qualities.append(read_qualities)

    return int_bases_qualities
'''
    Description: transposing int_bases_qualities array to get per position qualities of all reads, and calculate 5-number summary and the mean of each position, determine if module passed ,failed or there's a warning.
    Input: array of bases qualities in numeric format.
    Output: 2 arrays, one for each position 5-number summary, the second for the means, and 2 flags for warning and failure status.
'''
def five_number_summary(int_base_qualities):
    per_position_qualities= [list(filter(None, i)) for i in zip_longest(*int_base_qualities)]
    positions_summary= []
    means= []
    warning= False
    failure= False
    for position in per_position_qualities:
        position_summary= list(np.percentile(position, [10, 25, 50, 75, 90]))
        #we can issue here a threshold!!
        if position_summary[1]<10 or position_summary[2]<25:
            warning= True
        elif position_summary[1]<5 or position_summary[2]<20:
            failure= True
        position_summary= [round(x) for x in position_summary]
        mean= np.mean(position).round()
        positions_summary.append(position_summary)
        means.append(mean)
    return positions_summary, means, warning, failure
def draw_graph(positions_summary, means):
    plt.style.use('bmh')
    ax = sns.boxplot(data = positions_summary, color='yellow', dodge=True, linewidth=.5)
    ax.plot(means, label='Average quality per position')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
    ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
    plt.xlabel('Position in read')
    plt.ylabel('Quality scores')
    plt.title('Quality scores across all bases')
    plt.legend(loc= 'upper right')
    plt.savefig('box plot1.JPG', transparent=True, dpi=100)
    #plt.show()
if __name__ == '__main__':
    '''Reading sequences'''
    sequences, bases_qualities= readFastq_seq_and_qual(file_path)
    '''Calling numeric_qualities function'''
    int_bases_qualities= numeric_qualities(bases_qualities)
    '''Calling five_number_summary function'''
    positions_summary, means, warning, failure= five_number_summary(int_bases_qualities)
    draw_graph(positions_summary, means)