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
  #annotated_image = detector.draw_landmarks_on_image(frame, face_landmarker_result)
  black_frame = np.zeros_like(frame)
  mesh_only = detector.draw_landmarks_on_image(black_frame, face_landmarker_result)
#   # print(annotated_image.shape)
#   # print(type(annotated_image))
  return mesh_only
  # return face_landmarker_result
# def annotate(frame, result):
#   annotate_image = detector.draw_landmarks_on_image(frame, result)
#   return annotate_image

def change_layout(value):
  if value == "Stream & Mesh":
    return cam.update(visible=True)
  elif value == "Mesh only":
    return cam.update(visible=False)
  # elif value == "Mesh only":

# def get_mesh_only(frame, result):
#   img = np.zeros_like(fram)

def capture(frame):
  initial_result = detector.getResult(frame)
  initial_annotated_image = detector.draw_landmarks_on_image(frame, initial_result)
  return initial_annotated_image

init_values = []

with gr.Blocks() as demo:
  with gr.Column() as img_block:
    with gr.Row():
      snap = gr.Image(source="webcam", type="numpy", streaming=False, visible=False)
      # init_values = snap.capture()
      # print(init_values)
      cam = gr.Image(source="webcam", streaming=True, visible=True)
      output = gr.Image()
      # mesh = gr.Image()
      cam.stream(predict, cam, output, show_progress=False)
  with gr.Column():
    mode = gr.Dropdown(["Stream & Mesh", "Mesh only"], interactive=True)
    value = mode.value
  mode.change(change_layout, mode, cam)
  snap.change(capture, snap, init_values)

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

def get_init_coord():
  return init_values