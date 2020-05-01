try:
    import tkinter
except ImportError: #python2
    import Tkinter as tkinter
    
print(tkinter.TkVersion)
print(tkinter.TclVersion)

mainWindow = tkinter.Tk()

mainWindow.title("Hello")
mainWindow.geometry("640x480")

mainWindow.mainloop
