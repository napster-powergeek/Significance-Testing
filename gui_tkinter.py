# import module as md
try:
    import Tkinter as tk
except:
    import tkinter as tk

import tkinter.messagebox as tm
from tkinter.messagebox import showerror
from tkinter import BOTH, END, LEFT
import argparse

import csv
# from tabulate import tabulate
from tkinter.filedialog import askopenfilename
#from tkinter import *
import pandas as pd 
import numpy  as np 
from tkinter.simpledialog import askfloat


import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from scipy.stats import chi2
import os
import sys
import math
from scipy import stats
from operator import truediv
import statistics 
import xlsxwriter 

import matplotlib.image as mpimg 
import matplotlib.pyplot as plt

def left(s, amount):
    return s[:amount]

def test_func():
    print("Hello!")
def mean_fun(lst): 
    return sum(lst) / len(lst) 
def std_fun(test_list):
    return statistics.pstdev(test_list) 

def left(s, amount):
    return s[:amount]

def test_func():
    print("Hello!")
    
def __main__():
    chi_sq()
    z_t()
def mean_fun(lst): 
    return sum(lst) / len(lst) 
    
def std_fun(test_list):
    return statistics.pstdev(test_list)     


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()


class StartPage(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Significance Calculator", font=('Helvetica', 25, "bold")).grid(row=1,column = 1,ipadx ="10",pady="30", padx="20")
        tk.Label(self, text="What kind of a Test would you like to do?", font=('Helvetica', 10, "bold")).grid(row=2,column = 1,ipadx ="10",pady="20")
        tk.Button(self, text="Test for conversions (Chi Sq Test)",
                  command=lambda: master.switch_frame(PageOne)).grid(row=4,column = 1,ipadx ="10",pady="10")
        tk.Button(self, text="Test for time spent (Z- Test)",
                  command=lambda: master.switch_frame(PageTwo)).grid(row=5,column = 1,ipadx ="10",pady="10")
        tk.Button (self, text = "Exit").grid(row=6,column=1,pady="20")
                    

    def getExcel ():
            global df

            import_file_path = filedialog.askopenfilename()
            df = pd.read_excel (import_file_path)


class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self, text="Test for Conversions (Chi Sq Test)", font=('Helvetica', 15, "bold")).grid(row=1,column = 1,columnspan= 2,ipadx ="10",pady="10")
        self.v = tk.IntVar()
        tk.Radiobutton(self, text='Pre-Test Evlauaiton', variable=self.v,value =1 ).grid(row=2,column = 0,columnspan = 2,ipadx ="10",pady="10")
        tk.Radiobutton(self, text='Test Evaluation', variable=self.v,value=2).grid(row=2,column = 2,columnspan=2,ipadx ="10",pady="10")
        

            
    
    
        tk.Label(self, text="Page traffic", font=('Helvetica', 10, "bold")).grid(row=4,column = 0,ipadx ="10",pady="10")     
        tk.Label(self, text="Page Converted", font=('Helvetica', 10, "bold")).grid(row=5,column = 0,ipadx ="10",pady="10")
        tk.Label(self, text="Test%", font=('Helvetica', 10, "bold")).grid(row=6,column = 0,ipadx ="10",pady="10")
        tk.Label(self, text="Control%", font=('Helvetica', 10, "bold")).grid(row=7,column = 0,ipadx ="10",pady="10")
        tk.Label(self, text="Expected Uplift%", font=('Helvetica', 10, "bold")).grid(row=8,column = 0,ipadx ="10",pady="10")
        tk.Label(self, text="*Enter 7 day data only", font=('Helvetica', 10)).grid(row=9,column = 1,ipadx ="10",pady="10")
        
        self.Page_traffic = tk.Entry(self) 
        self.Page_orders = tk.Entry(self) 
        self.Test_p = tk.Entry(self)
        self.Control_p = tk.Entry(self)
        self.Uplift_p = tk.Entry(self) 

        self.Page_traffic.grid(row=4, column=1,ipadx ="10",pady="10",padx="10") 
        self.Page_orders.grid(row=5, column=1,ipadx ="10",pady="10",padx="10")
        self.Test_p.grid(row=6, column=1,ipadx ="10",pady="10",padx="10")
        self.Control_p.grid(row=7, column=1,ipadx ="10",pady="10",padx="10")
        self.Uplift_p.grid(row=8, column=1,ipadx ="10",pady="10",padx="10") 
     
    
        tk.Label(self, text="A traffic", font=('Helvetica', 10, "bold")).grid(row=4,column = 2,ipadx ="10",pady="10")
        tk.Label(self, text="A converted", font=('Helvetica', 10, "bold")).grid(row=5,column = 2,ipadx ="10",pady="10")
        tk.Label(self, text="B Traffic", font=('Helvetica', 10, "bold")).grid(row=6,column = 2,ipadx ="10",pady="10")
        tk.Label(self, text="B converted", font=('Helvetica', 10, "bold")).grid(row=7,column = 2,ipadx ="10",pady="10")
        tk.Label(self, text="Number of days", font=('Helvetica', 10, "bold")).grid(row=8,column = 2,ipadx ="10",pady="10")
     
        self.A_traffic = tk.Entry(self)
        self.A_orders = tk.Entry(self) 
        self.B_traffic = tk.Entry(self)
        self.B_orders = tk.Entry(self)
        self.n_days = tk.Entry(self) 
        

        self.A_traffic.grid(row=4, column=3,ipadx ="10",pady="10",padx="10") 
        self.A_orders.grid(row=5, column=3,ipadx ="10",pady="10",padx="10")
        self.B_traffic.grid(row=6, column=3,ipadx ="10",pady="10",padx="10")
        self.B_orders.grid(row=7, column=3,ipadx ="10",pady="10",padx="10")
        self.n_days.grid(row=8, column=3,ipadx ="10",pady="10",padx="10")
        
        
        
    
    
        tk.Button(self, text="Evaluate",
                  command=self.sel
                 ).grid(row=10,column = 1,columnspan =2, ipadx ="10",pady="10")

        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).grid(row=11,column = 1,columnspan =2, ipadx ="10",pady="10")
    def sel(self):
        selection = int(self.v.get())
        if(selection == 1):
            self.chi_sq2()
        else :
            self.chi_sq()
    def chi_sq(self):
    
        print("check1 chi_sq")
        a_visit = int(self.A_traffic.get())
        b_visit = int(self.B_traffic.get())
        a_conv  = int(self.A_orders.get())
        b_conv  = int(self.B_orders.get())
        n_d     = int(self.n_days.get())

        drops_a = a_visit-a_conv
        drops_b = b_visit-b_conv
        a_comvc = ((a_conv+b_conv)/(a_visit+b_visit))*a_visit
        b_comvc = ((a_conv+b_conv)/(a_visit+b_visit))*b_visit
        a_dps   = a_visit-a_comvc
        b_dps   = b_visit-b_comvc




        B = np.array([a_comvc, b_comvc, a_dps,b_dps])
        A = np.array([a_conv, b_conv, drops_a,drops_b])

        #Chi sq Distance

        D = np.sum(np.square(B-A)/B)

        pval = [chi2.sf(D, df=1)]
        pval = pd.DataFrame(pval)*100
        #pval.to_csv("pval.csv")

        #Plot p-value

        d = np.arange(0, 5, 0.1)
        plt.plot(d, chi2.pdf(d, df=1))
        plt.fill_between(d[d>D], chi2.pdf(d[d>D], df=1))
        plt.savefig('plot.png')
        #Test & Control



        #Chi sq Distance

        D = np.sum(np.square(B-A)/B)
        print("the Chi-sq Distance is "+str(round(D)))
        pval = [chi2.sf(D, df=1)]
        pval = pd.DataFrame(pval)*100
        p_val = pval.iloc[0,0]
        p_val1 = p_val/100
        ndt = ((n_d*95)/(100-round(p_val,2)))-n_d
        conf = str(100-round(p_val,2))

        # instead of pval in the datafrome print the value in the 4th quad as a percentage out of 100.



        print("The p- value is "+"\033[1m"  + str(round(p_val1,2))+ "\033[0m")
        print('The Confidence level is '+"\033[1m" +str(100-round(p_val,2))+ "%" + "\033[0m")
        if (100-round(p_val,2) < 95) and (ndt >= 0):
            print('More days to reach 95% confidence level: ' +str(round(ndt)))
        else:
            print('Test has already reached 95% confidence level')



        #Plot p-value


        d = np.arange(0, 5, 0.1)
        plt.plot(d, chi2.pdf(d, df=1), color = "grey")
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.fill_between(d[d>D], chi2.pdf(d[d>D], df=1), color = 'blue', label = 'p_val', alpha = 0.4)
        plt.fill_between(d[d<=D], chi2.pdf(d[d<=D], df=1), color = 'blue', label = 'confidence', alpha = 0.1)
        plt.legend(loc='right')

        plt.title('The p-value is '+ str(round(p_val/100,2)))
        if  (100-round(p_val,2) < 95) and (ndt >= 0):
            plt.suptitle('Number of days to reach 95% condfidence level: ' + str(round(ndt)) + '\n'+ '\n' + '\n'+ 'The present Confidence level is ' +left(conf,5)+ "%")
        else :
            plt.suptitle('The present Confidence is ' +str(100-round(p_val,2))+ "%" +' The test has already reached 95% confidence level ')



        plt.savefig('plot.png', bbox_inches='tight')

        img = mpimg.imread('plot.png') 

        os.system('plot.png')

