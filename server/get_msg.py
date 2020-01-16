#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask
from flask import jsonify
# from flask_cors import CORS

app = Flask(__name__)
# cors = CORS(app, resources={r"/getMsg": {"origins": "*"}})

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/getMsg', methods=['GET', 'POST'])
def home():
    response = {
        'msg': 'Hello, Python !'
    }
    return jsonify(response)

# ��������
if __name__ == '__main__':
    app.run()   # �����ӻ�ֱ�������ڱ��ط�������Ҳ���� localhost:5000
   # app.run(host='your_ip_address') # �����ͨ�� host ָ���ڹ���IP������