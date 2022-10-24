#============================= Memory Game =============================#
#                                                                       #
#                 Number Memory Game made with Python                   #
#                                                                       #
#                                                     @FranGarcia94     #
#=======================================================================#

from tkinter import *
from random import sample
from tkinter.ttk import Separator
import time
from tkinter import ttk
from random import *



def game(level: int):

    global win
    win = 0

    # To size the frame when a new level is selected
    try:

        print(root.grid_slaves()[0].destroy())
    except:

        pass


    mf2 = Frame(root)
    mf2.grid(row = 1, column = 0)
    mf2.config(bg = my_bg)


    start_time = time.time()

    mf2.config(highlightthickness = 5, highlightbackground = 'gray')

    def fun(m):

        global compare, rl, rl_2, aux, couple_index, win
        

        if aux == 0:

            compare.append(sl[m])
            couple_index = m
            bb[m]['text'] = sl[m]

            aux = 1
        elif aux == 1:

            if m != couple_index:

                compare.append(sl[m])
                bb[m]['text'] = sl[m]
                root.update_idletasks()
                root.after(200)
            else:
                
                compare.append(len(sl))
                bb[m]['text'] = sl[m]
                root.update_idletasks()
                root.after(200)
            
            if compare[0] == compare[1]:

                root.update_idletasks()
                bb[m]['bg'] = '#ffdf00'
                bb[m]['text'] = ''
                bb[m]['image'] = tro_im
                bb[m].config(width = 88, height = 48)

                bb[couple_index]['text'] = ''
                bb[couple_index]['bg'] = '#ffdf00'
                bb[couple_index]['image'] = tro_im
                bb[couple_index].config(width = 88, height = 48)

                if flashVar.get() == 1:

                    bb[m].flash()
                    bb[couple_index].flash()
                
                win += 2
            else:
                
                bb[couple_index]['text'] = ''
                bb[m]['text'] = ''

            #bb[couple_index].config(state='normal')
            couple_index = 0    
            compare = []
            aux = 0
            

        if win == len(sl):
            
            end_time = time.time()

            total_time = round(end_time - start_time, 2)
            minutes = int(total_time//60)
            seconds = round(total_time%60, 2)

            win_fun(minutes, seconds, level)


    n = level
    random_len = n*int(n/2)

    rl = sample([x for x in range(0,random_len)], random_len)
    rl_2 = sample([x for x in range(0,random_len)], random_len)
    sl = rl + rl_2

    print(f'Lista completa: {rl + rl_2}')
    print(f'Len lista: {len(rl + rl_2)}')

    cont = 0

    styl = ttk.Style()
    styl.configure('TSeparator', background='red')
    sep = Separator(mf2, orient = 'horizontal')
    sep.grid(row = int(n/2), column = 0, columnspan = n, sticky = 'ew', pady = 5)

    def enter_fun(cont):

        bb[cont].config(relief = 'groove')

    def leave_fun(cont):

        bb[cont].config(relief = 'raised')


    for i in range(n):

        for j in range(n):

            bb.append(str(cont))
            bb[cont] = Button(mf2, text = '', width = 7, height = 1, font = ('Pristina 17 bold'), command = lambda m = cont : fun(m))

            if cont < random_len:

                bb[cont].config(bg = my_blue, activebackground = my_bg, cursor = 'hand2')
                bb[cont].grid(row = i, column = j)
            else:

                bb[cont].config(bg = my_green, activebackground = my_bg, cursor = 'hand2')
                bb[cont].grid(row = i+1, column = j)

            bb[cont].bind('<Enter>', lambda event, cont = cont : enter_fun(cont))
            bb[cont].bind('<Leave>', lambda event, cont = cont : leave_fun(cont))
            cont += 1
    


    barraMenu = Menu(root)
    root.config(menu = barraMenu)

    checkVar.set(level)

    # To check if Flash checkbutton works well
    def flash_mode():
        # print(flashVar.get())
        pass

    def reset():
        global compare, aux
        compare = []
        aux = 0

    archivoMenu = Menu(barraMenu, tearoff = 0)
    archivoMenu.add_radiobutton(label = "Easy", activebackground = 'lightgreen', image = easy_2_im, columnbreak = 1, variable = checkVar, value=4, command = lambda: [game(4), reset()])
    archivoMenu.add_radiobutton(label = "Hard", activebackground = 'lightgreen', image = hard_2_im, columnbreak = 0, variable = checkVar, value=8, command = lambda: game(8))
    archivoMenu.add_separator()
    archivoMenu.add_radiobutton(label = "Extreme", activebackground = 'Black', image = extreme_2_im, columnbreak = 0, variable = checkVar, value=12, command = lambda: game(12))

    flashMenu = Menu(barraMenu, tearoff = 0)
    flashMenu.add_checkbutton(label = "Flash Buttons", activebackground = 'lightblue', image = flash_2_im, variable = flashVar, onvalue=1, offvalue=0, command = lambda: flash_mode())
    
    barraMenu.add_cascade(label = "Level", menu = archivoMenu)
    barraMenu.add_cascade(label = "Flash", menu = flashMenu)
    
    
def start_fun(level: int):

    mf3.destroy()
    root.config(bg = my_bg)

    game(level)


def win_fun(minutes, seconds, level):

    root.wm_attributes("-topmost", False)

    root_2 = Tk()
    root_2.focus_force()
    root_2.title('¡¡ WINNER !!')
    root_2.geometry('750x230+400+200')
    root_2.wm_attributes('-toolwindow', True)
    
    root_2.config(background = 'lightgreen')

    root_2.update()

    root_2.overrideredirect(True)

    lb_win = Label(root_2, text = '~~ CONGRATULATIONS ~~', font = ('Forte 34 bold'), background = 'lightgreen')
    lb_win.grid(row = 0, column = 0, sticky = 'wens')
    lb_win = Label(root_2, text = '~~ CONGRATULATIONS ~~', font = ('Magneto 34 bold'), background = 'lightgreen')
    lb_win.grid(row = 1, column = 0, sticky = 'wens')
    lb_win = Label(root_2, text = '~~ CONGRATULATIONS ~~', font = ('Broadway 34 bold'), background = 'lightgreen')
    lb_win.grid(row = 2, column = 0, sticky = 'wens')
    lb_win = Label(root_2, text = '~~ CONGRATULATIONS ~~', font = ('Terminal 34 bold'), background = 'lightgreen')
    lb_win.grid(row = 3, column = 0, sticky = 'wens')

    root_2.update()
    
    root_2.after(3000)
    root_2.overrideredirect(False)

    bw = Label(root_2, text = f'Time\nMinutes: {minutes} min\nSeconds: {seconds} s', font = ('Forte 22 bold'), highlightthickness=3, highlightbackground='black', background=my_bg)
    bw.place(relx = 0.5, rely = 0.5, anchor = 'center')

    root_2.geometry('222x108+400+200')

    root_2.update()
    
    def close_w(level):

        root_2.destroy()
        root.wm_attributes("-topmost", True)

        game(level)
        
    root_2.protocol("WM_DELETE_WINDOW", lambda: close_w(level))
    root_2.mainloop()





if __name__ == '__main__':

    aux = 0
    compare = []
    my_blue = '#7ed3fc'
    my_green = '#10b982'
    my_bg = '#98fad6'
    my_bg_2 = '#9d27b0'


    root = Tk()
    root.title('Memory Game')
    root.iconbitmap('C:\\Users\\...\\game.ico') # Insert URL
    root.wm_attributes("-topmost", True)
    root.wm_attributes('-transparentcolor', 'red')
    root.resizable(0,0)

    tro_im = PhotoImage(file = "C:\\Users\\...\\trophy.png") # Insert URL

    easy_im = PhotoImage(file = "C:\\...\\easy.png") # Insert URL
    hard_im = PhotoImage(file = "C:\\...\\hard.png") # Insert URL
    extreme_im = PhotoImage(file = "C:\\...\\extreme.png") # Insert URL

    easy_2_im = PhotoImage(file = "C:\\...\\easy_2.png") # Insert URL
    hard_2_im = PhotoImage(file = "C:\\...\\hard_2.png") # Insert URL
    extreme_2_im = PhotoImage(file = "C:\\...\\extreme_2.png") # Insert URL
    flash_2_im = PhotoImage(file = "C:\\...\\flash.png") # Insert URL


    mf1 = Frame(root)
    mf1.grid(row = 0, column = 0)

    mf3 = Frame(root)
    mf3.grid(row = 2, column = 0)

    bb = []
    couple_index = 0
    win = 0

    checkVar = IntVar()
    flashVar = IntVar()


    mf3.config(bg = my_bg_2, highlightthickness = 5, highlightbackground = 'black')


    level_label = Label(mf3, text = 'Select Level', font = ('Pristina 56 bold'), background = my_bg_2, foreground = '#ffdf00')
    level_label.grid(row = 0, column = 0, columnspan = 3)

    easy_button = Button(mf3, text ='easy', image = easy_im, bg = my_bg_2, activebackground = my_bg_2, relief = 'flat', cursor = 'hand2', command = lambda: start_fun(4))
    easy_button.grid(row = 1, column = 0, padx = 20)

    hard_button = Button(mf3, text = 'hard', image = hard_im, bg = my_bg_2, activebackground = my_bg_2, relief = 'flat', cursor = 'hand2', command = lambda: start_fun(8))
    hard_button.grid(row = 1, column = 1, padx = 20)

    extreme_button = Button(mf3, text = 'extreme', image = extreme_im, bg = my_bg_2, activebackground = my_bg_2, relief = 'flat', cursor = 'hand2', command = lambda: start_fun(12))
    extreme_button.grid(row = 1, column = 2, padx = 20, pady = 20)


    root.mainloop()