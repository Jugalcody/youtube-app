#!/usr/bin/python3
import os
if(os.path.isfile('youtube')):
          os.system("chmod +x youtube")
          os.system("./youtube")
elif(os.path.isfile('main.py')):
          os.system('python3 main.py')
          
