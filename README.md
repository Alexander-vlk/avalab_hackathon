# avalab hackathon
Проект, представленный на хакатоне от avalab.

#### Схема работы

1. Данные собираются с сайта при помощи специальной команды, затем сохраняются в базу данных. 
2. Пользователь вводит в форму информацию о своем бизнесе (или стартапе)
3. Полученные данные отправляются на сервер, где искусственный интеллект обрабатывает их и данные, полученные с сайта, а затем отправляет список подходящих для этого пользователя мер поддержки бизнеса

![scheme](scheme.png)

#### Требования

- установленный npm
- pgAdmin

#### Установка

Клонируйте репозиторий
```bash
git clone https://github.com/Alexander-vlk/avalab_hackathon.git
```

Установите виртуальное окружение и выберите нужный интерпретатор
```bash
py -m venv venv
```

#### Установка зависимостей
```bash
python -m pip install -r requirements.txt
```

#### .env
Создайте в папке project_root файл .env и вставьте туда следующий код
```env
DEBUG=True
DJANGO_SECRET_KEY=
PG_NAME=postgres
PG_USER=postgres
PG_PASSWORD=1234
PG_HOST=localhost
PG_PORT=5432
LANGUAGE_CODE=ru
```

Для получения секретного ключа обратитесь к @Alexander-vlk

#### PostgreSQL

В pgAdmin4 создайте базу данных с паролем, логином и названием БД, как указано в .env

#### Tailwindcss

```bash
python manage.py tailwind init
python manage.py tailwind install
```

#### Запуск прооекта

```bash
python manage.py tailwind start
python manage.py runserver
```
#### Date: 22.11.2024
