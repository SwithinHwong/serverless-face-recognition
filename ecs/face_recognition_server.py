import http.server as http_server
import logging
from integration import integrated_face_recog_process
from dao import fetch_img
import sys
# sys.path.insert('../common')
import json


class FaceRecognitionServer(http_server.BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        req = json.loads(post_data)
        image_url = req["img_url"]
        logging.info(f'img_url is {image_url}')
        img = fetch_img(img_name=image_url)
        logging.info(f'img is {img}')
        matched_res = integrated_face_recog_process(img)
        logging.info(f'mathed_res {matched_res}')
        logging.info("233333")
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(matched_res).encode("UTF-8"))


PORT = 10086


def run():
    logging.basicConfig(level=logging.INFO)
    server_address = ('', PORT)
    server = http_server.HTTPServer(server_address, FaceRecognitionServer)
    server.serve_forever()


if __name__ == "__main__":
    run()
