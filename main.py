# version 0.1.5
import tkinter.filedialog
import getpass
import pandas as pd  # Renames imported library to "pd"


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.quit = tkinter.Button(self)
        self.select_csv_file = tkinter.Button(self)
        self.save_txt_file = tkinter.Button(self)
        self.convert_file = tkinter.Button(self)
        self.pack()
        self.selectfilewidget()
        self.savefilewidget()
        self.convertwidget()
        self.quitwidget()
        self.file_opt_open = options_open = {}
        self.file_opt_save = options_save = {}
        self.user = getpass.getuser()
        self.csv_file = None
        self.txt_file = None
        self.convert_file = None

        options_open['defaultextension'] = '.csv'
        options_open['filetypes'] = [('Comma Separated Value', '.csv'), ]
        options_open['initialdir'] = 'C:/Users/%s/desktop/' % self.user
        options_open['parent'] = root
        options_open['title'] = 'Select CSV file'
        options_open['multiple'] = 'False'

        options_save['defaultextension'] = '.txt'
        options_save['filetypes'] = [('Text File', '.txt'), ]
        options_save['initialdir'] = 'C:/Users/%s/desktop/' % self.user
        options_save['parent'] = root
        options_save['title'] = 'Select .txt File Save Location'
        # options_save['multiple'] = 'False'

    def selectfilewidget(self):
        self.select_csv_file["text"] = "Select File"
        self.select_csv_file["command"] = self.askopenfilename
        self.select_csv_file.pack(side="top")

    def savefilewidget(self):
        self.save_txt_file["text"] = "Output Location"
        self.save_txt_file["command"] = self.asksavefilename
        self.save_txt_file.pack(side="top")

    def convertwidget(self):
        self.convert_file["text"] = "Convert CSV File"
        self.convert_file["command"] = self.conversion
        self.convert_file.pack(side="top")

    def quitwidget(self):
        self.quit.pack(side="bottom")
        self.quit["text"] = "QUIT"
        self.quit["fg"] = "red"
        self.quit["command"] = root.destroy

    def askopenfilename(self):
        self.csv_file = tkinter.filedialog.askopenfilename(**self.file_opt_open)
        print(self.csv_file)  # print for debug
        print(type(self.csv_file))  # print for debug
        #  self.csvfilter()

    def asksavefilename(self):
        self.txt_file = tkinter.filedialog.asksaveasfilename(**self.file_opt_save)
        print(self.txt_file)  # print for debug
        print(type(self.txt_file))  # print for debug

    def conversion(self):
        print(pd.read_csv(self.csv_file, skipinitialspace=False, usecols=["SSID"])
              .drop_duplicates()
              .to_csv(path_or_buf=self.txt_file))


root = tkinter.Tk()
root.wm_title("CSV to TXT Converter")
app = Application(master=root)
app.mainloop()
