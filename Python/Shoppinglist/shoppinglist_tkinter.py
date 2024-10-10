from item_db_context import ItemDBContext as idc
import tkinter as tk

class ShoppinglistTKinter:
    def __init__(self):
        self.item_db = idc()
        
    def add(self):
        pass
    
    def show(self):
        pass
    
    def update(self):
        pass
    
    def delete(self):
        pass
    
    def start(self):
        self.build()
        
    def build(self):
        root = tk.Tk()

        #tk.Label(root, text="Hallo Welt!!!").grid(row=0, column=0)
        
        tk.Button(root, text="Click Me!", padx=100, pady=200, command=self.add, fg="blue", bg="#000000").pack()
        
        root.mainloop()