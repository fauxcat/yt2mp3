import tkinter as tk
from tkinter import filedialog
import os.path
from pytube import YouTube


class menu:
    def __init__(self):
        """Main Window"""
        self.window = tk.Tk()
        self.window.title("Youtube To MP3 Converter by fauxcat")
        self.window.geometry("405x150")
        self.window.resizable(False, False)
        winTitleTxt = tk.Label(
            self.window,
            text="Youtube To MP3 Converter",
            anchor="center",
            font=("Sans-Serif", 16, "bold"),
        )
        winTitleTxt.grid(row=0, column=0, columnspan=2)

        """ Path Text and Entry """
        self.pathTxt = tk.Label(self.window, text="Save MP3 File to: ")
        self.pathTxt.grid(row=2, column=0, padx=5, sticky="w")

        self.pathEntry = tk.Entry(
            self.window,
            width=50,
        )
        self.pathEntry.grid(row=3, column=0, padx=5, sticky="w")

        """ Input Link Text and Entry"""
        self.inputLinkTxt = tk.Label(self.window, text="Please enter a Youtube link: ")
        self.inputLinkTxt.grid(row=4, column=0, padx=5, sticky="w")

        self.linkEntry = tk.Entry(self.window, width=50)
        self.linkEntry.grid(row=5, column=0, padx=5, sticky="w")

        """ Browse Files Button """
        self.browseFilesBtn = tk.Button(
            self.window, text="Browse Files", width=10, command=self.browseFiles
        )
        self.browseFilesBtn.grid(row=3, column=1, padx=5, sticky="w")
        self.directory = ""

        """ Download button """
        self.downloadBtn = tk.Button(
            self.window, text="Download", width=10, command=self.download
        )
        self.downloadBtn.grid(row=5, column=1, padx=5, sticky="s")

        """ Error Message"""
        self.errorTxt = tk.Label(self.window, text="", fg="red")
        self.errorTxt.grid(row=6, column=0, sticky="w")

        self.window.mainloop()

    """Browse Button Functionality"""

    def browseFiles(self):
        directory = filedialog.askdirectory()
        if directory:
            self.pathEntry.delete(0, tk.END)
            self.pathEntry.insert(0, directory)

    """Download Button Functionality"""

    def download(self):
        self.errorTxt.config(text="")
        if not os.path.exists(self.pathEntry.get()):
            print("invalid dir")
            self.errorTxt.config(text="Error: Invalid Directory", fg="red")
            return

        try:
            videoLink = YouTube(self.linkEntry.get())
            audio_stream = videoLink.streams.filter(only_audio=True).first()

            if audio_stream:
                outputfile = audio_stream.download(output_path=self.pathEntry.get())
                base, ext = os.path.splitext(outputfile)
                newFile = base + ".mp3"
                os.rename(outputfile, newFile)
                self.errorTxt.config(
                    text="Download completed successfully!", fg="green"
                )

        except Exception as e:
            print(f"Error: {str(e)}")
            self.errorTxt.config(
                text="Error: Failed to download. Please check the YouTube Link.",
                fg="red",
            )


menu()
