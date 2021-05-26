#بسم الله الرحمن الرحيم
#-----------Per Sequence GC content--------

file_path=input("Enter file path")
from itertools import zip_longest
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import seaborn as sns

from collections import Counter
import itertools



def list_seqs(file_path):
    list_sequences=[]#---list_sequences is a list created to contain all sequences
    with open(file_path) as sequencelength:
         while True:
                sequencelength.readline()
                sequences = sequencelength.readline().strip()
                sequencelength.readline()
                sequencelength.readline()
                if len(sequences) == 0:
                    break
                list_sequences.append(sequences)
    return list_sequences
list_sequences= list_seqs(file_path)
#print(list_sequences)
def per_sequence_GC_content(list_sequences):
    #all_sequences = len(list_sequences)
    count_GC = []
    percentage_mean_GC= []
    whole_GC = 0
    for seq in list_sequences:
        sum_GC = seq.count("G")+seq.count("C")
        count_GC.append(sum_GC)
        whole_GC += sum_GC
        mean_GC= round((sum_GC/len(seq))*100)
        percentage_mean_GC.append(mean_GC)
    return count_GC, percentage_mean_GC, whole_GC
count_GC, percentage_mean_GC, whole_GC= per_sequence_GC_content(list_sequences)
#print(count_GC, '\n')
#print(percentage_mean_GC)
#print("GC% per sequence:",percentage_mean_GC)
#print(len(percentage_mean_GC))
#print('There are {} GC in whole file'.format(whole_GC))
c = dict(Counter(percentage_mean_GC))
c = dict(sorted(c.items(), key=lambda item: item[0], reverse=False))
#print(c)
def draw_hist(c):
    plt.style.use('bmh')
    x= list(c.keys())
    y= list(c.values())
    plt.plot(x, y, color='r', label='%GC')
    plt.title('GC content across all sequences')
    plt.xlabel('Mean GC content (%)')
    plt.ylabel('Frequency')
    plt.legend(loc= 'upper right')
    plt.savefig('box plot4.JPG', transparent=True, dpi=100)
    #plt.show()
draw_hist(c)