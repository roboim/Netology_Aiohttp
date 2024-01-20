# Домашнее задание к лекции «Aiohttp»

Инструкцию по сдаче домашнего задания вы найдете на главной странице репозитория.

## Задание 1

Переписать сервис из [домашнего задания по Flask](../2.1-flask) на aiohttp.

Результатом работы является API, написанный на aiohttp.

## Задание 2 (необязательное)

Докеризировать API, написанный в задании 1.  
Чтобы проверить корректность работы сервиса, нужно:
1. запустить контейнер
2. проверить работу

________________________________________________________________________________

# Домашнее задание к лекции «Flask»

Инструкцию по сдаче домашнего задания вы найдете на главной странице репозитория. 

## Задание 1

Вам нужно написать REST API (backend) для сайта объявлений.

Должны быть реализованы методы создания/удаления/редактирования объявления.    

У объявления должны быть следующие поля: 
- заголовок
- описание
- дата создания
- владелец

Результатом работы является API, написанное на Flask.

Этапы выполнения задания:

1. Сделайте роут на Flask.
2. POST метод должен создавать объявление, GET - получать объявление, DELETE - удалять объявление.

## Задание 2 *(не обязательное)

Добавить систему прав.

Создавать объявление может только авторизованный пользователь.
Удалять/редактировать может только владелец объявления.
В таблице с пользователями должны быть как минимум следующие поля: идентификатор, почта и хэш пароля.