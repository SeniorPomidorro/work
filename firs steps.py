import requests as r

BOT_TOKEN = ""

json = {"chat_id":-471798724,
"text":"мы тут"}

req = r.post('https://api.telegram.org//sendMessage', json=json)
print(req.text)
