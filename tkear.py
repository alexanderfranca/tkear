from Tkinter import *
import tkMessageBox
from collections import defaultdict
import random
import os 

class EarTrainner(Frame):

    playedNote = None
    notes = defaultdict(dict)
    notes['A']['color'] = "blue"
    notes['B']['color'] = "red"
    notes['C']['color'] = "yellow"
    notes['D']['color'] = "brown"
    notes['E']['color'] = "white"
    notes['F']['color'] = "green"
    notes['G']['color'] = "red"

    notesAndFiles = {}
    notesAndFiles['A'] = "A.mp3"
    notesAndFiles['B'] = "B.mp3"
    notesAndFiles['C'] = "C.mp3"
    notesAndFiles['D'] = "D.mp3"
    notesAndFiles['E'] = "E.mp3"
    notesAndFiles['F'] = "F.mp3"
    notesAndFiles['G'] = "G.mp3"


    def generateNotesWidgets( self ):

        for note,value in self.notes.iteritems():

            self.note= Label(self)
            self.note['text'] = note
            self.note.pack( {'side': 'left' } )
            self.note.config(highlightthickness=20)
            self.note.config(width=10)
            self.note.config(height=10)
            self.note.config(bd=1)
            self.note.config(background=self.notes[note]['color'])


    def createWidgets(self):

        self.hi_there = Button(self)
        self.hi_there["text"] = "Play a note"
        self.hi_there["command"] = self.quit 
        self.hi_there.pack({"side": "left"})


    def playRandomNote( self, event ):

        noteToPlay = random.choice( self.notes.keys() )
        self.playedNote = noteToPlay

        self.execPlayer( self.notesAndFiles[ noteToPlay ] )


    def getFileToPlay( self, note=None ):

        note = str(note.replace("'",'')) 
        return self.notesAndFiles[ note ]


    def execPlayer( self, file_to_play=None ):

        print( "mplayer -quiet './" + file_to_play + "' 2> /dev/null" )
        os.system( "mplayer -quiet './" + file_to_play + "' 2> /dev/null" )


    def playNote(self, note=None):

        self.execPlayer( self.getFileToPlay( note ) ) 


    def playAskedNote( self, event ):

        self.playNote( repr(event.char ) )


    def checkAnswer( self, event ):

        note = repr( event.char )
        note = str( note.replace("'",'') )
        note = note.upper() 

        if note == self.playedNote:
            tkMessageBox.showinfo( 'Answer', "You got it!" )
        else:
            tkMessageBox.showinfo( 'Answer', 'Wrong note. Try again.' )


    def generateHotKeys( self ):
        self.master.bind('<A>', self.playAskedNote) 
        self.master.bind('<B>', self.playAskedNote) 
        self.master.bind('<C>', self.playAskedNote) 
        self.master.bind('<D>', self.playAskedNote) 
        self.master.bind('<E>', self.playAskedNote) 
        self.master.bind('<F>', self.playAskedNote) 
        self.master.bind('<space>', self.playRandomNote) 

        self.master.bind('<a>', self.checkAnswer ) 
        self.master.bind('<b>', self.checkAnswer ) 
        self.master.bind('<c>', self.checkAnswer ) 
        self.master.bind('<d>', self.checkAnswer ) 
        self.master.bind('<e>', self.checkAnswer ) 
        self.master.bind('<f>', self.checkAnswer ) 

        self.focus_set()


    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.createWidgets()
        self.generateNotesWidgets()
        self.generateHotKeys()
        self.pack()


root = Tk()
app = EarTrainner(master=root)
app.mainloop()
root.destroy()
