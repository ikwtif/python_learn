import tkinter.filedialog


def askopenfilename():
    filename = tkinter.filedialog.askopenfilename()
    print(filename)
    return filename


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.quit = tkinter.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.select_file = tkinter.Button(self)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.select_file["text"] = "Select File"
        self.select_file["command"] = askopenfilename
        self.select_file.pack(side="top")
        self.quit.pack(side="bottom")


root = tkinter.Tk()
root.wm_title("CSV to TXT Converter")
app = Application(master=root)
app.mainloop()
