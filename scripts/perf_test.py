# -*- coding: utf-8 -*-
"""
Descripttion: 
Author: ZhifeiCheng
Date: 2021-12-15 03:17:13
LastEditors: SijinHuang
LastEditTime: 2021-12-15 03:46:20
"""
import json
import time
from multiprocessing import Pool
import requests
import traceback
from datetime import datetime
import pandas as pd

def load_para():
    with open("config.json", 'r') as f:
        return json.load(f)


def send_request(img_url, end_point, thread_id):
    body = {
        "img_url": img_url
    }
    start_time = time.time()
    response = requests.post(end_point, json=body)
    end_time = time.time()
    # print([thread_id, start_time, end_time, (end_time - start_time), response.text])
    try:
        server_time = json.loads(response.text)['duration']
    except:
        traceback.print_exc()
        server_time = -1
    return {
        'thread_id': thread_id,
        'client_time': (end_time - start_time),
        'server_time': server_time
    }


def run():
    config = load_para()
    if config["target"] == "ecs":
        end_point = config['ecs_endpoint']
    else:
        end_point = config['lambda_endpoint']
    data = [(config["img_url"], end_point, i) for i in range(config["request_number"])]
    with Pool(processes=config["request_number"]) as pool:
        metrics = pool.starmap(send_request, data)
    metrics_df = pd.DataFrame(metrics, columns=['thread_id', 'client_time', 'server_time'])
    metrics_df['experiment_name'] = config['experiment_name']
    print(metrics_df)

    time_str = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    csv_filename = f"{config['experiment_name']}_{time_str}.csv"
    print('Write to ', csv_filename)
    metrics_df.to_csv(csv_filename, index=False)


if __name__ == "__main__":
    run()
