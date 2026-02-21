import gradio as gr

from answer import answer_question  # pyright: ignore[reportMissingImports]

gr.ChatInterface(answer_question, type="messages").launch(inbrowser=True)