import gradio as gr
import redis
import numpy as np
from modules.openCV import detector
import pickle

r = redis.Redis(host='localhost', port=6379, db=0)

def predict(frame):
  global width, height
  width = frame.shape[0]
  height = frame.shape[1]
#   # data = im.fromarray(frame)
#   # data = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  face_landmarker_result = detector.getResult(frame)
  # byte_result = bytearray(face_landmarker_result)
  result = pickle.dumps(face_landmarker_result.face_landmarks)
  r.set('current_result', result)
  #annotated_image = detector.draw_landmarks_on_image(frame, face_landmarker_result)
  black_frame = np.zeros_like(frame)
  mesh_only = detector.draw_landmarks_on_image(black_frame, face_landmarker_result, width, height)
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

def capture(frame):
  initial_result = detector.getResult(frame)
  # byte_init_result = bytearray(initial_result)
  results = pickle.dumps(initial_result.face_landmarks)
  r.set('first_result', results)

  # initial_annotated_image = detector.draw_landmarks_on_image(frame, initial_result, width, height)
  return initial_result

with gr.Blocks() as demo:
  with gr.Column() as img_block:
    with gr.Row():
      # init_values = snap.capture()
      # print(init_values)
      cam = gr.Image(source="webcam", streaming=True, visible=True)
      output = gr.Image()
      # mesh = gr.Image()
      cam.stream(predict, cam, output, show_progress=False)
  with gr.Column():
    mode = gr.Dropdown(["Stream & Mesh", "Mesh only"], interactive=True)
    snap = gr.Button("Press to take initial photo of relaxed face for a benchmark")
    init_values = gr.Textbox(visible=False)
    snap.click(capture, cam, init_values)
  mode.change(change_layout, mode, cam)


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