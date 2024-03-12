import logging
import os

from app import create_app
from app.services.sender import send_bulk_messages

app = create_app()


@app.cli.command("send-messages")
def send_messages_command():
    send_bulk_messages("example.txt")


if __name__ == "__main__":
    logging.info("Flask app started")
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
