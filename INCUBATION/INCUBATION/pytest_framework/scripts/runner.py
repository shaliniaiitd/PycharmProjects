 #! /usr/bin/env python
import subprocess
import os

#if __name__ == '__main__':

   # For WINDOWS
   # cmd1 = f'DEL ..\\reports\*.json'
   # cmd2 = f'DEL ..\\reports\*.png'

    #FOR MAC
    #cmd1 = f'rm -r ..//reports/*.json'
    #cmd2 = f'rm -r ..//reports/*.png'

cmd3 = f'pytest --alluredir=../reports ../tests/'
cm4  = f'allure '

#d1 = subprocess.run(cmd1, shell=True, check=True)
#d2 = subprocess.run(cmd2, shell=True, check=True)
t = subprocess.run(cmd3, shell=True, check=False)
#r = subprocess.run(cmd4, shell =True, check=True)