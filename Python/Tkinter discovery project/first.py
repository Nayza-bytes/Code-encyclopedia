import tkinter as tk

#Setup variables
mainapp = tk.Tk()

win_width = 920
win_height = 640
screen_wdth = int(mainapp.winfo_screenwidth())
screen_hght = int(mainapp.winfo_height())
Position_X = (screen_wdth // 2) - (win_width // 2)
#Position_Y = (screen_hght // 2) - (win_height // 2)
geometry = '{}x{}'.format(win_width, win_height)




#setup Main window
mainapp.title('Windows program')
mainapp.minsize(win_width, win_height)
mainapp.geometry(geometry)
mainapp['bg'] = "#23262e"

#Method for stoping user resize
#mainapp.resizable(width=False, height=False)
#default position when the window is open
#mainapp.positionfrom('user')

#Widgets creations
home_label = tk.Label(mainapp, text='Home')

#adding labels
home_label.pack()

mainapp.mainloop()