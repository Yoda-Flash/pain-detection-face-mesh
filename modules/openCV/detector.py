import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe import solutions
from mediapipe import ImageFormat
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import matplotlib.pyplot as plt
import cv2
import time

modelPath = "./face_landmarker.task"
# img_path = "opencv_frame_0.png"
# cv2_image = cv2.imread(img_path)

# image = mp.Image(image_format=ImageFormat.SRGB, data=cv2_image)

# baseOptions = mp.tasks.python.
faceLandmarker = mp.tasks.vision.FaceLandmarker
faceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions
visionRunningMode = mp.tasks.vision.RunningMode

base_options = python.BaseOptions(model_asset_path=modelPath)

options = faceLandmarkerOptions(
  base_options=base_options,
  running_mode=visionRunningMode.IMAGE)

detector = vision.FaceLandmarker.create_from_options(options)
def getResult(image):
  # with faceLandmarker.create_from_options(options) as landmarker:
  frame = mp.Image(image_format=ImageFormat.SRGB, data=image)
  result = detector.detect(frame)
  # print(result)
  return result



# print(face_landmarker_result)

def draw_landmarks_on_image(rgb_image, detection_result):
  face_landmarks_list = detection_result.face_landmarks
  annotated_image = np.copy(rgb_image)
  # Loop through the detected faces to visualize.
  for idx in range(len(face_landmarks_list)):
    face_landmarks = face_landmarks_list[idx]

    # Draw the face landmarks.
    face_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
    face_landmarks_proto.landmark.extend([
      landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in face_landmarks
    ])

    solutions.drawing_utils.draw_landmarks(
      image=annotated_image,
      landmark_list=face_landmarks_proto,
      connections=mp.solutions.face_mesh.FACEMESH_TESSELATION,
      landmark_drawing_spec=None,
      connection_drawing_spec=mp.solutions.drawing_styles
      .get_default_face_mesh_tesselation_style())

    solutions.drawing_utils.draw_landmarks(
      image=annotated_image,
      landmark_list=face_landmarks_proto,
      connections=mp.solutions.face_mesh.FACEMESH_CONTOURS,
      landmark_drawing_spec=None,
      connection_drawing_spec=mp.solutions.drawing_styles
      .get_default_face_mesh_contours_style())

    solutions.drawing_utils.draw_landmarks(
      image=annotated_image,
      landmark_list=face_landmarks_proto,
      connections=mp.solutions.face_mesh.FACEMESH_IRISES,
      landmark_drawing_spec=None,
      connection_drawing_spec=mp.solutions.drawing_styles
      .get_default_face_mesh_iris_connections_style())
  return annotated_image

def plot_face_blendshapes_bar_graph(face_blendshapes):
  # Extract the face blendshapes category names and scores.
  face_blendshapes_names = [face_blendshapes_category.category_name for face_blendshapes_category in face_blendshapes]
  face_blendshapes_scores = [face_blendshapes_category.score for face_blendshapes_category in face_blendshapes]
  # The blendshapes are ordered in decreasing score value.
  face_blendshapes_ranks = range(len(face_blendshapes_names))

  fig, ax = plt.subplots(figsize=(12, 12))
  bar = ax.barh(face_blendshapes_ranks, face_blendshapes_scores, label=[str(x) for x in face_blendshapes_ranks])
  ax.set_yticks(face_blendshapes_ranks, face_blendshapes_names)
  ax.invert_yaxis()

  # Label each bar with values
  for score, patch in zip(face_blendshapes_scores, bar.patches):
    plt.text(patch.get_x() + patch.get_width(), patch.get_y(), f"{score:.4f}", va="top")

  ax.set_xlabel('Score')
  ax.set_title("Face Blendshapes")
  plt.tight_layout()
  plt.show()

# annotated_image = draw_landmarks_on_image(cv2_image, face_landmarker_result)
# cv2.imwrite("annotated_image.png", annotated_image)
