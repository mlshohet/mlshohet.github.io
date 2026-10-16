<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>Gradio Lite Stable</title>
    <!-- Locked to an older version that entirely predates the huggingface-hub 0.33 problem -->
    <script type="module" crossorigin src="https://jsdelivr.net"></script>
    <link rel="stylesheet" href="https://jsdelivr.net" />
</head>
<body>

<gradio-lite>
<gradio-file name="app.py" entrypoint>
import gradio as gr

def greet(name):
    return f"Hello {name}!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch()
</gradio-file>
</gradio-lite>

</body>
</html>
