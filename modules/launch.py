import gradio as gr
import cv2
from PIL import Image as im
import mediapipe as mp
from mediapipe import ImageFormat
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import matplotlib.pyplot as plt
from mediapipe.tasks.python.vision import FaceLandmarkerResult, FaceLandmarker

from modules.openCV import detector
from modules.openCV.capture import Capture
#
def predict(frame):
#   # data = im.fromarray(frame)
#   # data = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  face_landmarker_result = detector.getResult(frame)
  annotated_image = detector.draw_landmarks_on_image(frame, face_landmarker_result)
#   # print(annotated_image.shape)
#   # print(type(annotated_image))
  return annotated_image
  # return face_landmarker_result
# def annotate(frame, result):
#   annotate_image = detector.draw_landmarks_on_image(frame, result)
#   return annotate_image

with gr.Blocks(live=True) as demo:
  with gr.Row():
    cam = gr.Image(source="webcam", streaming=True)
    output = gr.Image()
    cam.stream(predict, cam, output, show_progress=False)
#   # while (True):
#   #      image = gr.Image(capturer.capture())
#   #      print(image.shape)
#   with gr.Tab("test"):
#     frame = gr.Image(source="webcam", type="numpy", streaming=True)
#     print(frame.shape)
#     if frame.shape is not None:
#       print(frame.shape)
#       frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#       image = mp.Image(image_format=ImageFormat.SRGB, data=frame)
#       face_landmarker_result = detector.getResult(frame)
#
#       annotated_image = detector.draw_landmarks_on_image(frame, face_landmarker_result)
#
#       new_frame = gr.Image(annotated_image)
#   # print(image.shape)
#
# demo.launch()


# img_input = gr.Image(source="webcam", type="numpy", streaming=True)
# img_output = gr.Image(interactive=False, source='upload', streaming=False)
#
# # img_input.stream(predict, inputs=[img_output], outputs=[img_output])
# # gr.Image.stream(annotate, inputs=)
#
# demo = gr.Interface(fn=predict,
#                     inputs=[img_input],
#                     outputs=[img_output], live=True)

demo.launch()