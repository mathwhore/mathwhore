import tkinter as tk
import math
calculation = ""
def Add_to_calculation(symbol):
    global calculation
    if 'π' in str(symbol): 
     calculation+=str(math.pi)
    else: 
     calculation+=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)
def Evaluate_calculation():
    global calculation
    try:
        if "ln" in calculation:
            calculation= math.log(float(calculation[3:len(calculation)-1]))
        elif "e^" in calculation:
            calculation=math.exp(int(calculation[2:]))  
        elif '√' in calculation:
            calculation=math.sqrt(int(calculation[1:])) 
        elif "^" in calculation:
            calculation=math.pow(float(calculation[:1]),float(calculation[2:len(calculation)]))        
        elif "sin" in calculation or "cos" in calculation or "tan" in calculation:
            calculation = eval(f"math.{calculation}")
        else:
            calculation=eval(calculation)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    text_result.delete(1.0, "end")
    calculation = ""

root = tk.Tk()
root.geometry("290x360")
root.title("Haider's calculator")
img=root.iconbitmap("Calculator_30001.ico")
root.config(bg="#708090")
text_result=tk.Text(root,height=2,width=16,font=("Arial",24),bg='#79CDCD')
text_result.grid(columnspan=5)
col_row=[[6,2],[5,1],[5,2],[5,3],[4,1],[4,2],[4,3],[3,1],[3,2],[3,3]]
for i in range(10):
 btn=tk.Button(root,text=i,bg="#528B8B",command=lambda pi=i:Add_to_calculation(pi),width=5,font=("Arial",14))
 btn.grid(row=col_row[i][0],column=col_row[i][1])
symbols=["+","-","*","/","ln(",'√','^',"π","(",")","e^","cos(","sin(","tan("] 
cl_rw=[[2,4],[3,4],[4,4],[5,4],[7,1],[7,2],[7,3],[7,4],[6,3],[6,4],[6,1],[2,1],[2,2],[2,3]]
for i in range(len(symbols)):
    btns=tk.Button(root,text=symbols[i],bg="#528B8B",command=lambda i=i:Add_to_calculation(symbols[i]),width=5,font=("Arial",14))
    btns.grid(row=cl_rw[i][0],column=cl_rw[i][1])
btnclear=tk.Button(root,text="c",bg="#79CDCD",command=clear_field,width=11,font=("Arial",14))
btnclear.grid(row=8,column=1,columnspan=2)
btnequal=tk.Button(root,text="=",bg="#79CDCD",command=Evaluate_calculation,width=11,font=("Arial",14))
btnequal.grid(row=8,column=3,columnspan=2)
root.mainloop()
