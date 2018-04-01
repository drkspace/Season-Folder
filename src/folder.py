import sys
import Tkinter as tk
from os import mkdir

def create(l,n):
    for i in range(n):
        s = l+"\\Season {}".format(i+1)
        print("Making {}".format(s))
        mkdir(s)
    print("Done")

def tkInput():
    root = tk.Tk()
    root.geometry('500x500')
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky='w')


    l = tk.StringVar()
    tk.Label(frame, text = 'File path of the series folder').grid(row=0, column=0)
    tk.Entry(frame, textvariable = l).grid(row=1, column=0)

    n = tk.IntVar()
    tk.Label(frame, text = 'Number of seasons').grid(row=0, column=1)
    tk.Entry(frame, textvariable = n).grid(row=1, column=1)

    def run(l,n):
        if(l.get() == "" or n.get()<=0):
            return
        create(l.get(), n.get())

    tk.Button(frame, text='Create Folders', command = lambda: run(l,n)).grid(row=2,column=0)

    root.mainloop()
def cmdInput():
    args = sys.argv[1:]
    if len(args)!=2:
        print("Malformed input")
        sys.exit()
    create(args[0], int(args[1]))

def main():
    
    #Using tkinter
    if(True):
        tkInput()

    #Command line input
    else:
        cmdInput()

if __name__ == "__main__":
    main()
