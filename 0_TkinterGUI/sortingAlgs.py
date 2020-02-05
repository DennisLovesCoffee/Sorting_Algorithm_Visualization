from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(900, 600)
root.config(bg='black')

#variables
selected_alg = StringVar()

def drawData(data):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill="red")
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

def Generate():
    print('Alg Selected: ' + selected_alg.get())
    try:
        minVal = int(minEntry.get())
    except:
        minVal = 1
    try:
        maxVal = int(maxEntry.get())
    except:
        maxVal = 10
    try:
        size = int(sizeEntry.get())
    except:
        size = 10

    if minVal < 0 : minVal = 0
    if maxVal > 100 : maxVal = 100
    if size > 30 or size < 3: size = 25
    if minVal > maxVal : minVal, maxVal = maxVal, minVal

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    drawData(data)

#frame / base lauout
UI_frame = Frame(root, width= 600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

#User Interface Area
#Row[0]
Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)
Button(UI_frame, text="Generate", command=Generate, bg='red').grid(row=0, column=2, padx=5, pady=5)
#Row[1]
Label(UI_frame, text="Size ", bg='grey').grid(row=1, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

Label(UI_frame, text="Min Value ", bg='grey').grid(row=1, column=2, padx=5, pady=5, sticky=W)
minEntry = Entry(UI_frame)
minEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

Label(UI_frame, text="Max Value ", bg='grey').grid(row=1, column=4, padx=5, pady=5, sticky=W)
maxEntry = Entry(UI_frame)
maxEntry.grid(row=1, column=5, padx=5, pady=5, sticky=W)

root.mainloop()

