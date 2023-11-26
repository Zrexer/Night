#!/usr/bin/env python3
"""
[+] Night [+]

_< Spammer >_

DEV#Host1let => R3D\|/R00m


License :

Copyright (c) 2023 R3D\|/R00m Host1let: Night

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import pyautogui 
import time
import pystyle

writer = pystyle.Write.Print
colors = pystyle.Colors
underline = '\033[4m'
white = '\033[00m'

banner = """    _  _ _ ____ _  _ ___ 
    |\ | | | __ |__|  |  
    | \| | |__] |  |  |  

            {}
""".format('dev#Host1let')

class Box:
    
    def __init__(self, msg : str = None) -> None:
        self.msg = str(msg)
    
    @property
    def infoBox(self):
        writer('[{}] [{}] {}'.format(time.strftime("%H:%M:%S"), 'INFO', self.msg), colors.green_to_blue, 0)
        print()
    
    @property
    def errorBox(self):
        writer('[{}] [{}] {}'.format(time.strftime("%H:%M:%S"), 'ERROR', self.msg), colors.red_to_purple, 0)
        print()

def timer():
    lis = [0, 1 ,2 ,3 ,4 ,5]
    print()
    for p in lis:
        print(f'\rAttack starts in: {p}/5', end="")
        time.sleep(1)
    
    print()

def send(msg, for_):
    for _ in range(for_):
        pyautogui.typewrite(msg)
        pyautogui.press('enter')
        
def usage(numDict):
    dictX = {
        'commands' : [
            {
                'co' : 'help','info' : "show this message",
                'usage' : 'type " help "'
            },
            {
                'co' : 'cut',
                'info' : 'start The Attack',
                'usage' : {
                    'arg1' : 'text -> --open #<Filename or Path to send> -> text #<Text to send>'
                }
            }
        ]
    }
    
    return dictX['commands'][numDict]


class NightActivity:

    def ACT():
        writer(banner, colors.red_to_green, 0)

        while 1:
            
            user = str(input(f'\n{white}{underline}Night{white} > '))
            text = user.split()
            
            if 'help' in text or '?' in text:
                print()
                numDicts = [0, 1]
                
                for n in numDicts:
                    command = usage(n).get('co')
                    info = usage(n).get('info')
                    usagex = usage(n).get('usage')

                    Box(f'Command: {command}').infoBox
                    Box(f'Info: {info}').infoBox
                    Box(f'Usage: {usagex}').infoBox
                    print()
            
            if 'cut' in text:
                if 'text' in text:
                    if '--open' in text:
                        try:
                            fileToOpen = text[text.index('--open')+1]
                            file = open(fileToOpen, 'r').read()
                            print()
                            many = int(input('    How Many Type? > '))
                            timer()
                            send(file, many)
                            Box('Finish: {}\n'.format(many)).infoBox
                            print()
                        
                        except Exception as EO:
                            Box(EO).errorBox
                            pass
                        
                    else:
                        try:
                            textToSend = text[text.index('text')+1]
                            print()
                            manyx =  int(input('    How Many Type? > '))
                            timer()
                            send(textToSend, manyx)
                            Box('Finish: {}'.format(manyx)).infoBox
                            print()
                            
                        except Exception as ET:
                            Box(ET).errorBox
                            pass
                        
                else:
                    print()
                    Box('Faild To Use: Please Set Text by " text " argument').errorBox
                    # Help FUNC is Here -> just for text argument
                    Box(usage(-1)['usage']['arg1']).infoBox
                    
            if 'exit' in text:
                Box('Bye Bye').infoBox
                exit()

                            
                        
                        

NightActivity.ACT()