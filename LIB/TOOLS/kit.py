import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import xlsxwriter

class KIT:

    def __init__(self,temp):
        self.date   = []
        self.tag    = []
        self.titel  = []
        self.amount = []

        for range in temp:
            self.date.append(range[0])
            self.tag.append(range[1])
            self.titel.append(range[2])
            self.amount.append(range[3])


    def a_kit(self):
        ini = 0
        ino = 0
        inv = 0

        i = 0
        
        for i in range(len(self.date)):
            if self.tag[i] == 'IN  ':
                ini += self.amount[i]
            elif self.tag[i] == 'Out ':
                ino += self.amount[i]
            elif self.tag[i] == 'INV ':
                inv += self.amount[i]
        return ini,ino,inv

    def g_kit(self,type):
        x = []
        y = []

        if type=='ALL':
            x = self.date
            y = self.amount

        else:
            for i in range(len(self.date)):
                if self.tag[i] == type:
                    x.append(self.date[i])
                    y.append(self.amount[i]) 


        plt.plot(x,y,color='blue',marker='o')
        plt.title('Amount Transaction',fontsize=14)
        plt.xlabel('Date',fontsize=14)
        plt.ylabel('Amount',fontsize=14)
        plt.grid(True)
        plt.show()

    def f_kit(self, type, name):
        name = name + '.xlsx'
        rowindex = 2
        newfile = xlsxwriter.Workbook(name)

        worksheet = newfile.add_worksheet("Transactions")

        worksheet.write('A1','Date')
        worksheet.write('B1','Tag')
        worksheet.write('C1','Titel')
        worksheet.write('D1','Amount')

        if type == 'ALL':
            for i in range(len(self.date)):
                
                worksheet.write('A' + str(rowindex),self.date[i])
                worksheet.write('B' + str(rowindex),self.tag[i])
                worksheet.write('C' + str(rowindex),self.titel[i])
                worksheet.write('D' + str(rowindex),self.amount[i])                  

                rowindex = rowindex + 1         

        else:    
            for i in range(len(self.date)):
                if self.tag[i] == type:
                    worksheet.write('A' + str(rowindex),self.date[i])
                    worksheet.write('B' + str(rowindex),self.tag[i])
                    worksheet.write('C' + str(rowindex),self.titel[i])
                    worksheet.write('D' + str(rowindex),self.amount[i])                  

                rowindex = rowindex + 1         





        newfile.close()





#############################################################################
if __name__ == '__main__':
    print("Kit.py")