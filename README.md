РОУТЫ:

POST:
http://13.58.61.133:8000/auth/register/ - регистрация

*(username, password)*


POST:
http://13.58.61.133:8000/auth/login/ - логин

*(username, password)*


POST:
http://13.58.61.133:8000/token/refresh/ - обновить токены

*(refresh)*


GET:
http://13.58.61.133:8000/news/ - новости

передать: *bearer access token*


Краткое описание, как поднимал сервер:

В сервисе *EC2* в проекте поднимаю docker-compose, 
который поднимает Dockerfile,
в котором запускается сервер gunicorn
