# -*- coding: utf-8 -*-
"""
Descripttion: 
Author: SijinHuang
Date: 2021-12-06 21:19:11
LastEditors: SijinHuang
LastEditTime: 2021-12-13 21:39:29
"""
import json
import numpy as np
import insightface
from insightface.data import get_image as ins_get_image

from common.dao import fetch_img

detection_model = insightface.model_zoo.get_model('./.insightface/models/buffalo_m/det_2.5g.onnx')
detection_model.prepare(ctx_id=0, input_size=(640, 640), det_thresh=0.5)

def detect_faces(img):
    bboxes, kpss = detection_model.detect(img, max_num=0)
    if bboxes.shape[0] == 0:
        return []
    ret = []
    for i in range(bboxes.shape[0]):
        bbox = bboxes[i, 0:4]
        det_score = bboxes[i, 4]
        kps = None
        if kpss is not None:
            kps = kpss[i]
        det_obj = {
            'bbox': bbox.tolist(),
            'kps': kps.tolist(),
            'det_score': float(det_score),
        }
        ret.append(det_obj)
    return ret


def handler(event, context):
    img_url = event['img_url']
    img = fetch_img(img_url)
    det_res = detect_faces(img)
    return json.dumps(det_res, ensure_ascii=False)
