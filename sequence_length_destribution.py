#بسم الله الرحمن الرحيم
#---------Sequence Length Distribution---------
from collections import Counter
import itertools
import matplotlib.pyplot as plt
import numpy as np
file_path=input("Enter file path")
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
list_sequences=list_seqs(file_path)
#max_len = max(len(read) for read in list_sequences)
#print(max_len)
#print(list_sequences)
seqs_length = []
for sequence in list_sequences:
    length_of_each_sequence = len(sequence)
    seqs_length.append(length_of_each_sequence)
#print("Sequence Length Distribution : ",seqs_length)
c = dict(Counter(seqs_length))  
c = dict(sorted(c.items(), key=lambda item: item[0], reverse=False))
def draw_hist(c):
    plt.style.use('bmh')
    x= list(c.keys())
    y= list(c.values())
    plt.plot(x, y, color='r', label='Sequence length')
    plt.title('Sequence length distribution')
    plt.xlabel('Sequences Length')
    plt.ylabel('Frequency')
    plt.legend(loc= 'upper right')
    plt.savefig('box plot6.JPG', transparent=True, dpi=100)
    #plt.show()
draw_hist(c)

###############################################

