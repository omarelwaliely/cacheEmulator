from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from collections import defaultdict
import math
import binascii

filename = ""
totalSize = 0
lineSize = 0
cycles = 0

class Data:
    validbit = '0'
    tag = "N/A"
    memory = None


def fileclick():
    global filename
    filename = filedialog.askopenfilename()


def simulation(line,size,cycle,frame,button,root):
    global filename
    global totalSize
    global lineSize
    global cycles
    if filename == "":
        messagebox.showerror(message="You did not select a file!",title = "File Error")
    elif line.get() == "" or cycle.get() == "" or size.get() == "":
        messagebox.showerror(message="You did not fill in all the labels!",title = "Empty Label Error")
    elif not (line.get().isnumeric() and cycle.get().isnumeric() and size.get().isnumeric()):
        messagebox.showerror(message="Please enter valid numbers!", title = "Number Error")
    elif int(cycle.get()) < 1 or int(cycle.get()) > 10:
        messagebox.showerror(message="Please enter a clock cycle between 1 and 10!", title = "Cycle Error")
    else:
        cycles = int(cycle.get())
        totalSize = int(size.get())
        lineSize = int(line.get())
        frame.destroy()
        button.destroy()
        simulatorScreen(root)


def simulatorScreen(root):
    root.geometry("800x800")
    try:
        index = int(math.log2(totalSize/lineSize))
        memory = []
        for i in range((2**(index)-1)):
           x = Data()
           memory.append(x)
        disp = math.log2(lineSize)
        tag = int(32 - (index + disp))
    except:
        messagebox.showerror(message="Your sizes were insufficent please try again", title = "Incorrect Syntax")
        root.destroy()
        startScreen()
        return


    scrollframe = Scrollbar(root)
    scrollframe.pack(side=RIGHT, fill=Y)
    test= Text(root, width = 80, height = 80, wrap = NONE,
                 yscrollcommand = scrollframe.set)
    with open(filename) as file:
        lines = (line.rstrip() for line in file) 
        lines = (line for line in lines if line) #removes empty lines
        j= 0 #number of accesses
        test.insert(END,"Initial Data")
        for i in range((2**index) -1):
            test.insert(END,"\nIndex: "+ "{0:08b}".format(int(str(i),10)) + "   Valid bit: " + memory[i].validbit + "  Tag: "+ memory[i].tag + "\n")
        for line in lines:
            try:
                curr = "{0:08b}".format(int(line, 16))
                curr = curr.rjust(32, '0')
                if(memory[int(curr[tag:(tag+index)],2)].tag == "N/A"):
                    memory[int(curr[tag:(tag+index)],2) -1].tag = curr[:tag]
                    memory[int(curr[tag:(tag+index)],2) -1].validbit = '1'
                    print("BBING BONG TIME")
                    missTest = "MISS"
                elif(memory[int(curr[tag:(tag+index)],2) -1].tag== curr[:tag]):
                    missTest = "HIT"
                else:
                    memory[int(curr[tag:(tag+index)],2) -1].tag = curr[:tag]
                    memory[int(curr[tag:(tag+index)],2) -1].validbit = '1'
                    missTest = "MISS"
                test.insert(END,"Access #" + str(j+1) + "\n" + missTest)
                j = j+1
                for i in range((2**index) -1):
                    test.insert(END,"\nIndex: "+ "{0:08b}".format(int(str(i),10)) + "   Valid bit: " + memory[i].validbit + "  Tag: "+ memory[i].tag + "\n")
                test.insert(END,"\nHit Ratio: " +"Miss Ratio: "+ "AMAT: " + "\n\n")
            except:
                messagebox.showerror(message="You inputted the memory wrong!", title = "Incorrect Syntax")
                return
    test.pack()
                






def startScreen():
    root = Tk()
    root.title("Cache Simulator")
    root.geometry("400x300")
    frame = LabelFrame(root,text="")
    frame.pack()
    sizeLabel = Label(frame,text = "Total Cache Size",width = 20)
    sizeEntry = Entry(frame)
    sizeLabel.grid(column=0,row=0)
    sizeEntry.grid(column=1,row=0)
    lineLabel = Label(frame,text = "Cache Line Size",width = 20)
    lineEntry = Entry(frame)
    lineLabel.grid(column=0,row=1)
    lineEntry.grid(column=1,row=1)
    cycleLabel = Label(frame,text = "Number of Cycles",width = 20)
    cycleEntry = Entry(frame)
    cycleLabel.grid(column=0,row=2)
    cycleEntry.grid(column=1,row=2)
    fileLabel = Label(frame,text = "Access Sequence",width = 20)
    fileButton = Button(frame,text = "Select file",command=lambda: fileclick())
    fileLabel.grid(column=0,row=3)
    fileButton.grid(column=1,row=3)
    startButton = Button(root, anchor="se",text = "Begin Simulation",command= lambda: simulation(lineEntry,sizeEntry,cycleEntry,frame,startButton,root))
    startButton.pack()
    root.mainloop()

startScreen()