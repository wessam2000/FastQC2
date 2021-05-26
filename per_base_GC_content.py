#بسم الله الرحمن الرحيم

#----------------Per Base GC Content-------------------
file_path=input("Enter file path")
from itertools import zip_longest
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import seaborn as sns

from collections import Counter
import itertools

list_sequences=[]#---list_sequences is a list created to contain all sequences
def list_seqs(file_path):
    with open(file_path) as sequencelength:
         while True:
                sequencelength.readline()
                sequences = sequencelength.readline()
                sequencelength.readline()
                sequencelength.readline()
                if len(sequences) == 0:
                    break
                list_sequences.append(sequences)
    return list_sequences
seqs=list_seqs(file_path)
#print(seqs)
import itertools
from itertools import zip_longest
def per_base_GC_content(seqs):
    per_base_seq = [list(filter(None, m)) for m in zip_longest(*seqs)]
    all_sequences = len(seqs)
    count_GC = []
    whole_GC = 0
    for base in per_base_seq:
        sum_GC = base.count("G")+base.count("C")
        count_GC.append(sum_GC)
        whole_GC += sum_GC
        GC_percentage = [0]*len(count_GC)
    for k in range(len(count_GC)):
        GC_percentage[k] = round((count_GC[k]/all_sequences)*100, 2)
    return count_GC, GC_percentage, whole_GC
count_GC, GC_percentage, whole_GC = per_base_GC_content(seqs)
# print(count_GC)
#print("GC% Per Base :",GC_percentage)
#print(len(GC_percentage))
#print('There are {} GC in whole file'.format(whole_GC))
##################################################

max_len = max(len(read) for read in list_sequences)
x = np.arange(max_len)
plt.style.use('bmh')

plt.plot(x, GC_percentage, color='r', label='%GC')
plt.title('GC content across all bases ')
plt.xlabel('position in read (bp')
plt.ylabel('Frequency')
plt.legend()
plt.savefig('box plot3.JPG', transparent=True, dpi=100)   


#plt.show()