import os;
import tkinter;
from tkinter import *;
from tkinter import filedialog;
from tkinter import messagebox

from tika import parser

import SoundLib.SoudConverter
from Forms.FileFormats import FileFormatExtension
import Forms.ConvertSettingApps

sys.path.append(r'/Forms')

class MenuFileEvent:
    def __init__(self,master,text):
        self.__master=master;

        self.__text=text;

        self.__Language = tkinter.StringVar(value="pl");

    def OpenRegularPdfText(self):

        fname = filedialog.askopenfilename()
        if fname is None:
            return;

        if FileFormatExtension.PDF in os.path.basename(fname):
           pdfText = parser.from_file(str(fname))

           self.__SetTextValue(pdfText['content'])

    def __SetTextValue(self,textValue):

        self.__text.delete(1.0, END)

        self.__text.insert(END,textValue )

    def OpenRegularTxtFile(self):
        fname = filedialog.askopenfilename();

        if fname is None:
            return;

        if FileFormatExtension.TXT in os.path.basename(fname):
            file=open(fname,"r",encoding="utf-8");
            resultText=file.read();
            file.close();
            self.__SetTextValue( resultText)
    def SaveMp3File(self):

        text = self.__text.get(1.0, END);

        if (str(text).strip() == ""):
            messagebox.showinfo('Warning', "No TEXT to convert");
            return
        fname = filedialog.asksaveasfilename(title = "Select file",
                                             filetypes = (("mp3 files","*.mp3"),("all files","*.*")));

        if fname is None:
            return;
        else:
            if "mp3" not in fname:
                fname=(fname.rstrip('.')+".mp3")
            if os.path.exists(fname)==True:
                os.remove(fname);

        sound=SoundLib.SoudConverter.SoundConverter(lang=self.__Language.get(),text=text);
        sound.SaveMp3(fname)
        messagebox.showinfo('Info', "End convert to mp3");

    @property
    def Language(self):
        return self.__Language;

    @Language.setter
    def Language(self, value):
        self.__Language=value;
    def ConvertToMp3WithSettings(self):
        """subRoot=Tk();
        status_bar_frame = Frame(subRoot)
        status_bar_frame.grid(row=3, column=0, columnspan=2)

        status_bar = Label(status_bar_frame, text="status bar")
        status_bar.pack()
        subRoot.mainloop();
        """
        print("Hello")