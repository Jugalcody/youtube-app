import os
# app fuction will convert the file to executable file
def app():
 s=input("have you installed python-pyinstaller(y/n)? ")
 if s=='y':
   try:
     import os
     try:
        os.system("sudo apt install python3-tk")
        import tkinter as tk
     except:
        print("Kindly install tkinter packet!!\n")
     os.system("pyinstaller -i images.ico -F youtube.py")
   except :
        print("an error occured, try agaian!!")
        os.system(f"pip install https://github.com/pyinstaller/pyinstaller/tarball/develop ")
        app()
   a=os.getcwd()
   b=a+'/dist/youtube'
   c=a+'\dist\youtube.exe'
   o=input("you are using terminal or cmd(t/c)? ")
   if o=='t':
     
       os.system(f"cp {b} {a}")
       os.system("rm -r build")
       os.system("rm -r dist")
       os.system("rm youtube.spec")
       os.system("rm -r __pycache__")
       os.system("rm -r .gitignore")
       os.system("rm main.py")
       os.system("rm youtube.py")
       os.system("rm images.ico")
       os.system("rm LICENSE")
       os.system("rm README.md")
       os.system("rm run2.py")
       os.system("chmod +x youtube")
       os.system("chmod +x run.py")
       f=open(".zshrc","a+")
       v=os.getcwd()
       f.write(f"export PATH=$PATH:{v}")
       os.system("source ~/.zshrc")
       f.close()
       os.system("sudo cp youtube /bin")
       os.system("sudo cp run.py /bin")
   elif o=='c':
               os.system(f"copy {c} {a}")
               print("Enter y ----")
               os.system("rmdir /s build")
               print("Enter y ----")
               os.system("rmdir /s dist")
               os.system("del youtube.spec")
               print("Enter y ----")
               os.system("rmdir /s __pycache__")
               os.system("del main.py")
               os.system("del youtube.py")
               os.system("del images.ico")
               os.system("del LICENSE")
               os.system("del README.md")
               os.system("del run.py")
             
 else:
               import os                   
               os.system(f"pip install https://github.com/pyinstaller/pyinstaller/tarball/develop ")
               app()
                        
                                     
if __name__=="__main__":
          import os
          app()
          if(os.path.isfile('run.py')):
                 os.system('python3 run.py')
          elif(os.path.isfile('run2.py')):
                 os.system('python run2.py')
                        
                 
          
                          

