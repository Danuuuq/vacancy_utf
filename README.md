# Проект Food API

API для получения списка категорий блюд и связанных с ними блюд. Реализовано в рамках тестового задания

## Требования

- Python 3.x
- Django 5.x
- Django REST Framework
- python-dotenv (для использования переменных окружения)

## Установка

1. Клонирование репозитория:
   ```bash
   git clone git@github.com:<your_name>/vacancy_utf.git
   cd vacancy_utf
   ```

2. Установка зависимостей:
   ```bash
   pip install -r requirements.txt
   ```

3. В файле `.env` необходимо указать следующие переменные окружения:
   ```bash
   SECRET_KEY=your-secret-key
   DEBUG=True
   ```

4. Создание БД и таблиц:
   ```bash
   python manage.py migrate
   ```

5. Запуск сервера:
   ```bash
   python manage.py runserver
   ```

## Эндпоинт API

- **`GET /api/v1/foods/`**: Возвращает список категорий блюд с их соответствующими блюдами.

### Пример запроса:
```bash
GET http://127.0.0.1:8000/api/v1/foods/
```

### Пример ответа:
```json
[
      {
         "id":1,
         "name_ru":"Напитки",
         "name_en":null,
         "name_ch":null,
         "order_id":10,
         "foods":[
            {
               "internal_code":100,
               "code":1,
               "name_ru":"Чай",
               "description_ru":"Чай 100 гр",
               "description_en":null,
               "description_ch":null,
               "is_vegan":false,
               "is_special":false,
               "cost":"123.00",
               "additional":[
                  200
               ]
            },
            {
               "internal_code":200,
               "code":2,
               "name_ru":"Кола",
               "description_ru":"Кола",
               "description_en":null,
               "description_ch":null,
               "is_vegan":false,
               "is_special":false,
               "cost":"123.00",
               "additional":[
                  
               ]
            },
            {
               "internal_code":300,
               "code":3,
               "name_ru":"Спрайт",
               "description_ru":"Спрайт",
               "description_en":null,
               "description_ch":null,
               "is_vegan":false,
               "is_special":false,
               "cost":"123.00",
               "additional":[
                  
               ]
            },
            {
               "internal_code":400,
               "code":4,
               "name_ru":"Байкал",
               "description_ru":"Байкал",
               "description_en":null,
               "description_ch":null,
               "is_vegan":false,
               "is_special":false,
               "cost":"123.00",
               "additional":[
                  
               ]
            }
         ]
      },
      {
         "id":2,
         "name_ru":"Выпечка",
         "name_en":null,
         "name_ch":null,
         "order_id":20,
         "foods":[]
      },
   ]
```
