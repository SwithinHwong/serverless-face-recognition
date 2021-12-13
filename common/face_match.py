# -*- coding: utf-8 -*-
"""
Description: 
Author: SijinHuang
Date: 2021-12-13 13:24:32
LastEditors: SijinHuang
LastEditTime: 2021-12-13 13:49:03
"""
import json
import numpy as np
import pandas as pd

from dao import fetch_img

df_gallery = pd.read_csv('./data/gallery_urls.csv')
gallery_names = df_gallery['name'].values.tolist()
gallery_urls = df_gallery['url'].values.tolist()
gallery_embs = np.load('./data/gallery_embeddings.npy')


def match_face(recog_res):
    matched_res = []
    for recog_obj in recog_res:
        bbox = np.array(recog_obj['bbox'])
        kps = np.array(recog_obj['kps'])
        det_score = recog_obj['det_score']
        embedding = recog_obj['embedding']
        sims = np.dot(embedding, gallery_embs.T)
        max_prob_idx = sims.argmax()
        max_prob = float(sims.max())
        match_obj = {
            'bbox': recog_obj['bbox'],
            'kps': recog_obj['kps'],
            'det_score': recog_obj['det_score'],
            'recog_name': gallery_names[max_prob_idx],
            'recog_similarity': max_prob,
            'recog_gallery_url': gallery_urls[max_prob_idx]
        }
        matched_res.append(match_obj)
    return matched_res

def handler(event, context):
    # img_url = event['img_url']
    # img = fetch_img(img_url)
    recog_res = json.loads(event['recog_res'])
    matched_res = match_face(recog_res)
    return json.dumps(matched_res, ensure_ascii=False)
