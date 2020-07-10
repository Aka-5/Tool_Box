import os
from functools import partial
from tkinter import *

repertoire = os.chdir("/home/mathieu/scripttest")

def ecrire():

   os.chdir("/home/mathieu/scripttest")
   with open("mathieu.txt","a") as test1:
      test1.write("salut à toi jeune sffsfsfsfaventurier")

def suppfich():
   repertoire= os.chdir("/home/mathieu/Downloads")
   for filename in os.listdir(repertoire):
      os.remove(filename)


f1 = Tk()
f1.geometry("720x480")
button2 = Button(f1, text='ecrireture', command=ecrire)
button3 = Button(f1, text='supp', command=suppfich)

button2.pack()
button3.pack()
c