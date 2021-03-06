#بسم الله الرحمن الرحيم
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import sys
import pickle
#########################################################################################
import ntpath
from pyqtgraph import PlotWidget
import numpy as np


########################################################################################
MainUI,_ = loadUiType('FASTQC2project.ui')

class Main(QMainWindow , MainUI):
    def __init__(self , parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handel_buttons()
        self.openfilepathtab()
        self.ui_changes()

    ####################################################################################
        
    def ui_changes(self):
        self.tabWidget.tabBar().setVisible(False)
            
    def code_connect(self):
            pass
    ###################################################################################
    ###################################################################################    
    def handel_buttons(self):
        self.pushButton.clicked.connect(self.openfilepathtab)
        self.pushButton_2.clicked.connect(self.openbasicstaatisticstab)
        self.pushButton_3.clicked.connect(self.openperbasesequencequalitytab)
        self.pushButton_4.clicked.connect(self.openpersequencequalityscoretab)
        self.pushButton_5.clicked.connect(self.openpersequencequalitycontenttab)
        self.pushButton_6.clicked.connect(self.openperbaseGCcontenttab)
        self.pushButton_7.clicked.connect(self.openpersequenceGCcontenttab)
        self.pushButton_8.clicked.connect(self.openperbaseNcontenttab)
        self.pushButton_9.clicked.connect(self.opensequencelengthdistributiontab)
        self.pushButton_10.clicked.connect(self.openduplicatesequencestab)
        self.pushButton_11.clicked.connect(self.openoverrepresentedsequencestab)
        self.pushButton_12.clicked.connect(self.openoverrepresentedkmertab)
        self.pushButton_13.clicked.connect(self.filepath)
        self.pushButton_14.clicked.connect(self.filename)
        self.pushButton_16.clicked.connect(self.filetype)
        self.pushButton_17.clicked.connect(self.encoding)
        self.pushButton_18.clicked.connect(self.totalsequences)
        self.pushButton_19.clicked.connect(self.maximumread)
        self.pushButton_20.clicked.connect(self.maximumreadlength)
        self.pushButton_21.clicked.connect(self.minimumread)
        self.pushButton_22.clicked.connect(self.minimumreadlength)
        self.pushButton_23.clicked.connect(self.totallength)
        self.pushButton_25.clicked.connect(self.GC_content)
        self.pushButton_26.clicked.connect(self.sequenceswithnoN)
        self.pushButton_15.clicked.connect(self.show_per_base_quality_scores)
        self.pushButton_27.clicked.connect(self.show_per_sequence_quality_scores)
        self.pushButton_28.clicked.connect(self.show_per_base_sequence_content)
        self.pushButton_29.clicked.connect(self.show_per_base_GC_content)
        self.pushButton_30.clicked.connect(self.show_per_sequence_GC_content)
        self.pushButton_34.clicked.connect(self.show_overrepresented_sequences)

        self.pushButton_31.clicked.connect(self.show_per_base_N_content)
        self.pushButton_32.clicked.connect(self.show_sequence_length_distribution)
        self.pushButton_33.clicked.connect(self.show_duplicate_sequences)
        
        #self.pushButton_34.clicked.connect(self.show_per_base_sequence_quality)
        self.pushButton_35.clicked.connect(self.show_overrepresented_kmers)
        
        
    
    def show_per_base_quality_scores(self):
        self.label_2.setPixmap(QtGui.QPixmap("box plot1"))

    def show_per_sequence_quality_scores(self):
        self.label_3.setPixmap(QtGui.QPixmap("box plot2")) 

    def show_per_base_sequence_content(self):
        self.label_4.setPixmap(QtGui.QPixmap("box plot9"))      

    def show_per_base_GC_content(self):
        self.label_5.setPixmap(QtGui.QPixmap("box plot3"))  

    def show_per_sequence_GC_content(self):
        self.label_6.setPixmap(QtGui.QPixmap("box plot4")) 


    def show_per_base_N_content(self):
        self.label_7.setPixmap(QtGui.QPixmap("box plot5"))  


    def show_sequence_length_distribution(self):
        self.label_8.setPixmap(QtGui.QPixmap("box plot6")) 

    def show_duplicate_sequences(self):
        self.label_9.setPixmap(QtGui.QPixmap("box plot7"))

        
    def show_overrepresented_kmers(self):
        self.label_11.setPixmap(QtGui.QPixmap("box plot8.JPG")) 

          

    
    def show_overrepresented_sequences(self):
        overrep_seq=open("filename",'r')
        overrep_seq.close
        fo=overrep_seq.read()
        #print(fo)
        self.label_10.setText(fo)


        
        
        ##########################################################    
        ##########################################################
        #C:\Users\gamel\OneDrive\Desktop\FGD1\downloadflask\sample.fastq
        #basicstatistics
    file_path=True
    list_sequences=[]
    seq=""
    sequencelength=0 
    firstt=0
    lengthx=0
    lengthn=0
    minread=""
    maxread=""
    minlength=""
    maxlength=""
    i = 0
    GC_sum = 0
    sequences_=True
    j = 0
    sum_bases = 0
    sum_=0
    x = 0
    N_list = []
    ####################################################################
    ####################################################################
    def  filepath (self):
        
        global file_path
        file_path=self.lineEdit.text()
    ####################################################################
    ####################################################################     
    def filename(self):
        file_path=self.lineEdit.text()
        FN=ntpath.basename(file_path)
        file_name=self.lineEdit_2.setText(FN)
    ####################################################################
    ####################################################################     

    def filetype(self):
        global list_sequences
        global sequencelength
        global first
        global maxread
        global minlength
        global maxlength
        global i
    
        with open (file_path) as sequencelength:
            
            list_sequences=[]
            while True:
                sequencelength.readline()
                sequences=sequencelength.readline().strip()
                sequencelength.readline()
                sequencelength.readline()
                if len(sequences)==0:
                    break
                list_sequences.append(sequences)
        first=list_sequences[0]
        if list_sequences[0].isnumeric==True:
            filetype=self.lineEdit_6.setText("Colorspace Data")
        else:
             filetype=self.lineEdit_6.setText("Conventional base calls")    
    ####################################################################################
    ####################################################################################
    def encoding (self):
        encoding_=self.lineEdit_5.setText("Illumina 1.9/sanger")
    ####################################################################################
    ####################################################################################
    def totalsequences(self):
        totalsequences_=str(len(list_sequences))
        #total=str(totalsequences_)

        total_seq=self.lineEdit_4.setText(totalsequences_)  
    #####################################################################################
    #####################################################################################
    def maximumread(self):
        maxread = max(list_sequences, key=len)
        maxreadlength=self.lineEdit_3.setText(maxread)

    def maximumreadlength(self):
        maxread = max(list_sequences, key=len)
        lengthx=len(maxread) 
        maxlength=str(len(maxread))
        maxreadlength=self.lineEdit_8.setText(maxlength)
    ######################################################################################
    ######################################################################################3
    def minimumread(self):
        minread = min(list_sequences, key=len)
        maxreadlength=self.lineEdit_10.setText(minread)

    def minimumreadlength(self):
        minread = min(list_sequences, key=len)
        lengtn=len(minread) 
        minlength=str(len(minread))
        maxreadlength=self.lineEdit_7.setText(minlength) 
    ########################################################################################
    #########################################################################################
    def totallength(self):
        global lengthn
        global lengthx
        maxread = max(list_sequences, key=len)
        lengthx=len(maxread) 
        maxlength=str(len(maxread))
        minread = min(list_sequences, key=len)
        lengthn=len(minread)
        minlength=str(len(minread))
        if lengthn!=lengthx:
            totallen=self.lineEdit_11.setText(minlength+"-"+maxlength)
        else:
            totallen=self.lineEdit_11.setText(minlength+" :all reads have the same length")
    #########################################################################################
    #########################################################################################
    def GC_content(self):
        global i
        i=0
        
        global j
        j=0
        global sum_bases
        while i < len(list_sequences):
            global seq
            global GC_sum
            GC_sum=0
            seq=list_sequences[i]
            GC_content = seq.count(("G"))+seq.count(('C'))
            # print(GC_content)
            sum_ = GC_sum+GC_content
            i = i+1

        while j < len(list_sequences):
            global sum_bases
            sum_bases=0
            seq_=list_sequences[j] 
            seq_length = (len(seq_))
            sum_bases = sum_bases+seq_length
            j = j+1
        GC_percentage =round(sum_/sum_bases*100,2)
        kk=str(GC_percentage) 
        gc=self.lineEdit_13.setText(kk) 
    ##############################################################################
    ##############################################################################
    def sequenceswithnoN(self):
        global x
        x=0
        global N_list
        N_list=[]
        while x < len(list_sequences):
             
             my_sequence = list_sequences[x]
             N_content = my_sequence.count("N") 
             N_list.append(N_content)
             x = x+1
        no_N =str( N_list.count(0))     
        noNpercentage=self.lineEdit_15.setText(no_N)     
################################################################################################################
###############################################################################################################
            
    def basicstatistics (self):
            pass
    def perbasesequencequaliy(self):
            pass
    def persequencequalityscores(self):
            pass
    def perbasesequencecontent(self):
            pass
    def perbaseGCcontent (self):
            pass
    def persequenceGCcontent (self):
            pass
    def perbaseNcontent (self):
            pass
    def sequencelengthdistribution(self):
            pass
    def duplicatesequences (self):
            pass
    def overrepresentedsequences(self):
            pass
    def overrepresentedkmers(self):
            pass
        #########################################################
    #print(filename(file_path))
       
    #####################################################################################################
    #####################################################################################################
    def openfilepathtab(self):
        self.tabWidget.setCurrentIndex(0)

    def openbasicstaatisticstab(self):
        self.tabWidget.setCurrentIndex(1)

    def openperbasesequencequalitytab(self):
        self.tabWidget.setCurrentIndex(2) 

    def openpersequencequalityscoretab(self):
        self.tabWidget.setCurrentIndex(3)   

    def openpersequencequalitycontenttab(self):
        self.tabWidget.setCurrentIndex(4) 

    def openperbaseGCcontenttab(self):
        self.tabWidget.setCurrentIndex(5)

    def openpersequenceGCcontenttab(self):
        self.tabWidget.setCurrentIndex(6)  

    def openperbaseNcontenttab(self):
        self.tabWidget.setCurrentIndex(7)   

    def opensequencelengthdistributiontab(self):
        self.tabWidget.setCurrentIndex(8)

    def openduplicatesequencestab(self):
        self.tabWidget.setCurrentIndex(9)

    def openoverrepresentedsequencestab(self):
        self.tabWidget.setCurrentIndex(10) 

    def openoverrepresentedkmertab(self):
        self.tabWidget.setCurrentIndex(11)
    #################################################################################################
    ################################################################################################## 
            

def main():
        app = QApplication(sys.argv)
        window = Main()
        window.show()
        app.exec_()


if __name__=='__main__':
    main()
