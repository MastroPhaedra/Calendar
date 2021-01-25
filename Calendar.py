from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import*
import calendar
import datetime
import random
from textwrap import wrap # дробит строчку по пробелам
import pyperclip # позволяет копировать в буфер # pip install pyperclip
from my_weather import*
#
root = Tk()
root.title("С добрым утром!")
days = []
now = datetime.datetime.now()
year = now.year
month = now.month
root.geometry("570x420")
root.resizable(width=False, height=False)
#
tab_control=ttk.Notebook(root)
tab1=Frame(tab_control)
tab2=Frame(tab_control)
tab3=Frame(tab_control)
tab4=Frame(tab_control)
tab_control.add(tab1,text="Календарь")
tab_control.add(tab2,text="Погода")
tab_control.add(tab3,text="Гороскоп")
tab_control.add(tab4,text="Заметки")
#
def osnov_calendar(): # для красоты, изначальную задумку в нём не выполнить
    #
    def prew():
        global month, year
        month -= 1
        if month == 0:
            month = 12
            year -= 1
        fill()
    #
    def next():
        global month, year
        month += 1
        if month == 13:
            month = 1
            year += 1
        fill()
    # 
    def fill():
        info_label["text"] = calendar.month_name[month] + ", " + str(year)
        month_days = calendar.monthrange(year, month)[1]
        if month == 1:
            prew_month_days = calendar.monthrange(year-1, 12)[1]
        else:
            prew_month_days = calendar.monthrange(year, month - 1)[1]
        week_day = calendar.monthrange(year, month)[0]
        for n in range(month_days):
            days[n + week_day]["text"] = n+1
            days[n + week_day]["fg"] = "black"
            if year == now.year and month == now.month and n == now.day-1:
                days[n + week_day]["background"] = "green"
            else:
                days[n + week_day]["background"] = "lightgray"
        for n in range(week_day):
            days[week_day - n - 1]["text"] = prew_month_days - n
            days[week_day - n - 1]["fg"] = "gray"
            days[week_day - n - 1]["background"] = "#f3f3f3"
        for n in range(6*7 - month_days - week_day):
            days[week_day + month_days + n]["text"] = n+1
            days[week_day + month_days + n]["fg"] = "gray"
            days[week_day + month_days + n]["background"] = "#f3f3f3"
    # вывод календаря через TKinter
    # заголовок (месяц, год), кнопки назад и вперёд
    prew_button = Button(tab1, text="<", command=prew)
    prew_button.grid(row=0, column=0, sticky="nsew")
    next_button = Button(tab1, text=">", command=next)
    next_button.grid(row=0, column=6, sticky="nsew")
    info_label = Label(tab1, text="0", width=1, height=1, 
                font=("Verdana", 16, "bold"), fg="#ffb700")
    info_label.grid(row=0, column=1, columnspan=5, sticky="nsew")
    # числовые блоки
    for n in range(7):
        lbl = Label(tab1, text=calendar.day_abbr[n], width=1, height=1, 
                    font=("Verdana", 10, "normal"), fg="darkblue")
        lbl.grid(row=1, column=n, sticky="nsew")
    for row in range(6):
        for col in range(7):
             lbl = Label(tab1, text="0", width=5, height=2, font=("Verdana", 16, "bold"))
             lbl.grid(row=row+2, column=col, sticky="nsew")
             days.append(lbl)
    fill() # для запуска в том или ином окне, везде, где требует root, надо прописать tab[номер]
#
def osn_goroskop():
    global first, second1, second2, third, goroskop, wrapped_goroskop
    def loe_fail(f):
        fail=open(f,'r')
        mas=[] 
        for rida in fail:
            mas.append(rida.strip(";\n"))
        fail.close()
        return mas
    first = loe_fail("first_file.txt")
    second1 = loe_fail("second1_file.txt")
    second2 = loe_fail("second2_file.txt")
    third = loe_fail("third_file.txt")
    goroskop=(random.choice(first))+" "+(random.choice(second1))+" "+(random.choice(second2))+" "+(random.choice(third))
    wrapped_goroskop="\n".join(wrap(goroskop)) # расчёты / на основе этой функции и работает top_goroskop()
#
def top_goroskop():
    #
    osn_goroskop()
    #
    #c_box=ttk.Combobox(tab3, values=["Овен","Телец","Близнецы","Рак","Лев","Дева","Весы","Скорпион","Змееносец","Стрелец","Козерог","Водолей","Рыбы"],state="readonly")
    #c_box.grid(row=0, padx=25, pady=5, sticky="NESW")
    #
    lbl2=Label(tab3,text="Универсальный гороскоп для всех знаков зодиака",font=("Verdana", 13))
    lbl2.grid(row=0, padx=25, pady=5, sticky="NESW")
    #
    def pkm_lbl(event):
        frame_top = Frame(tab3, bg="#ffb700", bd=5)
        frame_top.grid(row=1, padx=12, pady=10)
        lbl=Label(frame_top, text=wrapped_goroskop, bg="#ffb700")
        lbl.grid()
    #
    def buffer_skop(event): # нужен для копирования в буффер
        pyperclip.copy(goroskop)
    # Спрашиваем у пользователя про его знак (буду брать данные у пользователя, через Combobox и/или messagebox у tkinter)
    btn=Button(tab3, text="Посмотреть гороскоп на сегодня",font=("Verdana", 16, "bold"), bg="lightgray")
    btn.bind("<Button-1>", pkm_lbl)
    btn.grid(row=2, padx=25, pady=5, sticky="NESW")
    btn2=Button(tab3, text="Скопировать гороскоп",font=("Verdana", 16, "bold"), bg="gray")
    btn2.bind("<Button-1>", buffer_skop)
    btn2.grid(row=3, padx=25, pady=5, sticky="NESW")
#
def top_spisok():
    #
    def save_file(event):
        s_file=asksaveasfile(mode="w",defaultextension=((".txt"),(".doc")),filetypes=(("Notepad",".txt"),("Word",".doc")))
        text=txt.get(0.0,END)
        s_file.write(text) # если текст не менялся, вылезает ошибка по поводу "записи"
        s_file.close()
    def open_file(event):
        txt.delete('1.0', END)
        o_file=askopenfile()
        text_in=o_file.read()
        txt.insert(INSERT,text_in)
        txt.focus()
        o_file.close()
    def buffer_vstav(event):
        pyperclip.copy(goroskop)
        buf=pyperclip.paste()
        txt.insert(INSERT,buf)
        txt.focus()
    #
    txt=scrolledtext.ScrolledText(tab4,width=68,height=9) #text=(f"---- {now.day}.{now.month}.{now.year} ---- ")
    txt.grid(row=0,column=0,columnspan=3)
    text_in=(f"---- {now.day}.{now.month}.{now.year} ----\n")
    txt.insert(INSERT,text_in)
    txt.focus()
    btn_txt=Button(tab4, text="Сохранить как...")
    btn_txt.bind("<Button-1>", save_file)
    btn_txt.grid(row=1,column=0)
    btn_txt2=Button(tab4, text="Открыть файл")
    btn_txt2.bind("<Button-1>", open_file)
    btn_txt2.grid(row=1,column=1)
    btn_txt3=Button(tab4, text="Вставить гороскоп")
    btn_txt3.bind("<Button-1>", buffer_vstav)
    btn_txt3.grid(row=1,column=2)
# tab1
osnov_calendar()
# tab2
top_weather(tab2,now)
# tab3
top_goroskop()
# tab4
top_spisok()
#
tab_control.pack(expand=1, fill="both")
#
root.mainloop()