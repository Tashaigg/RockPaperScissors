from tkinter import *
#from tkinter.ttk import *
from pathlib import Path
import random
import time

import sys, os
def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


w = 0
l = 0
t = 0

root = Tk()

#defs
def p_rock():
    global label_p
    global label_m
    global label_vs
    global image_p
    global label_res
    player = 'rock'
    label_p.destroy()
    label_m.destroy()
    label_vs.destroy()
    label_res.destroy()
    image_p = root.r
    label_p = Label(root, image=image_p)
    label_p_canvas = canvas1.create_window(30, 120, anchor="nw", window=label_p)
    label_vs = Label(root, image=root.vs)
    label_vs_canvas = lambda : canvas1.create_window(168, 120, anchor="nw", window=label_vs)
    canvas1.after(600,label_vs_canvas)
    calc(player)
def p_paper():
    global label_p
    global label_m
    global label_vs
    global image_p
    global label_res
    player = 'paper'
    label_p.destroy()
    label_m.destroy()
    label_vs.destroy()
    label_res.destroy()
    image_p = root.p
    label_p = Label(root, image=image_p)
    label_p_canvas = canvas1.create_window(30, 120, anchor="nw", window=label_p)
    label_vs = Label(root, image=root.vs)
    label_vs_canvas = lambda : canvas1.create_window(168, 120, anchor="nw", window=label_vs)
    canvas1.after(600,label_vs_canvas)
    calc(player)
def p_scissors():
    global label_p
    global label_m
    global label_vs
    global image_p
    global label_res
    player = 'scissors'
    label_p.destroy()
    label_m.destroy()
    label_vs.destroy()
    label_res.destroy()
    image_p = root.s
    label_p = Label(root, image=image_p)
    label_p_canvas = canvas1.create_window(30, 120, anchor="nw", window=label_p)
    label_vs = Label(root, image=root.vs)
    label_vs_canvas = lambda : canvas1.create_window(168, 120, anchor="nw", window=label_vs)
    canvas1.after(600,label_vs_canvas)
    calc(player)
def calc(p):
    global image_p
    global label_m
    m = random.choice(['scissors', 'rock', 'paper'])
    if p == m:
        label_m = Label(root, image=image_p)
        label_m_canvas = lambda : canvas1.create_window(275, 120, anchor="nw", window=label_m)
        canvas1.after(1300,label_m_canvas)
        e_tie()
    elif p == 'rock':
        if m == 'paper':
            label_m = Label(root, image=root.p)
            label_m_canvas = lambda : canvas1.create_window(275, 120, anchor="nw", window=label_m)
            canvas1.after(1300,label_m_canvas)
            e_lose()
        else:
            label_m = Label(root, image=root.s)
            label_m_canvas = lambda : canvas1.create_window(275, 120, anchor="nw", window=label_m)
            canvas1.after(1300,label_m_canvas)
            e_win()
    elif p == 'paper':
        if m == 'scissors':
            label_m = Label(root, image=root.s)
            label_m_canvas = lambda : canvas1.create_window(275, 120, anchor="nw", window=label_m)
            canvas1.after(1300,label_m_canvas)
            e_lose()
        else:
            label_m = Label(root, image=root.r)
            label_m_canvas = lambda : canvas1.create_window(275, 120, anchor="nw", window=label_m)
            canvas1.after(1300,label_m_canvas)
            e_win()
    elif p == 'scissors':
        if m == 'rock':
            label_m = Label(root, image=root.r)
            label_m_canvas = lambda : canvas1.create_window(275, 120, anchor="nw", window=label_m)
            canvas1.after(1300,label_m_canvas)
            e_lose()
        else:
            label_m = Label(root, image=root.p)
            label_m_canvas = lambda : canvas1.create_window(275, 120, anchor="nw", window=label_m)
            canvas1.after(1300,label_m_canvas)
            e_win()
