# avalab_hackathon
The project for hackathon of avalab 

#### Требования

- установленный npm

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
NPM_PATH=
```

Для получения секретного ключа обратитесь к @Alexander-vlk
В качестве NPM_PATH укажите абсолютный путь к файлу npm.cmd

#### Запуск прооекта

Для разработки
```bash
docker-compose -f docker-compose.dev.yml up
```

Для прода
```bash
docker-compose -f docker-compose.yml up
```

Запуск проекта
```python
python manage.py tailwind start
python manage.py runserver
```
#### Date: 22.11.2024
