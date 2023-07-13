import gradio as gr

with gr.Blocks() as demo:
    image = gr.Image(source = "webcam", streaming = True, live = True)


demo.launch()