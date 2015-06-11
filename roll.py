from Tkinter import *
import random

class App:
    
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.die_label = Label(frame, bg='white',font=('Helvetica', 50, 'bold'), text=str(random.choice([1,2,3,4,5,6])))
        self.die_label.grid(row=0, column=0)
        
        self.die_label2 = Label(frame, bg='white',font=('Helvetica', 50, 'bold'), text=str(random.choice([1,2,3,4,5,6])))
        self.die_label2.grid(row=0, column=1)

        self.roll_button = Button(frame, text='Roll', command=self.roll_die)
        self.roll_button.grid(row=1, column=0)

        self.quit_button = Button(frame, text='QUIT', command=frame.quit)
        self.quit_button.grid(row=1, column=1)


    def roll_die(self):
        value = random.choice([1,2,3,4,5,6])
        value2 = random.choice([1,2,3,4,5,6])
        self.die_label.config(text=value)
        self.die_label2.config(text=value2)

root = Tk()
app = App(root)
root.mainloop()

