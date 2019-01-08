import os;
import sys;
import tkinter
from tkinter import *;
from tkinter import filedialog;
from tkinter import scrolledtext;

from Forms import SoundLanguage
from Forms.MenuFileEvent import MenuFileEvent;

baseHeight = 600;
baseWidth = 800;

sys.path.append(r'/Forms')

class Apps:
    def __init__(self, master):
        self.frame = Frame(master, height=baseHeight, width=baseWidth);
        # information
        self.mainText = scrolledtext.ScrolledText(self.frame);
        self.mainText.pack(expand=True, fill='both');

        self.__menuEvent = MenuFileEvent(master, self.mainText);
        self.__buildMenu(master);

        self.frame.pack(fill=BOTH, expand=YES);

    def __buildMenu(self, master):
        menubar = Menu(master);
        filemenu = Menu(menubar)

        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Open Txt File", command=self.__menuEvent.OpenRegularTxtFile)
        filemenu.add_command(label="Open PDF File", command=self.__menuEvent.OpenRegularPdfText)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=master.quit)

        fileSoundMenu = Menu(master);

        fileLanguage = Menu(master);

        menubar.add_cascade(label="Sound", menu=fileSoundMenu);

        fileSoundMenu.add_cascade(label="Language", menu=fileLanguage);

        for fullName in SoundLanguage.LanguageOpction.Language.keys():
            fileLanguage.add_radiobutton(label=fullName,
                                         variable=self.__menuEvent.Language,
                                         value=SoundLanguage.LanguageOpction.Language[fullName]);

        fileSoundMenu.add_command(label="Convert to MP3", command=self.__menuEvent.SaveMp3File);

        fileSoundMenu.add_command(label="Convert to MP3 with settings",
                                  command=self.__menuEvent.ConvertToMp3WithSettings);
        master.config(menu=menubar)


