import sys, os
from tkinter import *


import subprocess


from myxml import MyXML
from table import GUI

def main(arg):
    file = arg[1]
    subprocess.call([sys.executable, './readRSRC.py', '-x', '-i' + file])
    for filename in os.listdir("."):
        if filename.endswith('FPHb.xml'):
            myxml = MyXML(filename)
            myxml.GetAllElementByTag('text')
            
            # create root window GUI
            root = Tk()
            t = GUI(root, myxml.elems, myxml, file)
            t.MakeTable()
            t.Show()
            

    

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print("usage: python3 Translate.py filename.vi")