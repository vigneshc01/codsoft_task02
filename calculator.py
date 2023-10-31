import tkinter as tk

root = tk.Tk()


root.title("Calculator")

#screen diemension in width x height
root.geometry("300x400")

#user to set the maximum screen size
# root.maxsize(300,400)

#minimum screeen size that a user can minimum size
root.minsize(200,200)


# label_variabel=Label(text='calculator ')
# label_variabel.pack()

# button for the number



#Grid box for the text input
result_text=tk.Text(root,height=2,width=17,font=('Arial',24))
result_text.grid(columnspan=5)


#function for mathematical functions 
#taking empty string to dynamically add value if new value is added for calculation
calculation=''

def add_value(symbol):
    global calculation
    calculation +=str(symbol)
    result_text.delete(1.0,'end')
    result_text.insert(1.0,calculation)


def evaluate_calculation():
    global calculation
    
    try:
        calculation=str(eval(calculation))
        
        result_text.delete(1.0,'end')
        result_text.insert(1.0,calculation)

    except:
        clear_field()
        
        result_text.insert(1.0,'ERROR')



def clear_field():
    global calculation

    calculation=''
    result_text.delete(1.0,'end')

def back_space():
    global calculation
    result_text.delete('end','end')



# inserting button to the calculator


but1=tk.Button(root,text='1',command=lambda:add_value(1),width=5,font=('arial',14))

but1.grid(row=2,column=1)

# but2

but2=tk.Button(root,text='2',command=lambda:add_value(2),width=5,font=('arial',14))
but2.grid(row=2,column=2)

# but3

but3=tk.Button(root,text='3',command=lambda:add_value(3),width=5,font=('arial',14))
but3.grid(row=2,column=3)

#but4

but4=tk.Button(root,text='4',command=lambda:add_value(4),width=5,font=('arial',14))
but4.grid(row=3,column=1)

but5=tk.Button(root,text='5',command=lambda:add_value(5),width=5,font=('arial',14))
but5.grid(row=3,column=2)

but6=tk.Button(root,text='6',command=lambda:add_value(6),width=5,font=('arial',14))
but6.grid(row=3,column=3)

but7=tk.Button(root,text='7',command=lambda:add_value(7),width=5,font=('arial',14))
but7.grid(row=4,column=1)

but8=tk.Button(root,text='8',command=lambda:add_value(8),width=5,font=('arial',14))
but8.grid(row=4,column=2)

but9=tk.Button(root,text='9',command=lambda:add_value(9),width=5,font=('arial',14))
but9.grid(row=4,column=3)

but0=tk.Button(root,text='0',command=lambda:add_value(0),width=5,font=('arial',14))
but0.grid(row=5,column=2)

but_plus=tk.Button(root,text='+',command=lambda:add_value('+'),width=5,font=('arial',14))
but_plus.grid(row=2,column=4)

but_sub=tk.Button(root,text='-',command=lambda:add_value('-'),width=5,font=('arial',14))
but_sub.grid(row=3,column=4)

but_div=tk.Button(root,text='%',command=lambda:add_value('%'),width=5,font=('arial',14))
but_div.grid(row=4,column=4)


but_mul=tk.Button(root,text='*',command=lambda:add_value('*'),width=5,font=('arial',14))
but_mul.grid(row=5,column=4)


# clear button

but_clear=tk.Button(root,text='CE',command=clear_field,width=5,font=('arial',14))
but_clear.grid(row=5,column=3)

#equal botton
but_equal=tk.Button(root,text='=',command=evaluate_calculation,width=5,font=('arial',14))
but_equal.grid(row=5,column=1)


#brackets

but_left_brackets=tk.Button(root,text='(',command=lambda:add_value('('),width=12,font=('arial',14))
but_left_brackets.grid(row=6,column=1,columnspan=2 )

#right_bracket
but_right_brackets=tk.Button(root,text=')',command=lambda:add_value(')'),width=12,font=('arial',14))
but_right_brackets.grid(row=6,column=3,columnspan=2 )



# but_backspace=tk.Button(root,text='<',command=back_space,width=5,font=('arial',14))
# but_backspace.grid(row=6,column=1)


root.mainloop()