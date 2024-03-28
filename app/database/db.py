import psycopg2
import logging
import os


from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#create table in the database
def create_table():
    conn = connect_db()  # Используем ранее определенную функцию для подключения к БД
    with conn.cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_messages (
            id SERIAL PRIMARY KEY,
            wa_id BIGINT NOT NULL,
            name VARCHAR(255),
            message TEXT NOT NULL,            
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP                       
        );            
        """)        

    conn.commit()  # Зафиксируйте изменения в БД
    conn.close()  # Закройте соединение

# --------------------------------------------------------------
# connect to the database
# --------------------------------------------------------------
def connect_db():
    logging.info("Attempting to connect to the database.")
    DATABASE_URL = os.getenv("DATABASE_URL")
    if DATABASE_URL is None:
        print('DATABASE_URL not found.')
        return None
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        print('Successfully connected to the database.')
        return conn
    except Exception as e:
        print(f'Failed to connect to the database: {e}')
        return None    

#save message to the database    
def save_message(wa_id, name, message):
    conn = connect_db()
    with conn.cursor() as cursor:
        query = """
        INSERT INTO user_messages (wa_id, name, message)
        VALUES (%s, %s, %s);
        """
        cursor.execute(query, (wa_id, name, message))
    conn.commit()
    conn.close()