def e_tie():
    global label_res
    global t
    t += 1
    label_res = Label(root, text="It's a Tie!!!", fg="white", bg='black', font=("Times", "28", "bold italic"))
    label_res_canvas = lambda : canvas1.create_window(100, 250, anchor="nw", window=label_res)
    canvas1.after(1900,label_res_canvas)
    label_score = Label(root, text=f"Win:{w}   Lose:{l}   Tie:{t}", fg="white", bg='black', font=("Times", "28", "bold italic"))
    label_score_canvas = lambda : canvas1.create_window(27, 30, anchor="nw", window=label_score)
    canvas1.after(2600,label_score_canvas)
def e_lose():
    global label_res
    global l
    l += 1
    label_res = Label(root, text="You Lose!!!", fg="white", bg='black', font=("Times", "28", "bold italic"))
    label_res_canvas = lambda : canvas1.create_window(100, 250, anchor="nw", window=label_res)
    canvas1.after(1900,label_res_canvas)
    label_score = Label(root, text=f"Win:{w}   Lose:{l}   Tie:{t}", fg="white", bg='black', font=("Times", "28", "bold italic"))
    label_score_canvas = lambda : canvas1.create_window(27, 30, anchor="nw", window=label_score)
    canvas1.after(2600,label_score_canvas)
def e_win():
    global label_res
    global w
    w += 1
    label_res = Label(root, text="You Win!!!", fg="white", bg='black', font=("Times", "28", "bold italic"))
    label_res_canvas = lambda : canvas1.create_window(100, 250, anchor="nw", window=label_res)
    canvas1.after(1900,label_res_canvas)
    label_score = Label(root, text=f"Win:{w}   Lose:{l}   Tie:{t}", fg="white", bg='black', font=("Times", "28", "bold italic"))
    label_score_canvas = lambda : canvas1.create_window(27, 30, anchor="nw", window=label_score)
    canvas1.after(2600,label_score_canvas)
def close_game(event=None):
    root.destroy()

root.title('ROCK PAPER SCISSORS')
root.geometry('402x531')
root.bind('<Escape>', close_game)

# Images
rock = PhotoImage(file=resource_path('rock.png'))
root.rock = rock
paper = PhotoImage(file=resource_path('paper.png'))
root.paper = paper
scissors = PhotoImage(file=resource_path('scissors.png'))
root.scissors = scissors
r = PhotoImage(file=resource_path('r.png'))
root.r = r
p = PhotoImage(file=resource_path('p.png'))
root.p = p
s = PhotoImage(file=resource_path('s.png'))
root.s = s
vs = PhotoImage(file=resource_path('vs.png'))
root.vs = vs

# Create Canvas
canvas1 = Canvas(root, width=402, height=531, bd=0, bg='black', highlightthickness=0)
canvas1.pack(fill="both", expand=True)

# Labels
label_p = Label(root)
label_p_canvas = canvas1.create_window(30, 120, anchor="nw", window=label_p, state='hidden')
label_m = Label(root)
label_m_canvas = canvas1.create_window(250, 120, anchor="nw", window=label_m, state='hidden')
label_vs = Label(root)
label_vs_canvas = canvas1.create_window(150, 120, anchor="nw", window=label_vs, state='hidden')
label_res = Label(root)
label_res_canvas = canvas1.create_window(150, 220, anchor="nw", window=label_res, state='hidden')


# Create buttons
btn_rock = Button(root, image=root.rock, command=p_rock)
btn_paper = Button(root, image=root.paper, command=p_paper)
btn_scissors = Button(root, image=root.scissors, command=p_scissors)

# Display Buttons
btn_rock_canvas = canvas1.create_window(30, 320, anchor="nw", window=btn_rock)
btn_paper_canvas = canvas1.create_window(140, 320, anchor="nw", window=btn_paper)
btn_scissors_canvas = canvas1.create_window(250, 320, anchor="nw", window=btn_scissors)


root.mainloop()
