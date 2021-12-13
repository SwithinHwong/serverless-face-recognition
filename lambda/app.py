# -*- coding: utf-8 -*-
"""
Descripttion: 
Author: SijinHuang
Date: 2021-12-02 13:58:15
LastEditors: SijinHuang
LastEditTime: 2021-12-13 17:17:04
"""

import json

from common import fetch_img, integrated_face_recog_process


# import insightface
# from insightface.app import FaceAnalysis
# from insightface.data import get_image as ins_get_image

# model = FaceAnalysis(name='buffalo_m', root='./.insightface')
# model.prepare(ctx_id=0, det_size=(640, 640))


def handler(event, context):
    img_url = event['img_url']
    img = fetch_img(img_url)
    matched_res = integrated_face_recog_process(img)
    return json.dumps(matched_res, ensure_ascii=False)
