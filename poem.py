import Tkinter
import tkMessageBox
import json
import winsound

#instantiates the GUI
top = Tkinter.Tk()

#load json file
Poem = json.load(open('test.json'))

#Defined Callback function for buttons
def functionCall(freq):
   winsound.Beep(int(float(freq)), 1000)  #Comment this out on nonwindows machines

#Instantiates 2d array of buttons, could still be optimized
buttons = [[None for _ in range(0, 10)] for _ in range(0, 10)]
labels = [None for _ in range(len(Poem['Tunings']))]
#Populates the empty array with buttons which parse their information from the Json file
for Tunings in Poem['Tunings']: #for each tuning
    i = 0; #iterator
    textVar = Tkinter.StringVar()
    labels[i] = Tkinter.Label(top, textvariable=textVar, height=2, width=40)
    textVar = str(i)
    labels[i].pack()
    for j in range(0, len(Poem[Tunings])):#for each string in each tuning
        buttons[i][j] = Tkinter.Button(top, text = "String: " + Poem[Tunings][i]['String'] + " " + "Tuning: " + Poem[Tunings][i]['Tuning'] + " " + "Freq: " + Poem[Tunings][i]['Freq'], command = lambda freq = Poem[Tunings][i]['Freq']: functionCall(freq),height=2, width=40) #populates the buttons with information
        buttons[i][j].pack() #loads the buttons into the GUI

        print "String:", Poem[Tunings][i]['String'], "Tuning:", Poem[Tunings][i]['Tuning'], "Freq:", Poem[Tunings][i]['Freq']
        i += 1
#Begins the GUI loop
top.mainloop()