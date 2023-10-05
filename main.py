from tkinter import *
import os.path


class menu():

  def __init__(self):
    ''' Main Window '''
    self.window = Tk()
    self.window.title("Youtube To MP3 Converter")
    self.window.geometry("600x150")
    self.window.resizable(False, False)
    winTitleTxt = Label(self.window, text="Youtube To MP3 Converter", anchor="center")
    winTitleTxt.grid(row=0, column=0)
    ''' Path Text and Entry '''
    self.pathTxt = Label(self.window, text="Save MP3 File to: ")
    self.pathTxt.grid(row=2, column=0, sticky="w")

    self.pathEntry = Entry(self.window, width=50,)
    self.pathEntry.grid(row=3, column=0, sticky="w")
    ''' Input Link Text and Entry'''
    self.inputLinkTxt = Label(self.window, text="Please enter a Youtube link")
    self.inputLinkTxt.grid(row=4, column=0, sticky="w")

    self.linkEntry = Entry(self.window, width=50)
    self.linkEntry.grid(row=5, column=0, sticky="w")
    ''' Browse Files Button '''
    self.browseFilesBtn = Button(self.window,
                                 text="Browse Files...",
                                 width=10,
                                 command=self.browseFiles)
    self.browseFilesBtn.grid(row=3, column=1, sticky="w")
    ''' Download button '''
    self.downloadBtn = Button(self.window,
                              text="Download",
                              width=10,
                              command=self.download)
    self.downloadBtn.grid(row=5, column=1, sticky="s")

    self.window.mainloop()

  def browseFiles(self):
    pass

  def download(self):
    pass


menu()