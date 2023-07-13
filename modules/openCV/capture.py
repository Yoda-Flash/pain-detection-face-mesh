import cv2
import gradio as gr

class Capture:
  def __init__(self):
    self.cap = cv2.VideoCapture(0)

  # @staticmethod
  def capture(self):
    # cap = cv2.VideoCapture(0)
    #
    # width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # writer= cv2.VideoWriter('stream.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, (width,height))

    ret, frame = self.cap.read()

    # writer.write(frame)

    # cap.release()
    # writer.release()

    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # cv2.destroyAllWindows()

    return frame