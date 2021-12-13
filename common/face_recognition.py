# -*- coding: utf-8 -*-
"""
Descripttion: 
Author: SijinHuang
Date: 2021-12-06 21:19:11
LastEditors: SijinHuang
LastEditTime: 2021-12-13 14:04:30
"""
import json
import numpy as np
import insightface

from dao import fetch_img

recognition_model = insightface.model_zoo.get_model('./.insightface/models/buffalo_m/w600k_r50.onnx')
recognition_model.prepare(ctx_id=0)

def recog_faces(img, det_res):
    ret = []
    for det_obj in det_res:
        bbox = np.array(det_obj['bbox'])
        kps = np.array(det_obj['kps'])
        det_score = det_obj['det_score']
        face = insightface.app.common.Face(bbox=bbox, kps=kps, det_score=det_score)
        recognition_model.get(img, face)
        # ret.append(face)
        det_obj['embedding'] = face.normed_embedding.tolist()
        ret.append(det_obj)
    return ret


def handler(event, context):
    img_url = event['img_url']
    img = fetch_img(img_url)
    det_res = json.loads(event['det_res'])
    recog_res = recog_faces(img, det_res)
    return json.dumps(recog_res, ensure_ascii=False)

