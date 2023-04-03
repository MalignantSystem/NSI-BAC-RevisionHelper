from os import listdir,getcwd,system
from webbrowser import open_new as openfile
from random import randint

pdfdirectory = getcwd() + '/pdf_folder/'
files = listdir(pdfdirectory)

def introduction():
    system('clear')
    print('Welcome, brave students!\n'
          "I'm certain you have realised that studying the practical exam using the websites given to us is very unpractical...\n"
          "Thus, I made this script to help you ( and myself :^] ) study effeciently.\n"
          
          "Put the pdf files that you need to revise in the folder named 'pdf_folder', then use the function 'openrandomfile() to open a random file from said directory.\n"
          "Alternatively, to open a file and remove it from the pool of subjects (like a checklist), use openrandomremove().\n"
          "Good luck!\n\n")

def openrandomfile():
    '''
    Python function that randomly opens a file from the folder in its directory called "pdf_folder",
    allowing a student to randomly open a pdf file to study for his NSI baccalaureat.
    '''
    if len(files) == 0:
        return ("The files directory is empty.")
    filetoOpen = files[randint(0, len(files)-1)]
    openfile(pdfdirectory + filetoOpen)
    print("Opening " + filetoOpen + "...")

def openrandomremove():
    '''
        Python function that randomly opens a file from the folder in its directory called "pdf_folder",
        and then removes it from the "files" array.runfile('/home/schlorfo/PycharmProjects/RevisionHelper/main.py', wdir='/home/schlorfo/PycharmProjects/RevisionHelper')
        This script allows a student to randomly open a pdf file to study for his NSI baccalaureat.
        '''
    if len(files) == 0:
        return ("The files directory is empty, or; you are all done!")
    filetoOpen = files.pop(randint(0, len(files) - 1))
    openfile(pdfdirectory + filetoOpen)
    print("Opening " + filetoOpen + "...")

introduction()

