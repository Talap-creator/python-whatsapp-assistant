import logging
import os

from app import create_app
# В начале вашего файла run.py или внутри функции, которая запускает приложение
from app.database.db import create_table

create_table()
app = create_app()


if __name__ == "__main__":
    logging.info("Flask app started")
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
