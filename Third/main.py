import smtplib
from dotenv import load_dotenv

email_from = "antony.noone@yandex.ru"
email_to = "antony.noone@yandex.ru"
mail_subject = "Приглашение!"
mail_contentType = """text/plain; charset="UTF-8";"""

message = """

From: antony.noone@yandex.ru
To: antony.noone@yandex.ru
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
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""


friend_name = "friend"
site_name = "https://dvmn.org/profession-ref-program/"
sender_name = "tony"


# print(mail_from, mail_to, mail_subject, mail_contentType, letter.replace("%friend_name%", friend_name).replace("%website%", site_name).replace("%my_name%", sender_name), sep="\n")


message = message.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login()
server.sendmail(email_from, email_to, message)
server.quit()
