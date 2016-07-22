import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import getpass
import pandas as pd  # Renames imported library to "pd"


'''The point of a computer is ....
... To do repetitive tasks for you. If you find yourself copy and pasteing
code 13 times, you are doing the computer's job!'''


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.user = getpass.getuser()
        self.csv_file = None
        self.txt_file = None
        self.convert_file = None
        self.initialise()
        self.createwidgets()
        
    def initialise(self):
        OPTION = [
            'defaultextension',
            'filetypes',
            'initialdir',
            'parent',
            'title',
            'multiple'
            ]

        OPTION_OPEN = [
            '.csv',
            {('Comma Separated Value', '.csv'), },
            'C:/Users/{}/desktop/'.format(self.user),
            root,
            'Select CSV file',
            'False'
            ]

        OPTION_SAVE = [
            '.txt',
            {('Text File', '.txt'), },
            'C:/Users/{}/desktop/'.format(self.user),
            root,
            'Select .txt File Save Location',
            None
            ]
        
        self.file_opt_open = dict(zip(OPTION, OPTION_OPEN))
        self.file_opt_save = dict(zip(OPTION, OPTION_SAVE))


    def createwidgets(self):
        widgets = tk.Frame(self)
        self.quit = ttk.Button(widgets, text = "QUIT", command = root.destroy)
        self.quit.pack(side="bottom")
        self.select_csv_file = ttk.Button(widgets, text = "Select File", command = self.askopenfilename)
        self.select_csv_file.pack(side="top")
        self.save_txt_file = ttk.Button(widgets, text = "Output Location", command = self.asksavefilename)
        self.save_txt_file.pack(side="top")
        self.convert_file = ttk.Button(widgets, text = "Convert CSV File", command = self.conversion)
        self.convert_file.pack(side="top")
        widgets.pack()


    def askopenfilename(self):
        self.csv_file = askopenfilename(**self.file_opt_open)
        print(self.csv_file)  # print for debug
        print(type(self.csv_file))  # print for debug

    def asksavefilename(self):
        self.txt_file = asksaveasfilename(**self.file_opt_save)
        print(self.txt_file)  # print for debug
        print(type(self.txt_file))  # print for debug

    def conversion(self):
        pd.read_csv(self.csv_file, skipinitialspace=False, usecols=["SSID"], encoding='utf_8_sig').drop_duplicates().to_csv(path_or_buf=self.txt_file)


if __name__ == "__main__":        
    root = tk.Tk()
    root.wm_title("CSV to TXT Converter")
    window = Application(root)
    window.pack()
    root.mainloop()
