#!/usr/bin/python3
# coding: utf-8
import time
import requests
import RPi.GPIO as GPIO
import subprocess

server='http://192.168.1.4'
def playsound(path):
    subprocess.Popen(['mpg123', '-q', path]).wait()


def get_gpio():
    status=''
    for i in range(4,8):
        status+=str(int(not GPIO.input(Relay[i])))
    return status

def send_alarm(name,status):
    data={'key':'19979476','name':name,'status':status,'expand':''}
    res=requests.post(server+'/alarm',timeout=3,data=data)
    if res.text=='Success':
        print('alarm send')
def send_affirm(name,affirm):
    data={'key':'19979476','name':name,'affirm':affirm}
    res=requests.post(server+'/affirm',timeout=3,data=data)
    if res.text=='Success':
        print('affirm send')
    
def receive_command(name):
    data={'key':'19979476','name':name}
    res=requests.post(server+'/command',timeout=3,data=data)
    command=res.text
    return eval(command)
def event_come():
    with open('event_come.txt','w')as f:
        f.write('1')
    

def execute_command(command):
    with open('local_command.txt','w')as f:
        f.write(command)
    for i in range(len(command)):
        GPIO.output(Relay[i],not int(command[i]))
        
            

def execute_text(name,text,time):
    new_text=[time,name,text]
    with open('text.txt','w')as f:
        f.write(str(new_text))
  
  


class local_machine():
    def __init__(self,key='19979476',name='',status={'command':'0000','alarm':'0000','text':'','voice':'0000','expand':''},affirm='0'):
        self.key=key
        self.name=name
        self.status=status
        self.affirm=affirm



    def check_status(self):
        status=get_gpio()
        if self.status['alarm']!=status:
            event_come()
            send_alarm(self.name,status)
            if int(status)>0:
                with open('local_alarm.txt','w')as f:
                    f.write('1')
                self.affirm='1'
            else:
                self.affirm='0'
                with open('local_alarm.txt','w')as f:
                    f.write('0')
            send_affirm(self.name,self.affirm)
            self.status['alarm']=status
        
    def get_command(self):
        command=receive_command(self.name)
        if self.status['command']!=command[self.name]['command']:
            event_come()
            execute_command(command[self.name]['command'])
            self.status['command']=command[self.name]['command']
        if self.status['text']!=command[self.name]['text']:
            event_come()
            execute_text(self.name,command[self.name]['text'],command['time'])
            self.status['text']=command[self.name]['text']

        

            
    def get_affirm(self):
        data={'key':'19979476','name':self.name,'affirm':'?'}
        res=requests.post(server+'/affirm',timeout=3,data=data)
        self.affirm=res.text
        
    def show_affirm(self):
        with open('affirm.txt','w')as f:
            f.write(self.affirm)
        

#initialize
Relay = [5, 6, 13, 16, 19, 20, 21, 26]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for i in range(0,8):
    GPIO.setup(Relay[i], GPIO.OUT)
for n in range(len(Relay)):
    GPIO.output(Relay[n],not 0)
            

        
bzy=local_machine(name='发射二营')
error=3
while True:
    try:
        bzy.check_status()
        time.sleep(2)
        if bzy.affirm=='1':
            bzy.get_affirm()
        bzy.show_affirm()   
        bzy.get_command()
        error=0
    except:
        error+=1
        time.sleep(2)
        if error>3:
            playsound('wire_error.mp3')
        
    
        

