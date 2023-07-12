import gradio as gr
from modules.openCV import capture

capture = capture.Capture

capture.capture()
#
# with gr.Blocks() as demo:
#     video = gr.Video("stream.mp4")
#
# demo.launch()