#        pre_test_evaluation

    def chi_sq2(self):
       
        print("check chi sq 2 is working")
        visit             = int(self.Page_traffic.get())
        conv              = int(self.Page_orders.get())
        visit_ratio       = int(self.Test_p.get())
        visit_ratio1      = int(self.Control_p.get())
        user_value        = int(self.Uplift_p.get())  
        n_d               = 7
        uplift            = [5,10,user_value]


        for i in uplift:
            
            a_visit=visit*visit_ratio1/100
            a_conv=conv*visit_ratio1/100
            
            a_conv_rate = a_conv/a_visit
            
            b_visit = visit*visit_ratio/100
            b_conv = conv*visit_ratio/100
            b_conv_rate = a_conv_rate*(1+(i/100))
            b_conv = b_visit*b_conv_rate
            
            drops_a = a_visit-a_conv
            drops_b = b_visit-b_conv

            a_comvc = ((a_conv+b_conv)/(a_visit+b_visit))*a_visit
            b_comvc = ((a_conv+b_conv)/(a_visit+b_visit))*b_visit

            a_dps   = a_visit-a_comvc
            b_dps   = b_visit-b_comvc




            B = np.array([a_comvc, b_comvc, a_dps,b_dps])
            A = np.array([a_conv, b_conv, drops_a,drops_b])

            #Chi sq Distance

            D = np.sum(np.square(B-A)/B)

            pval = [chi2.sf(D, df=1)]
            pval = pd.DataFrame(pval)*100
            pval.to_csv("pval.csv")

            ndt = ((n_d*95)/(100-round(pval,2)))-n_d
            #Plot p-value

            d = np.arange(0, 5, 0.1)
            plt.plot(d, chi2.pdf(d, df=1))
            plt.fill_between(d[d>D], chi2.pdf(d[d>D], df=1))
            plt.savefig('plot.png')
            #Test & Control

            B = np.array([a_comvc, b_comvc, a_dps,b_dps])
            A = np.array([a_conv, b_conv, drops_a,drops_b])

            #Chi sq Distance

            D = np.sum(np.square(B-A)/B)

            pval = [chi2.sf(D, df=1)]
            pval = pd.DataFrame(pval)*100



            # instead of pval in the datafrome print the value in the 4th quad as a percentage out of 100.
            p_val = pval.iloc[0,0]
            p_val1 = p_val/100

            ndt = ((n_d*95)/(100-round(p_val,2)))-n_d

            print("The P-value for "+str(i)+ "% uplift is "+"\033[1m"  + str(round(p_val1,2))+ "\033[0m")

            if (100-round(p_val,2) < 95) and (ndt >= 0):
                print('More days to reach 95% confidence level: ' +str(round(ndt)))



            pval.to_excel("pval.xlsx")
        

            d = np.arange(0, 5, 0.1)
            plt.plot(d, chi2.pdf(d, df=1), color = "grey")
            plt.gca().spines['top'].set_visible(False)
            plt.gca().spines['right'].set_visible(False)
            plt.fill_between(d[d>D], chi2.pdf(d[d>D], df=1), label = [str(100-round(p_val,0))+"%",str(round(ndt))])
            plt.legend(loc='upper right')
            plt.title('The Present Confidence level & the number of days to reach 95% confidence are given for each uplift in the legend ')
            


        
        plt.savefig('plot.png', bbox_inches='tight')

        img = mpimg.imread('plot.png')  
        os.system('plot.png')


