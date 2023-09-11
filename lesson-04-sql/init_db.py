import sqlite3
from faker import Faker
import random

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

fake = Faker(['uk'])
for i in range(8):
    first_name = fake.first_name()
    last_name = fake.last_name()
    cur.execute(
        "INSERT INTO customers (first_name, last_name) VALUES (?, ?)",
        (first_name, last_name)
    )

cur.execute(
    "INSERT INTO customers (first_name, last_name) VALUES (?, ?)",
    ("Олена", "Остапчук")
)

cur.execute(
    "INSERT INTO customers (first_name, last_name) VALUES (?, ?)",
    ("Олена", "Дзюба")
)

for i in range(100):
    song_name = fake.catch_phrase()
    duration = random.randint(30, 300)
    cur.execute(
        "INSERT INTO tracks (name, duration) VALUES (?, ?)",
        (song_name, duration)
    )

connection.commit()
connection.close()
