import tkinter as tk
from tkinter import filedialog
import os.path
from pytube import YouTube


class menu():

  def __init__(self):
    ''' Main Window '''
    self.window = tk.Tk()
    self.window.title("Youtube To MP3 Converter")
    self.window.geometry("600x150")
    self.window.resizable(False, False)
    winTitleTxt = tk.Label(self.window,
                           text="Youtube To MP3 Converter",
                           anchor="center")
    winTitleTxt.grid(row=0, column=0)
    ''' Path Text and Entry '''
    self.pathTxt = tk.Label(self.window, text="Save MP3 File to: ")
    self.pathTxt.grid(row=2, column=0, sticky="w")

    self.pathEntry = tk.Entry(
        self.window,
        width=50,
    )
    self.pathEntry.grid(row=3, column=0, sticky="w")
    ''' Input Link Text and Entry'''
    self.inputLinkTxt = tk.Label(self.window,
                                 text="Please enter a Youtube link")
    self.inputLinkTxt.grid(row=4, column=0, sticky="w")

    self.linkEntry = tk.Entry(self.window, width=50)
    self.linkEntry.grid(row=5, column=0, sticky="w")
    ''' Browse Files Button '''
    self.browseFilesBtn = tk.Button(self.window,
                                    text="Browse Files...",
                                    width=10,
                                    command=self.browseFiles)
    self.browseFilesBtn.grid(row=3, column=1, sticky="w")
    self.directory = ''
    ''' Download button '''
    self.downloadBtn = tk.Button(self.window,
                                 text="Download",
                                 width=10,
                                 command=self.download)
    self.downloadBtn.grid(row=5, column=1, sticky="s")

    self.window.mainloop()

  def browseFiles(self):
    directory = filedialog.askdirectory()
    if directory:
      self.pathEntry.delete(0, tk.END)
      self.pathEntry.insert(0, directory)

  def download(self):
    if self.pathEntry:

      videoLink = YouTube(self.linkEntry.get())

      video = videoLink.streams.filter(only_audio=True).first()
      video.download(output_path=self.directory)


menu()