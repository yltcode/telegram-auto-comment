# Автоматическое комментирование постов в Telegram

[![license](https://img.shields.io/github/license/yltcode/telegram-auto-comment?style=for-the-badge)](LICENSE)
[![last-commit](https://img.shields.io/github/last-commit/FoxUserbot/FoxUserbot?style=for-the-badge)](https://github.com/yltcode/telegram-auto-comment/commits/main)
[![codefactor](https://www.codefactor.io/repository/github/FoxUserbot/FoxUserbot/badge?style=for-the-badge)]()
[![stars](https://img.shields.io/github/stars/yltcode/telegram-auto-comment?style=for-the-badge)]()
[![repo-size](https://img.shields.io/github/repo-size/yltcode/telegram-auto-comment?style=for-the-badge)]()
[![languages](https://img.shields.io/github/languages/top/yltcode/telegram-auto-comment?style=for-the-badge)]()
[![python](https://img.shields.io/badge/python-%3E%203.6-blue?style=for-the-badge)]()

## Установка
- #### Клонирование репозитория

```sh
git clone https://github.com/yltcode/telegram-auto-comment
```

- #### Установка зависимостей

```sh
pip3 install -r requirements.txt
```

- #### Редактирование конфига

```sh
nano config.yaml
```

И изменяем сообщения из `messages` на свои

`CTRL + O + ENTER` - чтобы сохранить

`CTRL + X` - чтобы выйти

- #### Запускаем

```sh
python3 main.py
```

Вводим номер телефона и код, который придет в Telegram

Если написано `Started for ...`, значит все верно

## Возможные ошибки

- #### The SSL module is not available

Отсутствует или не обновлен пакет openssl

```sh
apt update
apt install --only-upgrade openssl
```
