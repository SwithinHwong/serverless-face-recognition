from face_detection import detect_faces
from face_recognition import recog_faces
from face_match import match_face


def integrated_face_recog_process(img):
    det_res = detect_faces(img)
    recog_res = recog_faces(img, det_res)
    matched_res = match_face(recog_res)
    return matched_res
