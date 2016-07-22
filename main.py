import tkinter as tk     #just like how you import pandas as pd
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename    # import like this to have easier access to the methods
                                                                     # lets you type askopenfilename instead of tkinter.filedialog.askopenfilename
import getpass
import pandas as pd  # Renames imported library to "pd"


'''The point of a computer is ....
... To do repetitive tasks for you. If you find yourself copy and pasteing
code 13 times, you are doing the computer's job!'''


"""
added initialise method for creating option parameter dictionary from lists
    used dict(zip()) to iterate trough both lists and create dictionary



added createwidgets method for creating buttons in their own frame
    moved Button parameters inside ttk.Button
    -- ttk.Button(self, text, command)

    ---used ttk import for visually better buttons, can just be tk if you want

"""


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.user = getpass.getuser()
        self.csv_file = None
        self.txt_file = None
        self.convert_file = None
        self.initialise()       # initialises options for opening/saving file
        self.createwidgets()    # creates buttons in their own frame
        
    def initialise(self):       # creates dict for options
        #general option parameters
        OPTION = [
            'defaultextension',
            'filetypes',
            'initialdir',
            'parent',
            'title',
            'multiple'
            ]
        #open file parameters
        OPTION_OPEN = [
            '.csv',
            {('Comma Separated Value', '.csv'), },
            'C:/Users/{}/desktop/'.format(self.user),
            root,
            'Select CSV file',
            'False'
            ]
        #save file parameters
        OPTION_SAVE = [
            '.txt',
            {('Text File', '.txt'), },
            'C:/Users/{}/desktop/'.format(self.user),
            root,
            'Select .txt File Save Location',
            None
            ]

        #creates dictionary from 2 lists
        self.file_opt_open = dict(zip(OPTION, OPTION_OPEN))
        self.file_opt_save = dict(zip(OPTION, OPTION_SAVE))


    def createwidgets(self):
        # bundled creating the widgets(buttons) into one function
        widgets = tk.Frame(self) #creates own frame for widgets
        # creating buttons
        self.quit = ttk.Button(widgets, text = "QUIT", command = root.destroy)
        self.quit.pack(side="bottom")
        self.select_csv_file = ttk.Button(widgets, text = "Select File", command = self.openfilename)
        self.select_csv_file.pack(side="top")
        self.save_txt_file = ttk.Button(widgets, text = "Output Location", command = self.savefilename)
        self.save_txt_file.pack(side="top")
        self.convert_file = ttk.Button(widgets, text = "Convert CSV File", command = self.conversion)
        self.convert_file.pack(side="top")
        # packs widget frame into window
        widgets.pack() 


    def openfilename(self): #changed name because was identical with askopenfilename method from tkinter.filedialog
        self.csv_file = askopenfilename(**self.file_opt_open)
        print(self.csv_file)  # print for debug
        print(type(self.csv_file))  # print for debug

    def savefilename(self): #changed name
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
