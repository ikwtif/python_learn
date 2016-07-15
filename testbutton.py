# version 0.1.3
import tkinter.filedialog


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.quit = tkinter.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.select_csv_file = tkinter.Button(self)
        self.pack()
        self.create_widgets()
        self.file_opt = options = {}
        options['defaultextension'] = '.csv'
        options['filetypes'] = [('all files', '.*'), ('comma separated value', '.csv')]
        # options['initialdir'] = 'C:\\'
        # options['initialfile'] = 'myfile.txt'
        # options['parent'] = root
        options['title'] = 'This is a title'

    def create_widgets(self):
        self.select_csv_file["text"] = "Select File"
        self.select_csv_file["command"] = self.askopenfilename
        self.select_csv_file.pack(side="top")
        self.quit.pack(side="bottom")

    def askopenfilename(self):
        self.csv_file = tkinter.filedialog.askopenfilename(self.file_opt)
        print(self.csv_file)
        return self.csv_file


root = tkinter.Tk()
root.wm_title("CSV to TXT Converter")
app = Application(master=root)
app.mainloop()
