# version 0.1.5
import tkinter.filedialog
import getpass
import pandas as pd



class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.quit = tkinter.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.select_csv_file = tkinter.Button(self)
        self.pack()
        self.create_widgets()
        self.file_opt = options = {}
        self.user = getpass.getuser()
        self.csv_file = None
        options['defaultextension'] = '.csv'
        options['filetypes'] = [('Comma Separated Value', '.csv'), ]
        options['initialdir'] = 'C:/Users/%s/desktop/' % self.user
        options['parent'] = root
        options['title'] = 'Select CSV file'
        options['multiple'] = 'False'

    def create_widgets(self):
        self.select_csv_file["text"] = "Select File"
        self.select_csv_file["command"] = self.askopenfilename
        self.select_csv_file.pack(side="top")
        self.quit.pack(side="bottom")

    def askopenfilename(self):
        self.csv_file = tkinter.filedialog.askopenfilename(**self.file_opt)
        print(self.csv_file) # print for debug
        print(type(self.csv_file)) #print for debug

    def ssidlist(self):
        print(pd.read_csv(self.csv_file, skipinitialspace=False, usecols=["SSID"]) .drop_duplicates())
        print(self.csv_file)


root = tkinter.Tk()
root.wm_title("CSV to TXT Converter")
app = Application(master=root)
app.mainloop()
