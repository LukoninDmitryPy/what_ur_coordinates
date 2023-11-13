# What-ur-coordinates
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![REST API](https://img.shields.io/badge/-REST%20API-464646?style=flat-square&logo=REST%20API)](https://restfulapi.net/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)

What-ur-coordinates является сервисом для работы с координатами и внешнем сервисом.

## Над проектом работал:
- [Дмитрий Луконин](https://t.me/folite999)

## Подготовка и запуск проекта
### Склонировать репозиторий на локальную машину:
```
git clone https://github.com/lukonindmitrypy/what_ur_coordinates
```

### Запуск проекта:

```
docker-compose up -d
```
## Использованые фреймворки и библиотеки:
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [drf-nested-routers](https://github.com/alanjds/drf-nested-routers)
- [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/)
- [Gunicorn](https://gunicorn.org/)

## Работа с API через Postman Agent

#### Для получения всех координат:

```
GET http://127.0.0.1/api/coordinates/
```
#### Для получения координат по id:
```
GET http://127.0.0.1/api/coordinates/{id}/
```

#### Для получения всех результатов по координатам:
```
GET http://127.0.0.1/api/result/
```
#### Для получения результата по координатам по id:
```
GET http://127.0.0.1/api/result/{id}/
```

#### Для обращения к стороннему сервису для координат:
```
GET http://127.0.0.1/api/result/boolea/
{
  "coordinates": кадастровый_номер(cadastral_numb)
}
```

#### Для получения истории обращения:
```
GET http://127.0.0.1/api/result/history/
```

#### Узнать соостояние стороннего сервера:
```
GET http://127.0.0.1/api/ping/
```