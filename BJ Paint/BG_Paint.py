import tkinter as tk
from tkinter import ttk, colorchooser

def set_tool(tool):
    global current_tool
    current_tool = tool
    if tool == "draw":
        canvas.config(cursor="pencil")
    elif tool == "erase":
        canvas.config(cursor="circle")

def start_draw(event):
    global drawing
    drawing = True

def stop_draw(event):
    global drawing
    drawing = False

def draw(event):
    if drawing and current_tool == "draw":
        x, y = event.x, event.y
        x1, y1 = (x - pen_size), (y - pen_size)
        x2, y2 = (x + pen_size), (y + pen_size)
        canvas.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color, width=pen_size*2)

def start_erase(event):
    global drawing
    drawing = True

def stop_erase(event):
    global drawing
    drawing = False

def erase(event):
    if drawing and current_tool == "erase":
        x, y = event.x, event.y
        x1, y1 = (x - eraser_size), (y - eraser_size)
        x2, y2 = (x + eraser_size), (y + eraser_size)
        canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="white")

def choose_draw_tool():
    set_tool("draw")

def choose_erase_tool():
    set_tool("erase")

def set_pen_size(size):
    global pen_size
    pen_size = size

def set_eraser_size(size):
    global eraser_size
    eraser_size = size

def change_color_from_menu(event):
    selected_color = color_picker.get()
    global current_color
    current_color = selected_color
    canvas.config(bg=current_color)

def pick_custom_color():
    color = colorchooser.askcolor()[1]
    if color:
        color_picker.set(color)
        global current_color
        current_color = color
        canvas.config(bg=current_color)


root = tk.Tk()
root.title("BG_Paint")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a "Tools" menu
tools_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Tools", menu=tools_menu)
tools_menu.add_command(label="Draw", command=choose_draw_tool)
tools_menu.add_command(label="Erase", command=choose_erase_tool)

# Create a "Size" menu
size_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Size", menu=size_menu)

# Add options to increase the size of pen and eraser under "Size" menu
size_menu.add_command(label="Increase Pen Size", command=lambda: set_pen_size(pen_size + 1))
size_menu.add_command(label="Decrease Pen Size", command=lambda: set_pen_size(pen_size - 1))
size_menu.add_command(label="Increase Eraser Size", command=lambda: set_eraser_size(eraser_size + 1))
size_menu.add_command(label="Decrease Eraser Size", command=lambda: set_eraser_size(eraser_size - 1))

# Create the canvas below the menu
canvas = tk.Canvas(root, bg="white", width=800, height=600)
canvas.pack(fill=tk.BOTH, expand=True)

# Set default tool to draw
set_tool("draw")

# Bind mouse events to canvas
drawing = False
current_tool = "draw"
pen_size = 3
eraser_size = 10
current_color = "black"

canvas.bind("<ButtonPress-1>", start_draw)   # Use left-click to draw
canvas.bind("<ButtonRelease-1>", stop_draw)
canvas.bind("<ButtonPress-3>", start_erase)  # Use right-click to erase
canvas.bind("<ButtonRelease-3>", stop_erase)
canvas.bind("<B1-Motion>", draw)            # Motion for drawing
canvas.bind("<B3-Motion>", erase)           # Motion for erasing

# Create the color picker
color_picker = ttk.Combobox(root, values=["black", "red", "green", "blue", "yellow"])
color_picker.set("black")
color_picker.pack()
color_picker.bind("<<ComboboxSelected>>", change_color_from_menu)

# Create a button to open a custom color picker dialog
custom_color_button = ttk.Button(root, text="Pick Custom Color", command=pick_custom_color)
custom_color_button.pack()

root.mainloop()
