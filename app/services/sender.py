import requests
import json
import os
import time
import random

from app.database.db import save_message
from dotenv import load_dotenv

load_dotenv()
access_token=os.getenv("ACCESS_TOKEN")
# Проверка, что переменная существует
phone_number_id=os.getenv("PHONE_NUMBER_ID")

def send_whatsapp_messages(access_token, phone_number_id, recipients, template_name, language_code):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    url = f'https://graph.facebook.com/v18.0/{phone_number_id}/messages'
    
    for recipient_number in recipients:
        data = {
            "messaging_product": "whatsapp",
            "to": recipient_number,
            "type": "template",
            "template": {
                "name": template_name,
                "language": {
                    "code": language_code
                }
            }
        }
        
        response = requests.post(url, headers=headers, data=json.dumps(data))
        
        if response.status_code == 200:
            print(f'Message sent successfully to {recipient_number}')
            save_message(recipient_number, 'ЖасикВатсап', template_name)
        else:
            print(f'Failed to send message to {recipient_number}: {response.status_code}, {response.text}')

        # Генерируем случайное время паузы от 30 секунд до 5 минут
        sleep_time = random.randint(30, 300)
        print(f'Waiting for {sleep_time} seconds before sending the next message...')
        time.sleep(sleep_time)

    print("All messages have been sent. The script has finished.")
        
# Использование функции
# Твой ID номера телефона
recipients = ['77089452884','77073204940','77018882028','77756986984','77477944157','77014272679']  # Список номеров получателей указывать так ['77089452884','77758327252']
template_name = 'marketing'  # Название твоего шаблона heroku run python app/services/sender.py
language_code = 'ru'  # Код языка для шаблона

send_whatsapp_messages(access_token, phone_number_id, recipients, template_name, language_code)