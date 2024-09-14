import os

from tkinter import *

from tkinter import filedialog, colorchooser, font

from tkinter.messagebox import *

from tkinter.filedialog import *

def change_color():
  color = colorchooser.askcolor(title="pick a color")
  text_area.config(fg=color[1])

def change_font(*args):
  text_area.config(font=(font_name.get(), size_box.get()))
def about():
  showwarning("About This Texteditor", "This is a Program Written By Ezra Mekuria")

def quit():
  window.destroy()
def new_file():
  pass
def new_window():
  pass
def open_file():
  pass

def save_file():
  pass
def saveas_file():
  pass
def saveall_file():
  pass
def printt():
  pass
def cut():
  pass

def copy():
  pass

def paste():
  pass
def delete():
  pass
def find():
  pass

window = Tk()

window.title("TextEditor")
file = None

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width / 2))

y = int((screen_height/2) - (window_height / 2))


window.geometry("{}x{}+{}+{}".format(window_width,window_height,x,y))

font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar(window)
font_size.set("23")

text_area = Text(window, font=(font_name.get(), font_size.get()))

Scroll_bar=Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
Scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=Scroll_bar.set)

text_area.grid(sticky=N + E + S +W)

frame =Frame(window)
frame.grid()

color_b=Button(frame, text="color", command=change_color)
color_b.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox (frame, from_=1, to= 100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New Tab        Ctrl+N", command=new_file)
file_menu.add_command(label="New Window     Ctrl+Shift+N", command=new_window)
file_menu.add_command(label="Open           Ctrl+O", command=open_file)
file_menu.add_command(label="Save           Ctrl+S", command=save_file)
file_menu.add_command(label="Save As        Ctrl+Shift+S", command=saveas_file)
file_menu.add_command(label="Save All       Ctrl+Alt+S", command=saveall_file)

file_menu.add_separator()

file_menu.add_command(label="Print          Ctrl+Alt+P", command=printt)

file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_command(label="Delete", command=delete)
edit_menu.add_separator()
edit_menu.add_command(label="Find", command=find)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)



#color_menu = Menu(window)
#window.config(menu=color_menu)
#color_menuu=Menu(color_menu, tearoff=0)

#color_menu.add_cascade(label="color", menu=color_menuu)
#color_menuu.add_command(frame, text="color", command=change_color)
#color_b.grid(row=0, column=0)

window.mainloop()