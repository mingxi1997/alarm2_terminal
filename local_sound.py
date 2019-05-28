#!/usr/bin/python3
# coding: utf-8

import subprocess
import time
import os

def playsound(path):
    subprocess.Popen(['mpg123', '-q', path]).wait()
    
def get_command():
    with open('local_command.txt','r')as f:
            command=f.read()
    return command

def tts(text):
    text=text.replace('连长','连掌').replace('营长','营掌').replace('旅长','旅掌')
    os.system('ekho '+text)

class local_sound():
    def __init__(self,text='',text_type='BROAD',times=3):
        self.text=text
        self.times=times
        self.text_type=text_type
        self.warning=0

    def get_text(self):
        with open('text.txt','r')as f:
            text=eval(f.read())
        with open('local_command.txt','r')as f:
            command=f.read()
        if self.text!=text[2][5:] or self.text_type!=text[2][:5] or int(get_command())>0:
            self.text_type=text[2][:5]
            self.text=text[2][5:]
            self.read_text()
    def read_text(self):
        if self.text_type=='ALARM' and int(get_command())==0:
            for i in range(self.times):
                tts(self.text)
        if int(get_command())>0:
            while int(get_command())>0:
                try:
                    playsound(get_command()+'.mp3')
                except:
                    pass
                with open('text.txt','r')as f:
                    text=eval(f.read())
                text_type=text[2][:5]
                text=text[2][5:]
                if text_type=='ALARM':
                    tts(text)
        
    def check_local(self):
        with open('local_alarm.txt','r')as f:
            local_alarm=f.read()
           
        if local_alarm=='1':
            with open('affirm.txt','r')as f:
                affirm=f.read()
            if self.warning==0:
                playsound('local_alarm.mp3')
            
            if affirm=='1' and self.warning==1:
                playsound('local_alarm_no_affirm.mp3')
                playsound('local_alarm.mp3')
            elif affirm=='0' and self.warning==1:
                playsound('local_alarm_affirm.mp3')
                playsound('local_alarm.mp3')
            self.warning=1
        else:
            self.warning=0
        
        
    
        

                
bzy=local_sound()            
while True:
  try:
    bzy.get_text()
    bzy.check_local()
    time.sleep(3)
  except:
      pass
    
        
    
        


        
