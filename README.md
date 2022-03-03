# Tatem Music
![Image alt](https://res.cloudinary.com/tatemmedia/image/upload/v1644686783/tatemmusic.jpg)
---
## Описание 
Tatem Music - это площадка на которой вы сможете бесплатно генерировать музыку, а позже использовать в своих целях. [Ссылка на сайт](https://tatem2.pythonanywhere.com)
---
## Мотивация создание 
1. Любовь к музыки.
2. Желать сочинять музыку и автоматизировать это.
3. Узнать новое о генерации музыки.
---
## Инструкция по запуску
1. Скопируйте репозиторий и установите зависимость:
```bash
git clone https://github.com/Daniil-7/Tatem-Music.git
cd Tatem-Music
pip install -r requirements.txt
```
2. Настройка почты для регистрации:
Изменим настройки проекта. 
Файл ./gettingstarted/settings.py:
```python 
# изменяем переменые
EMAIL_HOST_USER = "ваша_почта@gmail.com"
EMAIL_HOST_PASSWORD = "пароль от почты"
```
Разрешите отправку почты вашему сайту. Для этого перейдите по ссылке и разрешите доступ:
https://www.google.com/settings/security/lesssecureapps

Затем пройдите по этой ссылке и подтвердите разрешение:
https://accounts.google.com/DisplayUnlockCaptcha

3. Запустите проект локально:
```python
python manage.py runserver
```
4. При диплои проекта не забудьте установить ключ:
файл ./gettingstarted/settings.py:
```python
SECRET_KEY = "ваш ключ"
```
---
## Использованные технологии
1. Python 3.10.2
2. Django 4.0
3. EasyMIDI 1.0
---
## Примичание 
1. [Ссылка на сайт проекта](https://tatem2.pythonanywhere.com)
2. [Сайт портфолио](https://tatem.pythonanywhere.com)