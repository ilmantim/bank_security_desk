# Пульт охраны банка

Это внутренни репозитарий для сотрудников банка "Devman". Если вы попали в этот репозитарий случайно, то вы не сможете его запустить, т.к. у Вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны - это сайт, который можно подклюить к удаленной базе данных с визитами и карточками пропуска сотрудников Вашего банка.

## Как установить

Создайте файл .env в корневом каталоге проекта и укажите в нём необходимые переменные окружения.

SECRET_KEY: Секретный ключ Django. 

DB_HOST: Адрес хоста базы данных, к которой нужно подключиться.

DB_PORT: Порт базы данных, к которой нужно подключиться.

DB_NAME: Имя базы данных.

DB_USER: Имя пользователя базы данных.

DB_PASSWORD: Пароль пользователя базы данных.


Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

pip install -r requirements.txt

Запустите сервер:

python manage.py runserver localhost:8000

После запуска сервера, вы сможете получить доступ к приложению в браузере по адресу: http://localhost:8000/

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.

```bash
pip install -r requirements.txt
python manage.py runserver localhost:8000
