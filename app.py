import requests
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from datetime import datetime, timedelta

app = Flask(__name__)

# MySQL Config
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'payment_iae'
# app.config['MYSQL_PORT'] = 3306
# mysql = MySQL(app)

# Create Tables
# @app.before_first_request
# def create_tables():
#     pass

# Endpoint 1 - GET All Payment Types
@app.route('/test', methods=['GET'])
def get_all_payment_type():
    return jsonify({'status': False, 'status_code': 400,'message': 'Bad request!', 'timestamp' : datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

if __name__ == '__main__':
    app.run(debug=True)