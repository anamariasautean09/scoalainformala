from tkinter import *

window = Tk()
window.geometry('478x328')
window.title('Calculator')
window.resizable(0, 0)
# window.resizable(False, False)

def click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def egalitate():
    try:
        global expression
        rezultat = str(eval(expression))
        input_text.set(rezultat)
        expression = ""
    except Exception:
        expression = ""
        input_text.set("Error! Please click C button")


expression = ''
input_text = StringVar()
input_frame = Frame(window, width=312, height=50)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 28, 'bold'), textvariable=input_text,
                    width=50, bg='#FF9966', bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack()

frame_buttons = Frame(window, width=500, height=304, bg='#FFCC99')
frame_buttons.pack()

button_clear = Button(frame_buttons, text='C', width=50, height=3,
                      bg='#FFCC99', cursor='hand2',
                      command=lambda: clear()).grid(row=0, column=0, columnspan=3)
impartit = Button(frame_buttons, text='/', width=15, height=3, bg='#FF6633', cursor='hand2',
                  command=lambda: click('/')).grid(row=0, column=3)
sapte = Button(frame_buttons, text='7', width=15, height=3, bg='#FF9966', cursor='hand2',
               command=lambda: click('7')).grid(row=1, column=0)
opt = Button(frame_buttons, text='8', width=15, height=3, bg='#FF9966', cursor='hand2',
             command=lambda: click('8')).grid(row=1, column=1)
noua = Button(frame_buttons, text='9', width=15, height=3, bg='#FF9966', cursor='hand2',
               command=lambda: click('9')).grid(row=1, column=2)
inmultire = Button(frame_buttons, text='*', width=15, height=3, bg='#FF6633', cursor='hand2',
               command=lambda: click('*')).grid(row=1, column=3)

patru = Button(frame_buttons, text='4', width=15, height=3, bg='#FF9966', cursor='hand2',
               command=lambda: click('4')).grid(row=2, column=0)
cinci = Button(frame_buttons, text='5', width=15, height=3, bg='#FF9966', cursor='hand2',
               command=lambda: click('5')).grid(row=2, column=1)
sase = Button(frame_buttons, text='6', width=15, height=3, bg='#FF9966', cursor='hand2',
               command=lambda: click('6')).grid(row=2, column=2)
minus = Button(frame_buttons, text='-', width=15, height=3, bg='#FF6633', cursor='hand2',
               command=lambda: click('-')).grid(row=2, column=3)

unu = Button(frame_buttons, text='1', width=15, height=3, bg='#FF9966', cursor='hand2',
               command=lambda: click('1')).grid(row=3, column=0)
doi = Button(frame_buttons, text='2', width=15, height=3, bg='#FF9966', cursor='hand2',
               command=lambda: click('2')).grid(row=3, column=1)
trei = Button(frame_buttons, text='3', width=15, height=3, bg='#FF9966', cursor='hand2',
               command=lambda: click('3')).grid(row=3, column=2)
plus = Button(frame_buttons, text='+', width=15, height=3, bg='#FF6633', cursor='hand2',
               command=lambda: click('+')).grid(row=3, column=3)

zero = Button(frame_buttons, text='0', width=15, height=3, bg='#FF9966', cursor='hand2',
               command=lambda: click('0')).grid(row=4, column=0)
zerozero = Button(frame_buttons, text='00', width=15, height=3, bg='#FF9966', cursor='hand2',
               command=lambda: click('00')).grid(row=4, column=1)
virgula = Button(frame_buttons, text='.', width=15, height=3, bg='#FF9966', cursor='hand2',
               command=lambda: click('.')).grid(row=4, column=2)
egal = Button(frame_buttons, text='=', width=15, height=3, bg='#FF6633', cursor='hand2',
               command=lambda: egalitate()).grid(row=4, column=3)

window.mainloop()
