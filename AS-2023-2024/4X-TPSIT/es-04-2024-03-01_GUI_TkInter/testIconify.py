import tkinter as tk

def riduci():
	winApp.iconify()

winApp = tk.Tk()
winApp.iconbitmap('./favicon.ico')
winApp.wm_iconbitmap('./favicon.ico')
winApp.title('Applicazione Riducibile')

# Creazione di un pulsante per ridurre l'applicazione
iconifyBtn = tk.Button(winApp, text = 'Riduci', command = riduci)
iconifyBtn.pack()

if __name__ == '__main__':
	winApp.mainloop()