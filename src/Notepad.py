from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def notepad_textholder():
    # defining functions
    def new_file():
        global file
        notepad.title('Notepad')
        file = None
        Text_area.delete(1.0, END)


    def open_file():
        global file
        file = askopenfilename(defaultextension='.txt',
                               filetypes=[('All files', '*.*'),
                                          ('text files', '*.txt')])
        if file == '':
            file = None
        else:
            notepad.title(os.path.basename(('../docs/notepad.txt') + '- Notepad'))
            Text_area.delete(1.0, END)
            f = open('../docs/notepad.txt', 'r')
            Text_area.insert(1.0, f.read())
            f.close()


    def save_file():
        global file
        if file == None:
            file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                     filetypes=[("All Files", "*.*"),
                                                ("Text Documents", "*.txt")])
            if file == "":
                file = None

            else:
                # Save as a new file
                f = open('../docs/notepad.txt', "w")
                f.write(Text_area.get(1.0, END))
                f.close()

                notepad.title(os.path.basename(file) + " - Notepad")
                print("File Saved")
        else:
            # Save the file
            f = open(file, "w")
            f.write(Text_area.get(1.0, END))
            f.close()


    def exit():
        notepad.quit()


    def cut():
        Text_area.event_generate(('<<Cut>>'))


    def copy():
        Text_area.event_generate(('<<Copy>>'))


    def paste():
        Text_area.event_generate(('<<Paste>>'))


    def about():
        showinfo('Notepad', 'Notepad for Python Project')


    # creating an GUI

    notepad = Toplevel()
    notepad.title('Untitled Notepad')
    height = notepad.winfo_screenheight()
    width = notepad.winfo_screenwidth()
    notepad.geometry("900x800+{}+{}".format((width - 100) // 4, height - height))

    # creating text area

    Text_area = Text(notepad, font=('Arial', 17))
    file = None
    Text_area.pack(expand=True, fill=BOTH)

    # creating file menu item

    my_menu = Menu(notepad)
    notepad.config(menu=my_menu)
    Main_menu = Menu(my_menu)
    my_menu.add_cascade(label='File', menu=Main_menu)
    Main_menu.add_command(label='New', command=new_file)
    Main_menu.add_command(label='Open', command=open_file)
    Main_menu.add_command(label='Save', command=save_file)
    # adding an separator to make it look good a bit
    Main_menu.add_separator()
    Main_menu.add_command(label='Exit', command=exit)

    # creating edit menu item

    edit_menu = Menu(my_menu)
    my_menu.add_cascade(label='Edit', menu=edit_menu)
    edit_menu.add_command(label='Cut', command=cut)
    edit_menu.add_command(label='Copy', command=copy)
    edit_menu.add_command(label='Paste', command=paste)

    # help menu

    help_menu = Menu(my_menu)
    my_menu.add_cascade(label='Help', menu=help_menu)
    help_menu.add_command(label='About', command=about)




    f = open('../docs/notepad.txt', 'r')
    Text_area.insert(1.0, f.read())
    f.close()

    notepad.mainloop()
