#بسم الله الرحمن الرحيم
#----------Per Sequence Quality Scores---------
file_path=input("Enter file path")
from itertools import zip_longest
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import seaborn as sns

from collections import Counter
import itertools  
###########################################################################
def Phred33ToQ(qual):
        return ord(qual)-64
##########################################################################
def average_list(M):
    return [round(sum(sublist) / len(sublist)) for sublist in M]
def perseq_quality(filename):
    avrs = []
    #quals = []
    B_list = []
    with open(filename) as fo:
        while True:
            fo.readline()
            seq = fo.readline()
            fo.readline()
            qual = fo.readline()  
            if len(seq) == 0:
                break
            num = []
            for i in range(len(qual)):
                a = round(Phred33ToQ(qual[i]))
                num.append(a)
            B_list.append(num)
    avrs = average_list(B_list)
    c = dict(Counter(avrs))
    c = dict(sorted(c.items(), key=lambda item: item[0], reverse=False))
    return c, B_list, avrs
c, B_list, avrs= perseq_quality(file_path)

#print(B_list)
#print(avrs)
#print(average_qual)
def draw_hist(c):
    plt.style.use('bmh')
    x= list(c.keys())
    y= list(c.values())
    plt.plot(x, y, color='r', label='Average Quality per read')
    plt.title('Per Sequence Quality Scores ')
    plt.xlabel('phred score')
    plt.ylabel('num of repetitions')
    plt.legend(loc= 'upper right')
    plt.savefig('box plot2.JPG', transparent=True, dpi=100)
    #plt.show()
draw_hist(c)
    
##############################################################

