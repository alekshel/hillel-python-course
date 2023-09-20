import sqlite3
from faker import Faker
import random

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

fake = Faker(['uk'])
for i in range(100):
    first_name = fake.first_name()
    last_name = fake.last_name()
    cur.execute(
        "INSERT INTO customers (first_name, last_name) VALUES (?, ?)",
        (first_name, last_name)
    )

for i in range(100):
    author = fake.name()
    duration = random.randint(30, 300)
    date_publicated = fake.date()
    cur.execute(
        "INSERT INTO tracks (author, duration, date_publicated) VALUES (?, ?, ?)",
        (author, duration, date_publicated)
    )

connection.commit()
connection.close()
