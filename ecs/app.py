# -*- coding: utf-8 -*-
"""
Descripttion: 
Author: SijinHuang
Date: 2021-12-13 22:01:52
LastEditors: SijinHuang
LastEditTime: 2021-12-13 22:41:02
"""
from flask import Flask, request, jsonify
import numpy as np

from common.dao import fetch_img
from common.integration import integrated_face_recog_process

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World!"


@app.route('/predict',methods=['POST'])
def predict_integrated():
    img_url = request.json["img_url"]
    img = fetch_img(img_url)
    matched_res = integrated_face_recog_process(img)
    return jsonify(matched_res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10086, debug = True)
