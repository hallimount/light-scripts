#                  created by hz-kto-ya
# Отправка сообщений по GMAIL 

import smtplib                                    


try:                
    server = smtplib.SMTP("smtp.gmail.com", 587)    #connection
    server.ehlo()
    server.starttls()
    print("SERVER CONNECTED")
except:
    print("Could Not connect to Gmail")             #failure 

user = input("Отправитель\n")                 # !!!!!!!!!!!!!!!!! ОТПРАВИТЕЛЬ !!!!!!!!
Pass_w = input("\nПароль\n")                 # !!!!!!!!!!!!!!!!!!! ПАРОЛЬ!!!!!!!!!!
reciever_id = input("\nПолучатель id\n")      # !!!!!!!!!!!!!!!!!! ПОЛУЧАТЕЛЬ !!!!!!!!!!
msg = input("\nСообщение\n")                 # !!!!!!!!!!!!!!!!!СООБЩЕНИЕ !!!!!!!!!!!

try:
    server.login(user, Pass_w)                      # log in
    print("Logged in")
except:
    print("Нужно настроить настройки безопастности для отправки сообщения")
    server.quit()
    exit()

server.sendmail(user, reciever_id, msg)
print("MAIL sent")                                  #confirmation


print("Closing Connection")
server.quit()                                       #closing connection
print("Server closed")