class PageTwo(tk.Frame):
    def __init__(self, master):
        

            
        
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Test for time spent (Z- Test)", font=('Helvetica', 15, "bold")).grid(row=1,column = 1,ipadx ="10",pady="10")
        
        self.entry = tk.Entry(self, width=40) 
        self.entry.grid(row=3,column=1)
        
        

        tk.Label(self, text="Please use the excel to enter the data for the Z-test", font=('Helvetica', 10)).grid(row=2,column = 1,ipadx ="10",pady="10")
        tk.Label(self, text="Excel file", font=('Helvetica', 10, "bold")).grid(row=3,column = 0,ipadx ="10",pady="10")
        
        browseButton_Excel = tk.Button(self, text='Browse File', width=25, bg = "light grey",   
                             fg = "black", command=self.button_browse_callback).grid(row=3, column=2,ipadx ="10",pady="10", padx="10")
        
        GoButton_Excel = tk.Button(self, text='Go', width=25, bg = "light grey",   
                             fg = "black", command=self.button_go_callback).grid(row=3, column=3,ipadx ="10",pady="10", padx="10")

        tk.Label(self, text="Number of days", font=('Helvetica', 10, "bold")).grid(row=4,column = 0,columnspan=1,ipadx ="10",pady="10")
        self.e1 = tk.Entry(self) 
        self.e1.grid(row=4, column=1,ipadx ="10",pady="10",padx="10") 
        
        
        tk.Button(self, text="Evaluate",command = self.z_t).grid(row=10,column = 1 ,ipadx ="10",pady="10")

        tk.Button(self, text="Go back to start page",
                      command=lambda: master.switch_frame(StartPage)).grid(row=11,column = 1,ipadx ="10",pady="10")


    def button_browse_callback(self):
            """ What to do when the Browse button is pressed """
            filename = askopenfilename()
            print(self.entry)
            self.entry.delete(0, END)
            self.entry.insert(0, filename)
        
        
    def button_go_callback(self):
            """ what to do when the "Go" button is pressed """
            input_file = self.entry.get()
            filename = input_file
            
            self.A = pd.read_excel(filename,sheet_name = "ZTestA")
            self.B = pd.read_excel(filename,sheet_name = "ZTestB")
            

    def z_t(self):

                def foo(Ao,A):
                    try:
                        return (ai/bi for ai,bi in zip(Ao,A))
                    except ZeroDivisionError:
                        return 0
                
                C = self.A
                D = self.B
                A = C
                B = D
                n_d     =  int(self.e1.get())

                #mean avg. time of test observations
                m_A = A.mean()[1]
                m_B = B.mean()[1]

                #std dev of avg. time
                std_A = A.std()[1]
                std_B = B.std()[1]
                n_A = len(A)
                n_B = len(B)

                #Z score
                Z = (m_B - m_A)/np.sqrt((std_B**2)/n_B + (std_A**2)/n_A)
                pvalue = norm.sf(Z)
                #n_d = len(A)

                pval = []
                pval.append(pvalue)
                pval = pd.DataFrame(pval)*100
                p_val = pval.iloc[0,0]
                p_val1 = p_val/100
                ndt = ((n_d*95)/(100-round(p_val,2)))-n_d
                conf = str(100-round(p_val,2))
                print("the p- value is "+"\033[1m"  + str(round(p_val1,2))+ "\033[0m")
                print('the Confidence is '+"\033[1m" + left(conf,5) + "%" + "\033[0m")
                pval.to_excel("pval.xlsx")


                if (100-round(p_val,2) < 95) and (ndt >= 0):
                    print('More days to reach 95% confidence level: ' +str(round(ndt)))
                else:
                    print('The test has already reached 95% confidence level')


                #Plotting results: choose range by rounding off z score to upper number
                z = np.arange(-3, 3, 0.1)
                plt.plot(z, norm.pdf(z), color = 'grey')
                plt.gca().spines['top'].set_visible(False)
                plt.gca().spines['right'].set_visible(False)
                plt.fill_between(z[z<=Z], norm.pdf(z[z<=Z]), color = 'blue', label = 'Confidence', alpha = 0.05)
                plt.fill_between(z[z>Z], norm.pdf(z[z>Z]), color = 'blue', label = 'p_val', alpha = 0.4)
                plt.legend(loc='right')

                plt.title('The P-value is '+ str(round(p_val/100,2)) +'  ' +'and the present Confidence level is ' + left(conf,5) + "%")
        #         plt.suptitle('the Confidence is ' +str(100-round(p_val,2))+ "%")
                if (100-round(p_val,2) < 95) and (ndt >= 0):
                    plt.suptitle('More days to reach 95% condfidence level: ' +str(round(ndt)) )
                else :
                    plt.suptitle('The test has already reached 95% confidence level' )
                plt.savefig('plot.png')
                # Read Images 
                img = mpimg.imread('plot.png')  
                os.system('plot.png')

                workbook = xlsxwriter.Workbook('pval.xlsx')
                worksheet = workbook.add_worksheet()
                worksheet.insert_image('B2', 'plot.png')       
if __name__ == "__main__":
    app = SampleApp()
    
    app.mainloop()
