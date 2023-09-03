# web application - 1market 

The app is marketplace similar to a kaspi.kz/shop. 

**Technology Stack**

- Django
- SQLite


### **Class Diagram**
![alt png](class-diagram-of-project.png)


## Запуск проекта

Установить зависимости:

```bash
poetry install
```

Войти в окружение poetry:

```bash
poetry shell
```


## Запустить Django-приложение.

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

После этого сервер запуститься на порту 8000. Чтобы проверить подключение сделайте запрос на [localhost:8000](http://localhost:8000).


**Swagger**

http://127.0.0.1:8000/swagger/