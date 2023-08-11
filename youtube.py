
import tkinter as tk
import webbrowser as wb,re,os

class Youtube:  #Youtube class will create a youtube front page 
    def __init__(self):
           
           self.root=tk.Tk()
           self.root.title("Youtube")
           self.root.resizable(False,False)
           self.root.geometry('1199x600+70+70')

           g=tk.Label(self.root,text="Youtube",font=("Helvatical bold",38))
           g.place(relx=0.4,rely=0.3)
           t=tk.Entry(self.root,font=("Default",14))
           t.place(relx=0.325,rely=0.45,width=400,height=42)
           
           
           def search():
               s=t.get()
               r=''
               for i in s:
                     if i!=' ':
                        r=r+i
                     else:
                        r=r+"+"   
                  
               wb.open(f'https://www.youtube.com/results?search_query={r}')

           b=tk.Button(self.root,text="search",command=search,cursor="hand2",width=9,height=1)
           b.place(relx=0.45,rely=0.56)
           
           n=f'{os.getcwd()}/images.png'
           try:
              photo=tk.PhotoImage(file=(r''+str(n)))
              self.root.iconphoto(False,photo)
              
           except:
                 pass
                
           self.root.mainloop()   



if __name__=="__main__":

       root=Youtube()
       

