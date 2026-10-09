# Лабораторная работа №6

## Индивидуальный вариант №8 — Хранение посещаемости

### Цель работы

Разработать фрагмент информационной системы для хранения посещаемости студентов с использованием полиморфных реализаций хранилища.

### Реализованные компоненты

- `Repository` — общий контракт хранилища, определённый через `Protocol`.
- `DictRepository` — хранение данных в словаре.
- `FileRepositoryStub` — хранение данных в JSON-файле.
- `MemorySpy` — тестовая реализация для проверки обращений к хранилищу.
- `CachedRepository` — кеширующий компонент.
- `AttendanceService` — сервис, содержащий бизнес-логику работы с посещаемостью.

### Архитектура

Зависимость `Repository` передаётся в `AttendanceService` через конструктор.

Сервис работает только с операциями:

```text
save(student_id, attendance)
get(student_id)

Структура
lab6/
├── attendance/
│   ├── __init__.py
│   ├── repository.py
│   ├── repositories.py
│   ├── service.py
│   └── cached_repository.py
│
├── tests/
│   ├── __init__.py
│   └── test_attendance.py
│
├── main.py
├── README.md
└── .gitignore

Запуск автоматических тестов
python -m unittest discover -s tests -v
