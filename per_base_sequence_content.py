#بسم الله الرحمن الرحيم
#-----------Per Base Sequence Content-------------------
from itertools import zip_longest
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import seaborn as sns

from collections import Counter
import itertools
file_path=input("entre file path")
list_sequences = []
def readFastq(filename):
    seqs = []
    quals = []
    with open(filename) as fo:
        while True:
            fo.readline()
            seq=fo.readline()
            fo.readline()
            qual=fo.readline()
            if len(seq)==0:
                break
            seqs.append(seq)
    return seqs
sequences = readFastq(file_path)
def per_base_sequences_content(sequences):
    per_base_seq = [list(filter(None, m)) for m in zip_longest(*sequences)]
    all_sequences = len(sequences)
    count_A = []
    count_T = []
    count_C = []
    count_G = []
    for base in per_base_seq:
        num_A = base.count("A")
        num_T = base.count("T")
        num_C = base.count("C")
        num_G = base.count("G")
        count_A.append(num_A)
        count_T.append(num_T)
        count_C.append(num_C)
        count_G.append(num_G)
    A_percentage = [0]*len(count_A)
    T_percentage = [0] * len(count_T)
    C_percentage = [0] * len(count_C)
    G_percentage = [0] * len(count_G)
    for a in range(len(count_A)):
        A_percentage[a] = round((count_A[a]/all_sequences)*100, 2)
    for t in range(len(count_T)):
        T_percentage[t] = round((count_T[t] / all_sequences) * 100, 2)
    for c in range(len(count_C)):
        C_percentage[c] = round((count_C[c] / all_sequences) * 100, 2)
    for g in range(len(count_G)):
        G_percentage[g] = round((count_G[g] / all_sequences) * 100, 2)
    return A_percentage, T_percentage, C_percentage, G_percentage
A_percentage, T_percentage, C_percentage, G_percentage = per_base_sequences_content(sequences)
#print(A_percentage)
#print(T_percentage)
#print(C_percentage)
#print(G_percentage)
max_len = max(len(read) for read in sequences)
x = np.arange(max_len)
plt.style.use('bmh')
plt.plot(x, A_percentage, color='b', label='A')
plt.plot(x, T_percentage, color='r', label='T')
plt.plot(x, C_percentage, color='g', label='C')
plt.plot(x, G_percentage, color='k', label='G')
plt.title('sequence content across all bases ')
plt.xlabel('position in read (bp')
plt.ylabel('Frequency')
plt.legend()
plt.savefig('box plot9.JPG', transparent=True, dpi=100)
#plt.show()
pass
###############################################################