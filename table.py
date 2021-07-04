from tkinter import *
import xml.etree.ElementTree as ET 
import subprocess, glob, sys, os
from tkinter import messagebox

from myxml import MyXML
  
class Row:
    def __init__(self, root, rowInd, numCol, data):
        self.root = root
        self.data = data
        self.content = [self.data[0]]
        for j in range(1, numCol):
            e = Entry(self.root, width=20, fg='blue',
                                font=('Arial',16,'bold'))
            e.grid(row=rowInd, column=j)
            e.insert(END, self.data[j])
            self.content.append(e)

    def GetRow(self):
        return self.content
  
class GUI:
    def __init__(self, root, data, myxml: MyXML, file):
        self.myxml = myxml
        self.root = root
        self.data = data
        self.file = file
        self.rows = []

        self.canvas = Canvas(self.root)
        self.scrollbar = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)      

    def Show(self):
        self.root.mainloop()

    def MakeTable(self):
        total_rows = len(self.data)
        total_columns = len(self.data[0])   
        for i in range(total_rows):
            row = Row(self.scrollable_frame, i, total_columns, self.data[i])
            self.rows.append(row)
        
        r = len(self.data)
        c = len(self.data[0])
        B = Button(self.root, text ="Save", command = self.Save)
        B.pack(side="bottom")     
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
    
    def Save(self):
        for row in self.rows:
            if row.GetRow()[2].get() == "":
                continue 
            row.GetRow()[0].text = row.GetRow()[2].get()
        self.myxml.Save()

        # recreate .vi file and delete other file
        subprocess.call([sys.executable, './readRSRC.py', '-c', '-m' + self.file.split('.')[0]+".xml"])
            
        # delete file
        for f in glob.glob(self.file.split('.')[0] + "*"):
            if f.endswith('.vi'):
                continue
            os.remove(f)
        
        messagebox.showinfo("OK", "Save Successfully!")
        




