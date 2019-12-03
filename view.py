import tkinter as tk
from tkinter import ttk



class genTool(tk.Toplevel):
    BUTTON_CAPTION =['Button2']
    number=''
    
    def __init__(self, parent,controller):
        super().__init__(parent)
        
        
        self.controller=controller
        self._make_entry()
        self._make_buttons()
        
  
    def _make_entry(self):
        self.value_var2=tk.StringVar()
        self.ent =tk.Entry(self, textvariable= self.value_var2)
        self.ent.grid(row=2,column=1)
    def _make_buttons(self):
        for caption in self.BUTTON_CAPTION:
            btn=tk.Button(
                self, text= caption, command =(
                lambda button= caption: self.controller.on_button_click(button)
                )
                )
            btn.grid(row=3,column=2)

class View(tk.Tk):
    PAD =10
    BUTTON_CAPTIONS =['Button1']
    # self is place holder for object name
    def __init__(self, controller):
        super().__init__()
        self.title("Application")
        self.controller = controller
        
        self._make_main_frame()
        self._make_entry()
        self._make_buttons()
        self.gen_tool=''
        
        
    
    def main(self):
        
        self.mainloop()
    
    def _make_entry(self):
        self.value_var1=tk.StringVar()
        
        
        self.ent =tk.Entry(self, textvariable= self.value_var1)
        self.ent.pack()
    def _make_buttons(self):
        
        for caption in self.BUTTON_CAPTIONS:
            btn=tk.Button(
                self, text= caption, command =(
                lambda button= caption: self.controller.on_button_click(button)
                )
                )
            btn.pack()
        
        
    def open_window(self):
        self.about=genTool(self,self.controller)
        
        self.about.grab_set()
    def _make_main_frame(self):
        menu = tk.Menu(self)
        menu = tk.Menu(self)
        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="otherwin",command=self.open_window)
        menu.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu)
        
