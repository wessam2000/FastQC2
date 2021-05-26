#بسم الله الرحمن الرحيم
#--------------overrepresented kemers--------------------------------------------

file_path=input("Enter file path")
import matplotlib.pyplot as plt
import numpy as np
from itertools import islice
from itertools import zip_longest
import re
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
    Description: extracting 5-mers from all sequences.
    Input: array of sequences.
    Output: array of arrays, each contains a sequence 5-mers.
'''
def extract_kmers(sequences):
    kmers_list= []
    for sequence in sequences:
        sequence = re.sub('N', '', sequence)
        kmers_in_read= []
        for i in range(len(sequence)-5+1):
            kmer= sequence[i:i+5]
            kmers_in_read.append(kmer)
        kmers_list.append(kmers_in_read)
    return kmers_list
'''
    Description: counting each 5-mer occurrences in whole sequences, then sorting the values in descending order.
    Input: array of arrays, each contains a sequence's 5-mers.
    Output: sorted dictionary of each 5-mer(as keys), count of the 5-mer(as values).
'''
def kmers_count(kmers_list):
    kmers_count_dect= {}
    for kmers_in_read in kmers_list:
        for kmer in kmers_in_read:
            if kmer not in kmers_count_dect:
                kmers_count_dect[kmer]= 1
            else:
                kmers_count_dect[kmer] += 1
    kmers_count_dect= dict(sorted(kmers_count_dect.items(), key=lambda item: item[1], reverse=True))
    return kmers_count_dect
'''
 Description: extracting most max 6 5-mers represented in sequences.
    Input: sorted dictionary of each 5-mer(as keys), count of the 5-mer(as values).
    Output: array of most max 6 5-mers.
'''
def return_6_max_kmers(kmers_count_dect):
    most_6_kmers= list(islice(kmers_count_dect, 6))
    return most_6_kmers
'''
    Description: transposing kmers list to get list of kmers per position, then compute their count and convert them into percentage values.
    Input: 2 arrays, one contains most max 6 5-mers, second is array of arrays of each contains a sequence 5-mers.
    Output: array of most max 5-mers percentage frequencies.
'''
def final(most_6_kmers, kmers_list):
    per_position_kmers= [list(filter(None, i)) for i in zip_longest(*kmers_list)] # transposing
    most_6_kmers_count= []
    new_percentage= []
    for kmer in most_6_kmers:
        kmer_count= []
        for position in per_position_kmers:
            kmer_count_per_position= position.count(kmer)
            kmer_count.append(kmer_count_per_position)
        most_6_kmers_count.append(kmer_count)
        kmer_count_percentage= []
        for kmer_count_per_position in kmer_count:
            position_percentage= round((kmer_count_per_position/total_sequences)*100, 2)
            kmer_count_percentage.append(position_percentage)
        new_percentage.append(kmer_count_percentage)
    return new_percentage
'''
    Description: drawing a graph to show frequencies of overrepresented k-mers per position.
    Input: array of k-mers percentage per position, array of most 6 overrepresented k-mers.
    Output: graph of k-mers frequencies per position over reads.
'''
def draw_hist(new_percentage, most_6_kmers):
    plt.style.use('bmh')
    x= np.arange(max_len-5+1)
    axes= plt.gca()
    axes.set_ylim([0,100])
    plt.xlabel('Position in read (bp)')
    plt.ylabel('Frequency')
    plt.title('k-mers frequencies per position over reads')
    plt.plot(x, new_percentage[0], label=most_6_kmers[0])
    plt.plot(x, new_percentage[1], label=most_6_kmers[1])
    plt.plot(x, new_percentage[2], label=most_6_kmers[2])
    plt.plot(x, new_percentage[3], label=most_6_kmers[3])
    plt.plot(x, new_percentage[4], label=most_6_kmers[4])
    plt.plot(x, new_percentage[5], label=most_6_kmers[5])
    plt.legend(loc= 'upper right')
    plt.savefig('box plot8.JPG', transparent=True, dpi=100)
   # plt.show()
if __name__ == '__main__':
    '''Reading sequences'''
    sequences= readFastq_seq(file_path)
    total_sequences= len(sequences)
    max_len= max(len(read) for read in sequences)
    '''Calling extract_kmers function'''
    kmers_list= extract_kmers(sequences)
    '''Calling kmers_count function'''
    kmers_count_dect= kmers_count(kmers_list)
    '''Calling return_6_max_kmers function'''
    most_6_kmers= return_6_max_kmers(kmers_count_dect)
    '''Calling final function'''
    new_percentage= final(most_6_kmers, kmers_list)
    '''Drawing graph'''
    draw_hist(new_percentage, most_6_kmers)
    ###############################################################33
