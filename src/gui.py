from tkinter import *
from tkinter import ttk, filedialog
import main
import os

def calculate(*args):
    finalfile = main.x[0].split('.')[0] + '.8085'
    str1 = ''
    str1 = str1 + 'Interpreting...........\nRunning Assembler \n'
    meters.set(str1)
    main.runass()
    str1 = str1 + 'Assembler Completed \n' + 'Running Linker \n'
    meters.set(str1)
    main.runlin()
    str1 = str1 + 'Linker Completed \n' + 'Running Loader \n'
    meters.set(str1)
    main.runload()
    str1 = str1 + 'Loading Complete \n' + '\t\tFile is ready to simulate.\n' + '\t\tFile name is : ' + finalfile + '\n'
    meters.set(str1)

def askopenfilename(*args):
    # Get filename
    filename = filedialog.askopenfilename()
    # Open file
    if filename:
        inputFile = open(filename,"r")
        code = inputFile.read()
        lines = code.split('\n')
        finalfile = lines[0].split('.')[0] + '.8085'
        print (lines[0].split('.')[0])
        print (finalfile)
        main.x = []
        for line in lines:
            if line != '':
                main.x.append(line)

def opensimulator(*args):
    finalfile = main.x[0].split('.')[0] + '.8085'
    os.system('python3 sim.py '+finalfile)
    
root = Tk()
root.title("Assembler Linker Loader")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

ttk.Button(mainframe, text="Open File", command=askopenfilename).grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Run", command=calculate).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="Simulate", command=opensimulator).grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.bind('<Return>', calculate)

root.mainloop()
