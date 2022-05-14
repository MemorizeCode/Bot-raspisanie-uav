
import time
from time import time
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

import requests
from bs4 import BeautifulSoup

vk_session = vk_api.VkApi(token = 'VK TOKEN')
ses_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)



help_cmd = ['настройки', 'Настройки' , 'НАСТРОЙКИ', 'помоги', '/help']


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg =  event.text.lower()
            id = event.user_id
            if msg in help_cmd:
                vk_session.method('messages.send' , {'user_id' : id, 'message' : 'Напишите цифру\n1)21ис-3\n2)Автор\n3)Исходники\n\n\nБот может внезапно упасть от большой нагрузки или сам по себе \nРабота с 10:00 по 14:00 где-то', 'random_id' : 0})
            if msg == '1':
                r = requests.post('https://uaviak.ru/pages/raspisanie-/#pos2')
                soup = BeautifulSoup(r.text, 'html.parser')
                ras = soup.find('div', class_="scrolling-text pos2").text.split('\n')
                das = soup.find('div', class_="scrolling-text pos2").text.split('\n')
                parameters = []
                for ur in ras:
                    if ur.find('21ис-3') >=0:
                        parameters.append(ur)
                full_ras = '\n'.join(parameters)
                parameters_d = []
                for ul in das:
                    if ul.find('Расписание')>=0:
                        parameters_d.append(ul)
                full_d = '\n'.join(parameters_d)
                vk_session.method('messages.send' , {'user_id' : id, 'message' : full_ras, 'random_id' : 0})
            if msg == '2':
                vk_session.method('messages.send' , {'user_id' : id, 'message' : 'https://vk.com/mr_4iter_pro', 'random_id' : 0})
            if msg == '3':
                vk_session.method('messages.send' , {'user_id' : id, 'message' : '-------', 'random_id' : 0})










