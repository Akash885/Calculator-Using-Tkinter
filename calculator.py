import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("Calculator")

label=tk.Label(root, text="Enter first Number", pady=(10))
label.pack()

first_number_entry = tk.Entry(root)
first_number_entry.pack()

label2= tk.Label(root, text="Enter second Number")
label2.pack()

second_number_entry = tk.Entry(root)
second_number_entry.pack()

operations= tk.Label(root, text="Operations")
operations.pack()

def takeValueInputplus():
    first, second = takeValueInput()
    result = first + second
    result_label.config(text="Operations result is: " + 
                        str(result))

def takeValueInputminus():  
      first, second = takeValueInput()
      result = first - second
      result_label.config(text="Operations result is: " + 
                        str(result))

def takeValueInputmul():  
      first, second = takeValueInput()
      result = first * second
      result_label.config(text="Operations result is: " + 
                        str(result))
      
def takeValueInputdivide():
    first, second =takeValueInput()
    
    if second == 0:
        messagebox.showerror("Error", "cannot divide the value by 0.")
    else:
        result = first / second
        result =  round(result, 2)
        result_label.config(text="Operations result is: " + 
                            str(result))

def takeValueInput():
    first =first_number_entry.get()
    second =second_number_entry.get()
    
    
    try:
        first = int(first)
        second = int(second)
        
        return first,second
    except ValueError:
        if((len(first_number_entry.get()) == 0) or (len(second_number_entry.get()) ==0 )):
            messagebox.showerror("Error", "Please enter a value")  
        else:
            messagebox.showerror("Error", "Enter only integer value") 
        quit(0)
        
button = tk.Button(root, text="+", command=lambda: takeValueInputplus())
button.pack()      

button = tk.Button(root, text="-", command=lambda: takeValueInputminus())
button.pack()  

button = tk.Button(root, text="*", command=lambda: takeValueInputmul())
button.pack()  

button = tk.Button(root, text="/", command=lambda: takeValueInputdivide())
button.pack()   


result_label= tk.Label(root, text="Operations result is:")
result_label.pack()
             
root.mainloop()           
            
            
      
      
      
      
      
      
      
      
      
      