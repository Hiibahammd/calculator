import tkinter as tk

calculation = ""
#contans our calculated value

def add_to_calculation(symbol):
    global calculation #so we can use it anywhere or change it in the funtion permanently
    calculation += str(symbol)  #add the symbol e.g 1 to the calc
    text_result.delete(1.0, "end") # we delete the operation like 1+2 from the firld to get the result
    text_result.insert(1.0, calculation) # start,string that we insert

#e.g we have 4+27*/3 we use this funtion to evaluate this
#uses/evaluates our calculation with nessasry tkinter
def evaluate_calculation():
    global calculation
    try:
        calculation= str(eval(calculation)) #this also evals code so dont do this in real apps
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

    except:
        clear_field()
        text_result.insert(1.0, "Error")

    

#C in Calculator
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


#GUI
root = tk.Tk()
root.title("Calculator")
root.geometry("340x380")
root.configure(bg="#FFF0F5") #background color


text_result = tk.Text(root, height= 2, width=16, font=("Consolas", 24), bg="#ffffff", fg="#333333", bd=0, highlightthickness=0)
text_result.grid(columnspan=5)
#5 columns and text box streches to all 5
#because we are using a grid

btn_font= ("Consolas", 18)
btn_relief = "flat"
pad_options = {"padx": 5, "pady": 5}

btn_bg = "#ffb6c1"
btn_fg = "#333333"

btn1 = tk.Button(root, text="1", command= lambda: add_to_calculation(1), width=5, font=btn_font, bg=btn_bg, fg=btn_fg, relief=btn_relief)
btn1.grid(row=2,column=1, **pad_options)

btn2 = tk.Button(root, text="2", command= lambda: add_to_calculation(2), width=5, font=btn_font, bg=btn_bg, fg=btn_fg, relief=btn_relief)
btn2.grid(row=2,column=2, **pad_options)

btn3 = tk.Button(root, text="3", command= lambda: add_to_calculation(3), width=5, font=btn_font, bg=btn_bg, fg=btn_fg, relief=btn_relief)
btn3.grid(row=2,column=3, **pad_options)

btn_p = tk.Button(root, text="+", command= lambda: add_to_calculation("+"), width=5, font=btn_font, bg=btn_bg, fg=btn_fg, relief=btn_relief)
btn_p.grid(row=2,column=4, **pad_options)

btn4 = tk.Button(root, text="4", command= lambda: add_to_calculation(4), width=5, font=btn_font, bg=btn_bg, fg=btn_fg, relief=btn_relief)
btn4.grid(row=3,column=1, **pad_options)

btn5 = tk.Button(root, text="5", command= lambda: add_to_calculation(5), width=5, font=btn_font, bg=btn_bg, fg=btn_fg, relief=btn_relief)
btn5.grid(row=3,column=2, **pad_options)

btn6 = tk.Button(root, text="6", command= lambda: add_to_calculation(6), width=5, font=btn_font, bg=btn_bg, fg=btn_fg, relief=btn_relief)
btn6.grid(row=3,column=3, **pad_options)

btn_mi = tk.Button(root, text="-", command= lambda: add_to_calculation("-"), width=5, font=btn_font, bg=btn_bg, fg=btn_fg, relief=btn_relief)
btn_mi.grid(row=3,column=4, **pad_options)

btn7 = tk.Button(root, text="7", command= lambda: add_to_calculation(7), width=5, font=btn_font, bg=btn_bg, fg=btn_fg, relief=btn_relief)
btn7.grid(row=4,column=1, **pad_options)

btn8 = tk.Button(root, text="8", command= lambda: add_to_calculation(8), width=5, font=btn_font, bg=btn_bg, fg=btn_fg, relief=btn_relief)
btn8.grid(row=4,column=2, **pad_options)

btn9 = tk.Button(root, text="9", command= lambda: add_to_calculation(9), width=5, font=btn_font, bg=btn_bg, fg=btn_fg, relief=btn_relief)
btn9.grid(row=4,column=3, **pad_options)

btn_m = tk.Button(root, text="×", command= lambda: add_to_calculation("*"), width=5, font=btn_font, bg=btn_bg, fg=btn_fg, relief=btn_relief)
btn_m.grid(row=4,column=4, **pad_options)

btn_r = tk.Button(root, text="(", command= lambda: add_to_calculation("("), width=5, font=btn_font, bg=btn_bg, fg=btn_fg, relief=btn_relief)
btn_r.grid(row=5,column=1, **pad_options)

btn_l = tk.Button(root, text=")", command= lambda: add_to_calculation(")"), width=5, font=btn_font, bg=btn_bg, fg=btn_fg, relief=btn_relief)
btn_l.grid(row=5,column=2, **pad_options)

btn0 = tk.Button(root, text="0", command= lambda: add_to_calculation(0), width=5, font=btn_font, bg=btn_bg, fg=btn_fg, relief=btn_relief)
btn0.grid(row=5,column=3, **pad_options)

btn_d = tk.Button(root, text="÷", command= lambda: add_to_calculation("/"), width=5, font=btn_font, bg=btn_bg, fg=btn_fg, relief=btn_relief)
btn_d.grid(row=5,column=4, **pad_options)

btn_c = tk.Button(root, text="C", command= clear_field, width=11, font=btn_font, bg="#ff7f7f", fg="#FFFFFF", relief=btn_relief)
btn_c.grid(row=6,column=1,columnspan=2, **pad_options)

btn_e = tk.Button(root, text="=", command= evaluate_calculation, width=11, font=btn_font, bg="#98fb98", fg="#FFFFFF", relief=btn_relief)
btn_e.grid(row=6,column=3, columnspan=2, **pad_options)
root.mainloop()