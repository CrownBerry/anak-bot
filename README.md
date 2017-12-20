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
twitchClientId: your twitch client ID, if u want switch bot to Twitch instead of VK
oauthToken: oauth token for Twitch
channelId: id of stream channel
telegramnChannel: Name of TG channel for notify
vkToken: service token VK API
group: VK group ID for subscribing
```

Also you need to install dependencies:
```
pip3 install -r requirements.txt
```

### Using

Just run
```
python3 Main.py
```

For reposting from VK group to telegram chat just add this bot to group member, and call
```
/notify_me
```
