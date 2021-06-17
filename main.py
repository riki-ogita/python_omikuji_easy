
import tkinter
import random
def sampleFunction():
    x = ["大吉", "中吉", "小吉", "末吉", "凶", "大凶"]
    lbl.configure(text=random.choice(x))
    
ui = tkinter.Tk()
ui.title("おみくじ")
ui.geometry("200x100")

btn = tkinter.Button(text="おみくじを引く", command = sampleFunction)
lbl = tkinter.Label()

btn.pack()
lbl.pack()

tkinter.mainloop()
