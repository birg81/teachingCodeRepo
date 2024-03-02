from tkinter import *

winApp = Tk()
winApp.iconbitmap('./favicon.ico')
winApp.wm_iconbitmap('./favicon.ico')
winApp.geometry('300x300')

myb1 = Button(winApp, text = 'A', fg = 'Red', bg = 'LightGreen')
myb1.pack(fill = NONE)

myb2 = Button(winApp, text = 'B', fg = 'Red', bg = 'LightGreen')
myb2.pack(fill = X, padx = 10, pady = 10)

myb3 = Button(winApp, text = 'C', fg = 'Red', bg = 'LightGreen')
myb3.pack(side = LEFT, fill = Y, padx = 10, pady = 10)

myb3 = Button(winApp, text = 'D', fg = 'Red', bg = 'LightGreen')
myb3.pack(side = TOP, fill = X, padx = 10, pady = 10)

myb4 = Button(winApp, text = 'E', fg = 'Red', bg = 'LightGreen')
myb4.pack(side = BOTTOM, fill = X, padx = 10, pady = 10)

myb5 = Button(winApp, text = 'F', fg = 'Red', bg = 'LightGreen')
myb5.pack(side = RIGHT, fill = BOTH, expand = 1, padx = 10, pady = 10)

if __name__ == '__main__':
	winApp.mainloop()