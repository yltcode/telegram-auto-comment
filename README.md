# Автоматическое комментирование постов в Telegram

[![license](https://shields.io/github/license/yltcode/telegram-auto-comment?style=flat-square&color=blue)](https://www.gnu.org/licenses/quick-guide-gplv3.ru.html)

[![code-size](https://shields.io/github/languages/code-size/yltcode/telegram-auto-comment?style=flat-square&color=orange)](https://github.com/yltcode/telegram-auto-comment)

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

В инструкции будет использоваться `nano`, а Вы можете использовать любой другой текстовый редактор

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
