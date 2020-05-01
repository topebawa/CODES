try:
    import tkinter
except ImportError: #mpython 2
    import Tkinter as tkinter
print(tkinter.TkVersion)
print(tkinter.TclVersion)

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry("550x380")

label = tkinter.Label(mainWindow, text = "My name is Tope")
label.pack(side='top')

canvas = tkinter.Canvas(mainWindow, relief='solid', borderwidth=110)

button1 = tkinter.Button(mainWindow, text ='YES')
##button1.pack(side='left')

mainWindow.mainloop()
