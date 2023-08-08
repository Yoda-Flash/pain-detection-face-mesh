import gradio as gr
import redis
import numpy as np
from detector import detector, getResult, draw_landmarks_on_image
import pickle
from athena import Pain
from config import REDIS_HOST

r = redis.Redis(host=REDIS_HOST, port=6379, db=0)

pain_detection = Pain()
def init(value):
  # print(f"value: {value}")
  value = 1
  return value

def predict(num, frame):
  try:
    if num == 1:
      global width, height
      width = frame.shape[0]
      height = frame.shape[1]
    #   # data = im.fromarray(frame)
    #   # data = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      face_landmarker_result = getResult(frame)
      # print(face_landmarker_result.face_landmarks)
      # byte_result = bytearray(face_landmarker_result)
      # result = pickle.dumps(face_landmarker_result.face_landmarks)
      # r.set('current_result', result)
      #annotated_image = detector.draw_landmarks_on_image(frame, face_landmarker_result)
      black_frame = np.zeros_like(frame)
      pain_result = pain_detection.detection(face_landmarker_result.face_landmarks[0])
      mesh_only = draw_landmarks_on_image(black_frame, face_landmarker_result, width, height, pain_result)
    #   # print(annotated_image.shape)
    #   # print(type(annotated_image))
      return mesh_only
    return
  except Exception as e:
    print(e)
    raise gr.Error(e)
  # else:
  #   return None
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
  try:
    initial_result = getResult(frame)
    # byte_init_result = bytearray(initial_result)
    results = pickle.dumps(initial_result.face_landmarks)
    r.set('first_result', results)
    #initial_annotated_image = detector.draw_landmarks_on_image(frame, initial_result, width, height, null)
    return initial_result
  except Exception as e:
    print(e)
    raise gr.Error(e)

with gr.Blocks() as demo:
  with gr.Column() as img_block:
    with gr.Row():
      # init_values = snap.capture()
      # print(init_values)
      cam = gr.Image(source="webcam", streaming=True, visible=True)
      output = gr.Image()
      # mesh = gr.Image()
      #cam.stream(predict, cam, output, show_progress=False)
  with gr.Column():
    mode = gr.Dropdown(["Stream & Mesh", "Mesh only"], interactive=True, type="value")
    snap = gr.Button("Press to take initial photo of relaxed face for a benchmark")
    start = gr.Button("Press to start operation")
    init_values = gr.Textbox(visible=False)
    num = gr.Number(visible=False, value=0)
    print(f"Num: {num.value}")
    cam.stream(predict, inputs=[num, cam], outputs=[output], show_progress=False)
    snap.click(capture, inputs=cam, outputs=init_values)
    start.click(init, inputs=num, outputs=num)
    # start.click(cam.stream(predict, cam, output, show_progress=False))
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
demo.launch(server_name="0.0.0.0", server_port=7860)