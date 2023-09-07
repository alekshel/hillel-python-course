from flask import Flask, jsonify
from faker import Faker
import pandas
import requests

INCH_TO_CM = 2.54
POUND_TO_KG = 0.45359237

app = Flask(__name__)

@app.route("/requrements", methods=['GET'])
def get_requirements():
    try:
        with open('requirements.txt', 'rb') as file:
            file_content = file.read()
        return file_content
    except FileNotFoundError:
        return "Файл не знайдено"
    except Exception as e:
        return str(e)
    
@app.route("/generate-users/", methods=['GET'])
@app.route("/generate-users/<int:count>", methods=['GET'])
def generate_users(count = 100):
    fake = Faker(['uk'])
    return jsonify([
        {
            'name': fake.name(),
            'email': fake.email()
        } for i in range(count)
    ])

@app.route("/mean/", methods=['GET'])
def mean_calc():
    file_data = pandas.read_csv('./hw.csv')

    column_height = file_data.columns[1]
    column_weight = file_data.columns[2]

    return jsonify({
        "Середній зріст, см": round(file_data[column_height].mean() * INCH_TO_CM, 2),
        "Середня вага, кг": round(file_data[column_weight].mean() * POUND_TO_KG, 2)
    })

@app.route("/space/", methods=['GET'])
def get_astrons():
    try:
        json = requests.get('http://api.open-notify.org/astros.json').json()
        return jsonify({
            "Кількість космонавтів на поточний момент": json["number"]
        })
    except Exception as e:
        return str(e)