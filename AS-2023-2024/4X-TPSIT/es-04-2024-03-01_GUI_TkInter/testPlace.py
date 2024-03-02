from tkinter import *

winApp = Tk()
winApp.geometry('600x600')

mybtn_height = Button(winApp, text = '60px high')
mybtn_height.place(height = 60, x = 300, y = 300)

mybtn_width = Button(winApp, text = '70px wide')
mybtn_width.place(width = 70, x = 400, y = 400)

mybtn_relheight = Button(winApp, text = 'relheight of 0.7')
mybtn_relheight.place(relheight = 0.7)

mybtn_relwidth = Button(winApp, text = 'relwidth of 0.4')
mybtn_relwidth.place(relwidth = 0.4)

mybtn_relx = Button(winApp, text = 'relx of 0.5')
mybtn_relx.place(relx = 0.5)

mybtn_rely = Button(winApp, text = 'rely of 0.8')
mybtn_rely.place(rely = 0.8)

mybtn_x = Button(winApp, text = 'X = 500px')
mybtn_x.place(x = 500)

mybtn_y = Button(winApp, text = 'Y = 520')
mybtn_y.place(y = 520)

if __name__ == '__main__':
	winApp.mainloop()