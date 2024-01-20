# Торговая сеть электроники

Данный проект является  веб-приложением с API интерфейсом и админ-панелью, цель которго - управление торговой сетью электроники. Сеть представлять собой иерархическую структуру из 3 уровней: завод,
розничная сеть, индивидуальный предприниматель. В приложении реализован функционал управления компаниями и продуктами, которые они продают.
#
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)

### Технологии:
- Python 3.11
- Django 5.0.1
- Django REST framework 3.14.0
- PostgreSQL

### Инструкция по развертыванию проекта:

Клонирование проекта:
```
git clone https://github.com/nataliamelnik138/trading_network
```
Запуск:
1. Создайте виртуальное окружение
```
python -m venv venv
```
2. Активируйте виртуальное окружение
```
venv/Skripts/activate
```
4. Установите зависимости
```
pip install -r requirements.txt
```
6. Создайте в папке проекта файл .env, который должен содержать значение переменных из файла .env.sample
7. Примените миграции
```
python manage.py migrate
```
6. Запустите проект
```
python manage.py runserver
```

#### Автор проекта: Мельник Наталья
