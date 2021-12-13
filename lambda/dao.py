# -*- coding: utf-8 -*-
"""
Descripttion: 
Author: SijinHuang
Date: 2021-12-13 13:13:18
LastEditors: SijinHuang
LastEditTime: 2021-12-13 14:30:18
"""
import os
import urllib
from urllib.request import urlopen
from pathlib import Path
import cv2
import numpy as np

# local_img_dir = Path(os.environ['IMAGE_DIR'])
local_img_dir = Path('./data/imgs/query_imgs/')


def url_to_image(url, readFlag=cv2.IMREAD_COLOR):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, readFlag)
    return image


def load_local_img(filename: str) -> np.ndarray:
    return cv2.imread(str(local_img_dir / filename))


def fetch_img(img_name: str) -> np.ndarray:
    if img_name.startswith('local:'):
        img_fn = img_name[6:]  # remove "local:"
        return load_local_img(img_fn)
    else:
        return url_to_image(img_name)
