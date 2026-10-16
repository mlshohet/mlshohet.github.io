<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>Gradio Lite Fix</title>
    <!-- 1. Load Pyodide and Micropip manually before Gradio loads -->
    <script src="https://jsdelivr.net"></script>
    
    <!-- 2. Lock Gradio Lite to a version that doesn't trigger the dependency loop -->
    <script type="module" crossorigin src="https://jsdelivr.net"></script>
    <link rel="stylesheet" href="https://jsdelivr.net" />
</head>
<body>

<script>
async function initPyodideFix() {
    // Force install a pure-python wheel directly into the browser context
    let pyodide = await loadPyodide();
    await pyodide.loadPackage("micropip");
    const micropip = pyodide.pyvars.get("micropip");
    
    // Explicitly install a pure wheel before Gradio's internal loader triggers
    await pyodide.runPythonAsync(`
        import micropip
        try:
            # Inject a known pure Python wheel version
            await micropip.install('huggingface-hub==0.24.0') 
        except Exception as e:
            print("Pre-install log:", e)
    `);
}
initPyodideFix();
</script>

<!-- 3. Your standard Gradio App inside the HTML body -->
<gradio-lite>
<gradio-file name="app.py" entrypoint>
import gradio as gr

def process_input(text):
    return f"Gradio Lite Browser Output: {text}"

demo = gr.Interface(fn=process_input, inputs="text", outputs="text")
demo.launch()
</gradio-file>
</gradio-lite>

</body>
</html>
