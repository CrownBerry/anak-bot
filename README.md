# Anak Bot

VK-to-Telegram notifier bot.

## Getting Started

You can use this bot with any VK group you want, but now group ID hardcoded in `config.ini` file

### Installing

Just clone it
```
git clone https://github.com/CrownBerry/anak-bot.git
```

### Configuring

You can use your own config with this project.

Config.ini example

```
[DEFAULT]
tgToken: your telegram token
vkToken: service token VK API
group: VK group ID for subscribing
connectionString: sqlite:///file.db # path to sqlite3 database file
```

Also you need to install dependencies:
```
pip3 install -r requirements.txt
```

### Using

* Create bot with telegram @BotFather, copy telegram token of your bot to `config.ini`

* Fill other configs.

* Just run
```
python3 main.py
```

* For subscribe TG group to VK group (whic ID you enter in `config.ini`) call
```
/notify_me
```

### Using with Docker

###### Dockefile exmaple
```
FROM python:3.4-alpine

COPY ./anak-bot /anak-bot/
COPY ./file.db /anak-bot/file.db

WORKDIR /anak-bot

RUN pip3 install -r requirements.txt

CMD ["python3", "/anak-bot/Main.py"]
```

### Using with docker-compose
###### docker-compose.yml example
```
version: '3'
services:
  anak-bot:
    build:
      context: .
      dockerfile: ./bot/Dockerfile
    restart: always
    volumes:
      - ./file.db:/anak-bot/file.db
```
If you use docker-compose, remove line with COPY database file in Dockerfile
```
COPY ./file.db /anak-bot/file.db
```
 We use docker-compose volumes instead
```
volumes:
  - ./file.db:/anak-bot/file.db
```