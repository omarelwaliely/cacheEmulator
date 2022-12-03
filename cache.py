from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
filename = ""
totalSize = 0
lineSize = 0
cycles = 0


def fileclick():
    global filename
    filename = filedialog.askopenfilename()


def simulation(line,size,cycle,frame,button):
    global filename
    global totalSize
    global lineSize
    global cycles

    if filename == "":
        messagebox.showerror(message="You did not select a file!",title = "File Error")
    elif line.get() == "" or cycle.get() == "" or size.get() == "":
        messagebox.showerror(message="You did not fill in all the labels!",title = "Empty Label Error")
    elif not (line.get().isnumeric() or cycle.get().isnumeric() or size.get().isnumeric()):
        messagebox.showerror(message="Please enter valid numbers!", title = "Number Error")
    elif int(cycle.get()) < 1 or int(cycle.get()) > 10:
        messagebox.showerror(message="Please enter a clock cycle between 1 and 10!", title = "Cycle Error")
    else:
        cycles = int(cycle.get())
        totalSize = int(size.get())
        lineSize = int(line.get())
        frame.destroy()
        button.destroy()
        simulatorScreen()


def simulatorScreen():
    return



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
    startButton = Button(root, anchor="se",text = "Begin Simulation",command= lambda: simulation(lineEntry,sizeEntry,cycleEntry,frame,startButton))
    startButton.pack()
    root.mainloop()

startScreen()