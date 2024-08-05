                        # PROJECT 4: TEXT TO SPEECH CONVERSION

from gtts import gTTS
import os
from tkinter import *

def textToSpeech():
    text=entry.get()
    language='en'
    output=gTTS(text=text,lang=language,slow=False)
    output.save('fileoutput.mp3')
    os.system('start fileoutput.mp3')

root=Tk()
root.title('Text to Speech Conversion')
root.geometry('400x300')

label=Label(root,text='Enter the text:',font=('Algerian',15))
label.grid(row=0,column=0)

entry=Entry(root)
entry.grid(row=0,column=1,ipadx=5,ipady=5)

button=Button(text='Convert',command=textToSpeech)
button.grid(row=1,column=1,ipadx=3,ipady=3)

root.mainloop()