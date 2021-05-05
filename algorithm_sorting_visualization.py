from tkinter import *
from tkinter import ttk
import random
from Bubble_Sort import bubble_sort

root = Tk()
root.title("Sorting_Algorithm_visualization")
root.maxsize(900, 600)
root.config(bg = "black")

selected_algorithm = StringVar()
data = []


def draw_Data(data, color_array):
  canvas.delete("all")
  c_height = 380
  c_width = 600
  x_width = c_width / (len(data) + 1)
  offset = 30
  spacing = 10
  normalized_data = [i / max(data) for i in data]
  for i, height in enumerate(normalized_data):
    x0 = i * x_width + offset + spacing
    y0 = c_height - height * 340
    x1 = (i + 1) * x_width + offset
    y1 = c_height
    canvas.create_rectangle(x0, y0, x1, y1, fill = color_array[i])
    canvas.create_text(x0 + 2, y0, anchor = SW, text = str(data[i]))
  
  root.update_idletasks()


def Create():
  global data
  min_Val = int(minEntry.get())
  max_Val = int(maxEntry.get())
  size = int(sizeEntry.get())
  
  data =[]
  for _ in range(size):
    data.append(random.randrange(min_Val, max_Val + 1))

  draw_Data(data, ["red" for x in range(len(data))])

def Start_algorithm():
  global data
  bubble_sort(data, draw_Data, speedScale.get())
  


#Frame
UI_frame = Frame(root, width = 600, height = 200, bg = "grey")
UI_frame.grid(row = 0, column = 0, padx = 10, pady = 5)

canvas = Canvas(root, width = 600, height = 380, bg = 'white')
canvas.grid(row = 1, column = 0, padx = 10, pady = 5)

#UI_Area
Label(UI_frame, text = "Algorithm: ", bg = "grey").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = W)
algMenu = ttk.Combobox(UI_frame, textvariable = selected_algorithm, values = ["Bubble_Sort"])
algMenu.grid(row = 0, column = 1, padx = 5, pady = 5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_ = 0.1, to = 2.0, length = 200, digit = 2, resolution = 0.2, orient = HORIZONTAL, label = "Selecte speed [s]")
speedScale.grid(row = 0, column = 2, padx = 5, pady = 6)
Button(UI_frame, text = "Start", command =Start_algorithm, bg = "red").grid(row= 0, column = 3, padx= 5, pady = 5)


#row1
sizeEntry = Scale(UI_frame, from_ = 3, to = 25, resolution = 1, orient = HORIZONTAL, label = "Data Size")
sizeEntry.grid(row = 1, column = 0, padx = 5, pady = 5)

minEntry =Scale(UI_frame, from_ = 0, to = 10, resolution = 1, orient = HORIZONTAL, label = "Min Value")
minEntry.grid(row = 1, column = 1, padx = 5, pady = 5)


maxEntry = Scale(UI_frame, from_ = 3, to = 25, resolution = 1, orient = HORIZONTAL, label = "Max Value")
maxEntry.grid(row = 1, column = 2, padx = 5, pady = 5)

Button(UI_frame, text = "Create", command =Create, bg = "white").grid(row= 1, column = 3, padx= 5, pady = 5)


root = mainloop()