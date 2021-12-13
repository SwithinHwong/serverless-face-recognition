# -*- coding: utf-8 -*-
"""
Descripttion: 
Author: SijinHuang
Date: 2021-12-02 13:58:15
LastEditors: SijinHuang
LastEditTime: 2021-12-13 15:20:48
"""

import cv2
import sys
import json
import numpy as np

from dao import fetch_img
from face_detection import detect_faces
from face_recognition import recog_faces
from face_match import match_face

# import insightface
# from insightface.app import FaceAnalysis
# from insightface.data import get_image as ins_get_image

# model = FaceAnalysis(name='buffalo_m', root='./.insightface')
# model.prepare(ctx_id=0, det_size=(640, 640))

def integrated_face_recog_process(img):
    det_res = detect_faces(img)
    recog_res = recog_faces(img, det_res)
    matched_res = match_face(recog_res)


def handler(event, context):
    img_url = event['img_url']
    img = fetch_img(img_url)
    matched_res = integrated_face_recog_process(img)
    return json.dumps(matched_res, ensure_ascii=False)
