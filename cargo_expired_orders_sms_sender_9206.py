import suptech
import re

token = 'AgAEA7qi5P2DAAWyGQcjt8EvqEefoirz8C3VdDM'
org_id = '650580'
query = 'queue: SUPPARTNERS tags: !sms_send_new tags: cargo_expired_order'
tracker = suptech.Tracker(token, org_id)
tickets = [x['key'] for x in tracker.search_issues(query)]


def parsing_text(text):
    text = re.sub("\r", "\n", text)
    full_sms_text = ""
    validator = False
    sms_array_return = []
    array_lines = text.split("\n")
    lock_sms = False
    lock_promo = False
    for data in array_lines:
        if data is None:
            continue
        if data.strip() in ['sms', u'смс'] and not lock_sms:
            lock_sms = True
            validator = True
            continue
        if lock_sms and data.strip() != "promo" and data.strip() not in ['sms', u'смс']:
            full_sms_text += data
        if data.strip() in "promo":
            lock_sms = False
            lock_promo = True
            continue
        if lock_promo and data.strip() not in "promo":
            sms_array_return.append({"text": data})
            lock_promo = False
    sms_array_return.append({"text": full_sms_text})
    return sms_array_return, validator


temp_sms = 'У вас завис заказ. Мы пытались дозвониться, чтобы разобраться с этим, но не смогли. Пожалуйста, не пропускайте наш следующий звонок.'
data = []
bad_tickets = []
for ticket in tickets:
    reversed_comments = reversed(tracker.get_issues_comments(ticket))
    for message in reversed_comments:
        if message['transport'] == 'email':
            target_message = parsing_text(message['email']['text'])
            if target_message[1] and target_message[0][-1]['text'] != temp_sms:
                data.append(['смс\n' + target_message[0][-1]['text'], ticket])
            else:
                bad_tickets.append(ticket)

print(data, bad_tickets)


for text in data:
    request = tracker.update_issue(data= {
            "comment": {
                "text": "{}".format(text[0])
            },
            "SendLastCommentAsSms": "Выбрано",
            'kategoria': ['Водитель'],
            "brand": "yandex"
        }, issue_id='{}'.format(text[1]))
    print(request)

