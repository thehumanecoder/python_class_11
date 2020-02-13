from tkinter import Tk,Menu,filedialog,END,messagebox
import tkinter.scrolledtext as ScrolledText


#Global File Name
filename = 'Untitled.txt'

#root for main window 
root = Tk(className = " Text Editor Noob")
root.iconbitmap(r'icon.ico')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
textArea = ScrolledText.ScrolledText(root,width=100, height =80)

#FUNCTIONS
#Open file function
def openFile():
    file =filedialog.askopenfile(parent=root,title="Please Select a file to open",filetypes=(("Text File","*.txt"),("All Files","*")))

    if file != None:
        contents = file.read()
        textArea.insert('1.0',contents)
        file.close()

#Save as File function
def fileSaveAs():
    file = filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    if file != None:
        #slice of the last character from get,as an extra return (enter) is added
        data = textArea.get('1.0',END+'-1c')
        file.write(data)
        file.close()

#Exit Function 
def quitroot():
    if messagebox.askyesno("Quit Text Editor Noob","Are you sure you want to quit?Because Biswas will mind if you quit X0X0"):
        root.destroy()

#About function
def About():
    label = messagebox.showinfo("About TextEditor Noob","An alternative notepad made with the help of Python and Developed By Biswas Sampad Satpathy")


#Menu options
menu = Menu(root)
root.config(menu=menu)
#top Menu
fileMenu = Menu(menu)
menu.add_cascade(label=" File",menu = fileMenu)
#sub menus
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open",command = openFile)
fileMenu.add_command(label="Save As",command = fileSaveAs)
fileMenu.add_command(label="Print")

fileMenu.add_separator()
fileMenu.add_command(label="Close",command = quitroot)
#top menu
helpMenu = Menu(menu)
menu.add_cascade(label="Help",menu=helpMenu)
helpMenu.add_command(label="Help")
#top menu
aboutMenu = Menu(menu)
menu.add_cascade(label="About",command=About)


textArea.pack()


#keep window open
root.mainloop()
