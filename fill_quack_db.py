import psycopg2
import psycopg2.extras
from datetime import datetime
from fill_quack_db_config import *
import factory

def main():
    conn = psycopg2.connect(f"dbname={DB_NAME} user={DB_USER} host='localhost' password={DB_PASSWORD}")
    cur = conn.cursor
    for i in range(5):
        username = factory.Faker('user_name')
        name = f'{factory.Faker("first_name")} {factory.Faker("last_name")}'
        cur.execute('INSERT INTO users (username, name) VALUES (%s, %s)', (username, name))
    cur.close()
    conn.close()
