# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# ch18_1.py
from tkinter import *
import random       
import csv
               

def printInfo():                    # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(),e2.get()))
    
def randomData():                    # 列印輸入資訊
    x=0
    outfn = 'dataOut.csv' 
    with open(outfn, 'w', newline = '') as csvFile:
        while True:
            csvWriter = csv.writer(csvFile, delimiter='\t')
            csvWriter.writerow(['data', 'index', 'randomNumber'])
            csvWriter.writerow(['RandomData', random.choice([1,2,3,4,5,6]), '1']) 
            if(x>10):
                break      
    # for i in range(10):
    #     print(random.choice([1,2,3,4,5,6]), end=",")
          
window = Tk()
window.title("Data Generator")             # 視窗標題

lab1 = Label(window,text="Account ").grid(row=0)
lab2 = Label(window,text="Password").grid(row=1)

e1 = Entry(window)                  # 文字方塊1
e2 = Entry(window,show='*')         # 文字方塊2
e1.grid(row=0,column=1)             # 定位文字方塊1
e2.grid(row=1,column=1)             # 定位文字方塊2

btn1 = Button(window,text="Print",command=printInfo)
# sticky=W可以設定物件與上面的Label切齊, pady設定上下間距是10
btn1.grid(row=2,column=0,sticky=W,pady=10)  
btn2 = Button(window,text="Quit",command=window.quit)
# sticky=W可以設定物件與上面的Entry切齊, pady設定上下間距是10
btn2.grid(row=2,column=1,sticky=W,pady=10)
btn3 = Button(window,text="Random Number",command=randomData)
# sticky=W可以設定物件與上面的Entry切齊, pady設定上下間距是10
btn3.grid(row=2,column=2,sticky=W,pady=10)



window.mainloop()