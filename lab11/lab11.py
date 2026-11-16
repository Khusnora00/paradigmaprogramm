import tkinter as tk
from tkinter import ttk, messagebox


# Создание главного окна
root = tk.Tk()
root.title('Библиотека — Выдача книг')
root.geometry('700x480')
root.resizable(False, False)


# Переменные интерфейса
reader_var = tk.StringVar()
book_var = tk.StringVar(value='Python для начинающих')
status_var = tk.StringVar(value='Готово')
count_var = tk.StringVar(value='Активных выдач: 0')


# Список записей предметной области
registrations = []


# Создание основного контейнера
frame = ttk.Frame(root, padding=16)
frame.pack(fill='both', expand=True)

frame.columnconfigure(1, weight=1)
frame.rowconfigure(3, weight=1)


# Заголовок
title_label = ttk.Label(
    frame,
    text='Система выдачи книг',
    font=('Arial', 16, 'bold')
)
title_label.grid(row=0, column=0, columnspan=3, pady=10)


# Поле читателя
ttk.Label(frame, text='Имя читателя').grid(
    row=1, column=0, sticky='w', pady=5
)

reader_entry = ttk.Entry(
    frame,
    textvariable=reader_var
)
reader_entry.grid(
    row=1, column=1, columnspan=2,
    sticky='ew', padx=8, pady=5
)


# Список книг
ttk.Label(frame, text='Название книги').grid(
    row=2, column=0, sticky='w', pady=5
)

book_box = ttk.Combobox(
    frame,
    textvariable=book_var,
    state='readonly',
    values=[
        'Python для начинающих',
        'Основы программирования',
        'Искусственный интеллект',
        'Базы данных',
        'Алгоритмы и структуры данных'
    ]
)

book_box.grid(
    row=2, column=1, columnspan=2,
    sticky='ew', padx=8, pady=5
)


# Кнопки
register_button = ttk.Button(
    frame,
    text='Выдать книгу'
)
register_button.grid(
    row=3, column=0, sticky='ew', padx=5, pady=8
)

clear_button = ttk.Button(
    frame,
    text='Очистить список'
)
clear_button.grid(
    row=3, column=1, sticky='ew', padx=5, pady=8
)


# Список результатов
result_list = tk.Listbox(
    frame,
    height=12,
    font=('Arial', 10)
)

result_list.grid(
    row=4, column=0, columnspan=3,
    sticky='nsew', pady=10
)

frame.rowconfigure(4, weight=1)


# Счётчик и строка состояния
ttk.Label(
    frame,
    textvariable=count_var
).grid(row=5, column=0, sticky='w')

ttk.Label(
    frame,
    textvariable=status_var
).grid(row=5, column=1, columnspan=2, sticky='e')


# Сброс сообщения
def reset_status():
    status_var.set('Готово')


# Отображение временного сообщения
def set_status(text):
    status_var.set(text)
    root.after(2500, reset_status)


# Обновление списка и счётчика
def update_list():
    result_list.delete(0, tk.END)

    active_count = 0

    for item in registrations:
        if item['returned']:
            status = 'Возвращена'
        else:
            status = 'Выдана'
            active_count += 1

        result_list.insert(
            tk.END,
            f"{item['reader']} — {item['book']} [{status}]"
        )

    count_var.set(f'Активных выдач: {active_count}')


# Выдача книги
def register():
    reader = reader_var.get().strip()
    book = book_var.get()

    if len(reader) < 2:
        messagebox.showwarning(
            'Проверка',
            'Введите имя читателя'
        )
        reader_entry.focus_set()
        return

    if not book:
        messagebox.showwarning(
            'Проверка',
            'Выберите книгу'
        )
        return

    # Проверка повторной выдачи
    for item in registrations:
        if (
            item['reader'].lower() == reader.lower()
            and item['book'] == book
            and not item['returned']
        ):
            set_status('Эта книга уже выдана читателю')
            return

    # Добавление новой записи
    registrations.append({
        'reader': reader,
        'book': book,
        'returned': False
    })

    update_list()

    reader_var.set('')
    reader_entry.focus_set()

    set_status('Книга успешно выдана')


# Обработчик клавиши Enter
def register_from_event(event):
    register()


# Возврат книги двойным щелчком
def return_book(event):
    selection = result_list.curselection()

    if not selection:
        return

    index = selection[0]

    item = registrations[index]

    if item['returned']:
        set_status('Книга уже возвращена')
        return

    item['returned'] = True

    update_list()

    set_status('Книга успешно возвращена')


# Очистка списка
def clear_all():
    if not registrations:
        set_status('Список уже пуст')
        return

    answer = messagebox.askyesno(
        'Подтверждение',
        'Удалить все записи о выдаче книг?'
    )

    if answer:
        registrations.clear()
        update_list()
        set_status('Список очищен')


# Подключение обработчиков событий
register_button.config(command=register)

clear_button.config(command=clear_all)

root.bind('<Return>', register_from_event)

result_list.bind('<Double-Button-1>', return_book)


# Установка начального фокуса
reader_entry.focus_set()


# Запуск главного цикла
root.mainloop() 