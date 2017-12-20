# Anak Bot

VK-to-Telegram notifier bot.

## Getting Started

You can use this bot with any VK group you want, but now group ID hardcoded in `config.ini` file

### Configuring

You can use your own config with this project.

Config.ini example

```
[DEFAULT]
tgToken: your telegram token
telegramnChannel: Name of TG channel for notify
vkToken: service token VK API
group: VK group ID for subscribing
connectionString: sqlite:///file.db # path to sqlite3 database file
```

Also you need to install dependencies:
```
pip3 install -r requirements.txt
```

### Using

*Create bot with telegram @BotFather, copy telegram token of your bot to `config.ini`

*Fill other configs.

*Just run
```
python3 Main.py
```

*For subscribe TG group to VK group (whic ID you enter in `config.ini`) call
```
/notify_me
```
