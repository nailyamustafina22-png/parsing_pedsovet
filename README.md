# Парсер статей с Pedsovet.org

## Описание
Программа парсит главную страницу сайта Pedsovet.org и извлекает данные из карточек статей.

## Что делает программа и какие данные извлекает
- Находит на странице карточки статей (прямоугольные виджеты)
- Извлекает из каждой карточки:
  - **Наименование статьи** (заголовок)
  - **Ссылку на полную статью**

## Откуда берется HTML
HTML-код загружается напрямую с главной страницы сайта:
https://pedsovet.org/

## Установка зависимостей

### 1. Клонируйте репозиторий
git clone https://github.com/nailyamustafina22-png/parsing_pedsovet.git

cd parsing_pedsovet

### 2. Создайте виртуальное окружение:
python -m venv venv

### 3. Активируйте виртуальное окружение:
source venv/bin/activate #Linux/Mac

venv\Scripts\activate #Windows

### 4. Установите зависимости:
pip install -r requirements.txt

### 5. Запуск программы:
python parse_pedagogy.py

## Результат работы
После запуска программа:

- Выводит в консоль количество найденных статей

- Показывает список всех статей с номерами

- Сохраняет данные в файл articles.json

Пример вывода в консоли:

Найдено статей: 27

1. Не списывание, а новый навык: нейросети в школьных работах
https://pedsovet.org/article/ne-spisyvanie-a-novyj-navyk-nejroseti-v-skolnyh-rabotah

2. Кинолог: плюсы и минусы профессии
https://pedsovet.org/article/kinolog-plusy-i-minusy-professii


Файл articles.json содержит:

json
[
  {
    "title": "Не списывание, а новый навык: нейросети в школьных работах",
    "link": "https://pedsovet.org/article/ne-spisyvanie-a-novyj-navyk-nejroseti-v-skolnyh-rabotah"
  },
  {
    "title": "Кинолог: плюсы и минусы профессии",
    "link": "https://pedsovet.org/article/kinolog-plusy-i-minusy-professii"
  }
]

## Используемые технологии
- Python 3 - язык программирования

- BeautifulSoup4 - парсинг HTML и поиск элементов

- Requests - загрузка веб-страниц

- JSON - сохранение результатов

## Структура проекта
- parse_pedagogy.py - основной скрипт парсера
- requirements.txt - зависимости: beautifulsoup4, requests, lxml
- README.md - документация
- .gitignore - исключает venv/, __pycache__/, articles.json

- articles.json - результаты



