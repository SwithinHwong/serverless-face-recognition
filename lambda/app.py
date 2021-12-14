# -*- coding: utf-8 -*-
"""
Descripttion: 
Author: SijinHuang
Date: 2021-12-02 13:58:15
LastEditors: SijinHuang
LastEditTime: 2021-12-15 04:02:42
"""

import json
import time

from common.dao import fetch_img
from common.integration import integrated_face_recog_process


# import insightface
# from insightface.app import FaceAnalysis
# from insightface.data import get_image as ins_get_image

# model = FaceAnalysis(name='buffalo_m', root='./.insightface')
# model.prepare(ctx_id=0, det_size=(640, 640))


def handler(event, context):
    ts_start = time.time()
    img_url = event['img_url']
    img = fetch_img(img_url)
    matched_res = integrated_face_recog_process(img)
    ts_end = time.time()
    res = {
        'result': matched_res,
        'duration': (ts_end - ts_start),  # server time
    }
    return res
