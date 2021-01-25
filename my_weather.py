from tkinter import *
import requests # pip install requests

#
def top_weather(tab2,now):
    def get_weather():
        # поиск только для Таллинна
	    url = "http://api.openweathermap.org/data/2.5/weather?q=Tallinn&appid=82b797b6ebc625032318e16f1b42c016&units=metric"
	    result = requests.get(url)
	    # Получаем JSON ответ по этому URL
	    weather = result.json()
	    # Полученные данные добавляем в текстовую надпись для отображения пользователю
	    info1["text"] = f'Температура: {weather["main"]["temp"]} С°' # температура находится в цельсиях (благодаря units=metric)
	    info2["text"] = f'Давление: {weather["main"]["pressure"]} hPa' 
	    info3["text"] = f'Влажность: {weather["main"]["humidity"]} %' 
    frame_top = Frame(tab2, bg="#ffb700", bd=5)
    frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)
    frame_bottom = Frame(tab2, bg="#ffb700", bd=5)
    frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.21)
    cityField = Label(frame_top, text=(f"Таллинн - {now.day} число"), bg="#ffb700", font=("Verdana", 16, "bold"))
    cityField.pack(pady=13)
    btn = Button(frame_top, text="Получить последние данные", command=get_weather)
    btn.pack(pady=4)
    info1 = Label(frame_bottom, text="Информация о температуре", bg="#ffb700", font=40)
    info1.pack()
    info2 = Label(frame_bottom, text="Информация о давлении", bg="#ffb700", font=40)
    info2.pack()
    info3 = Label(frame_bottom, text="Информация о влажности", bg="#ffb700", font=40)
    info3.pack()

