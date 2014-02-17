import Tkinter as tk
import enchant
from nltk.corpus import wordnet

class Dictionary:
    def __init__(self,master):
        frame=tk.Frame(master,bg="white",width=400,height=300)
        frame.pack()

  #Menu
        """ self.menu=tk.Menu(frame)
        self.aboutmenu=tk.Menu(self.menu)
        self.menu.add_cascade(label="Help",menu=self.aboutmenu)
        self.aboutmenu.add_cascade(label="About") """

  # Word entry Frame
        self.search_frame=tk.Frame(frame,width=400,height=30,bd=1,relief="sunken")
        self.search_frame.pack()

        self.search_label=tk.Label(self.search_frame,text="Word")
        self.search_label.grid(row=0,column=0,sticky="W")

        self.search_string=tk.StringVar()

        self.entry_text=tk.Entry(self.search_frame,bg="white",width=20,textvariable=self.search_string)
        self.entry_text.grid(row=0,column=1,sticky="W")


        self.reset_button=tk.Button(self.search_frame,text="Reset",command=self.reset_text)
        self.reset_button.grid(row=0,column=3,sticky="E")
        
        self.entry_text.bind('<Return>',self.search_text)
   # Meaning Frame

        self.return_frame=tk.Frame(frame,width=400,height=270,bg="white")
        self.return_frame.pack()

        self.text_area=tk.Text(self.return_frame,borderwidth=2,state='disabled',bg="white",relief="sunken")
        self.text_area.grid(row=0,column=0)

    def search_text(self,event):
        t=self.entry_text.get()
        a=enchant.Dict('en_US')
        self.text_area.config(state='normal')
        if a.check(t):
            self.text_area.insert('end','The Spelling you have entered is correct')
            self.text_area.config(state='disabled')
        else:
            self.text_area.insert('end','The Spelling you have entered is incorrect,Maybe you\'re looking for:')
            self.text_area.insert('end','\n')
            self.text_area.insert('end','Word')
            self.text_area.insert('end','\t')
            self.text_area.insert('end','\t')
            self.text_area.insert('end','\t')
            self.text_area.insert('end','Meaning')
            self.text_area.insert('end','\n')
            l=a.suggest(t)
            for i in l:
                self.text_area.config(state='normal')
                meaning=wordnet.synsets(i)[0]
                self.text_area.insert('end','\n')
                self.text_area.insert('end',i)
                self.text_area.insert('end','\t')
                self.text_area.insert('end','\t')
                self.text_area.insert('end','\t')
                self.text_area.insert('end',meaning.definition)
                self.text_area.config(state='disabled')

    def reset_text(self):
        self.text_area.config(state='normal')
        self.text_area.delete(1.0,"end")
        self.entry_text.delete(0,"end")
    

root=tk.Tk()
app=Dictionary(root)
root.title('Quick Spell Checker')
root.mainloop()

