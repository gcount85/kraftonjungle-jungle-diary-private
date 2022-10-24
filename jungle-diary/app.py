import requests
from flask import Flask, request, render_template, jsonify, make_response 
from pymongo import MongoClient 
from bs4 import BeautifulSoup
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)
# app.config["TEMPLATES_AUTO_RELOAD"] = True
# app.config['UPLOAD_FOLDER'] = "./static/profile_pics"

admin_id = "Minsu"
admin_pw = "123456"
SECRET_KEY = 'apple'

# client = MongoClient('mongodb://13.124.117.232', 27017, username="test", password="test")  # aws연결
client = MongoClient('localhost', 27017)  # 로컬연결
db = client.db_jungle_local




@app.route("/login", methods=['POST'])
def login_proc():
	print(request.form)
	input_data = request.form
	user_id = input_data['id']
	user_pw = input_data['pw']

	# 아이디, 비밀번호가 일치하는 경우
	if (user_id == admin_id and
			user_pw == admin_pw):
		payload = {
			'id': user_id,
			'exp': datetime.utcnow() + timedelta(seconds=60)  # 로그인 24시간 유지
		}
		token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

		return jsonify({'result': 'success', 'token': token})


	# 아이디, 비밀번호가 일치하지 않는 경우
	else:
		return jsonify({'result': 'fail'})