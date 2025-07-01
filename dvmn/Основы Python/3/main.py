import smtplib
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

friend_name = "friend"
site_name = "https://dvmn.org/profession-ref-program/"
sender_name = "tony"
email_from = 'antony.noone@yandex.ru'
email_to = 'tony.noone@yandex.ru'

letter = """\
From: {email_from}
To: {email_to}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format(email_from=email_from, email_to=email_to)

letter = letter.replace("%friend_name%", friend_name).replace("%website%", site_name).replace("%my_name%", sender_name)
letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(os.environ['EMAIL_LOGIN'], os.environ['EMAIL_PASS'])
server.sendmail(email_from, email_to, letter)
server.quit()