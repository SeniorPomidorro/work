import requests as r

BOT_TOKEN = "800123310:AAEqhwlZNivTsfGCf6s0tSjC-6X23Z5SwaU"

json = {"chat_id":-471798724,
"text":"мы тут"}

req = r.post('https://api.telegram.org/bot800123310:AAEqhwlZNivTsfGCf6s0tSjC-6X23Z5SwaU/sendMessage', json=json)
print(req.text)