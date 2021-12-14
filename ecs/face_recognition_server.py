import http.server as http_server
import multiprocessing
import logging
import time
from common.integration import integrated_face_recog_process
from common.dao import fetch_img
import json


class FaceRecognitionServer(http_server.BaseHTTPRequestHandler):
    def do_GET(self):
        logging.info(f'url path is {self.path}')
        if self.path == "/health":
            logging.info("healthcheck....")
            self.send_response(200)
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        start_time = time.time()
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        req = json.loads(post_data)
        image_url = req["img_url"]
        logging.info(f'img_url is {image_url}')
        img = fetch_img(img_name=image_url)
        logging.info(f'img is {img}')
        matched_res = integrated_face_recog_process(img)
        logging.info(f'mathed_res {matched_res}')
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.end_headers()
        end_time = time.time()
        output = {
            "result": matched_res,
            "duration": end_time - start_time,
            'cpu_cores': multiprocessing.cpu_count,
        }
        self.wfile.write(json.dumps(output).encode("UTF-8"))


PORT = 10086


def run():
    logging.basicConfig(level=logging.INFO)
    server_address = ('0.0.0.0', PORT)
    server = http_server.HTTPServer(server_address, FaceRecognitionServer)
    server.serve_forever()


if __name__ == "__main__":
    run()
