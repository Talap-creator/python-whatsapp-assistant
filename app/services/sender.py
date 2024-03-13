import requests
import json
import os
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
        else:
            print(f'Failed to send message to {recipient_number}: {response.status_code}, {response.text}')

# Использование функции
# Твой ID номера телефона
recipients = ['77089452884', '77758327252', '77054430621']  # Список номеров получателей
template_name = 'hello_world'  # Название твоего шаблона
language_code = 'en_US'  # Код языка для шаблона

send_whatsapp_messages(access_token, phone_number_id, recipients, template_name, language_code)