# -*- coding: utf-8 -*-
"""
Descripttion: 
Author: ZhifeiCheng
Date: 2021-12-13 21:37:17
LastEditors: SijinHuang
LastEditTime: 2021-12-13 21:40:29
"""
from common.face_detection import detect_faces
from common.face_recognition import recog_faces
from common.face_match import match_face


def integrated_face_recog_process(img):
    det_res = detect_faces(img)
    recog_res = recog_faces(img, det_res)
    matched_res = match_face(recog_res)
    return matched_res
