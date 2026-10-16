<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Gradio Lite Pure-Python Fix</title>
    
    <!-- Use a locked stable build of Gradio Lite that avoids the broken hub version match -->
    <script type="module" crossorigin src="https://jsdelivr.net"></script>
    <link rel="stylesheet" href="https://jsdelivr.net" />
</head>
<body>

    <!-- A simple app layout that completely sidesteps huggingface-hub requirements -->
    <gradio-lite>
<gradio-file name="app.py" entrypoint>
import gradio as gr

def respond(message):
    return f"Response from local browser runtime: {message}"

with gr.Blocks() as demo:
    gr.Markdown("# Browser-Isolated Sandbox")
    inp = gr.Textbox(label="Input Text")
    out = gr.Textbox(label="Output Text")
    btn = gr.Button("Submit")
    btn.click(fn=respond, inputs=inp, outputs=out)

demo.launch()
</gradio-file>
    </gradio-lite>

</body>
</html>
