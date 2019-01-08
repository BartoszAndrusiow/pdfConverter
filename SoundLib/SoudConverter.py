from gtts import gTTS;
import os;


class SoundConverter:
    def __init__(self,lang,text):
        self.__SoundConv = gTTS(lang=lang,text=text);

    def SaveMp3(self,path=""):
        if (path=="" or path==None):
            return;
        self.__SoundConv.save(path);