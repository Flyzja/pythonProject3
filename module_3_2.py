
def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    substring = "@"
    substring1 = ".com", ".ru", ".net"
    if substring not in recipient and substring not in sender:
        if substring1 not in recipient and substring1 not in sender:
            print(f"Невозможно отправить письмо с адреса {sender}>на адрес {recipient}")
    elif recipient == "university.help@gmail.com":
        print("Нельзя отправить письмо самому себе!")
    elif recipient == 'mamontova-75@mail.ru':
        print(f"Письмо успешно отправлено с адреса{sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо не отправлено с адреса {sender} на адрес {recipient}.")
    return recipient


result = send_email('Здравствуй, студент, cкоро ты познаешь Python!!!','urban.teacher@mail.uk')
send_email('Здравствуй, студент, cкоро ты познаешь Python!!!','university.help@mail.com')
send_email('Здравствуй, студент, cкоро ты познаешь Python!!!','mamontova-75@mail.ru')
send_email('Здравствуй, студент, cкоро ты познаешь Python!!!',"university.student@gmail.com")


