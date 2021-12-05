# -*- coding: utf-8 -*-
"""
Descripttion: 
Author: SijinHuang
Date: 2021-12-02 13:58:15
LastEditors: SijinHuang
LastEditTime: 2021-12-05 01:54:20
"""

import cv2
import sys
import json
import numpy as np
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image

model = FaceAnalysis(name='buffalo_m', root='./.insightface')
model.prepare(ctx_id=0, det_size=(640, 640))


def handler(event, context):
    img = ins_get_image('t1')

    faces = model.get(img)
    assert len(faces)==6

    # then print all-to-all face similarity
    feats = []
    for face in faces:
        feats.append(face.normed_embedding)
    feats = np.array(feats, dtype=np.float32)
    sims = np.dot(feats, feats.T)
    print('Features=')
    print(feats)
    print('Similarities=')
    print(sims)
    return json.dumps(feats.tolist())

