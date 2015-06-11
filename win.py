from Tkinter import *

root = Tk()
root.title = 'Die Simulator'

button_frame = Frame(root)
roll_button = Button(button_frame, text='Roll Again')
quit_button = Button(button_frame, text='Quit')
roll_button.pack(side=LEFT)
quit_button.pack(side=LEFT)

die_frame = Frame(root)
d1 = Label(die_frame, text='0', bg='white', font=("Helvetica", 40))
d2 = Label(die_frame, text='0', bg='white', font=("Helvetica", 40))
d1.config(height=5, width=5)
d2.config(height=5, width=5)
d1.pack(side=LEFT)
d2.pack(side=LEFT)

die_frame.pack()
button_frame.pack()
root.mainloop()

if __name__ == '__main__':
    main()

