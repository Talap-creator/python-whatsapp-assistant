from app.utils.whatsapp_utils import send_whatsapp_message

def send_bulk_messages(file_path):
    with open(file_path, 'r') as file:
        numbers = [line.strip() for line in file.readlines()]

    for number in numbers:
        message = "QQ Epta! This is a test message from the AirBnb Assistant."
        send_whatsapp_message(number, message)
        print(f"Sent message to {number}")