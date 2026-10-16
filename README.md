<html>
	<head>
		<script type="module" crossorigin src="https://cdn.jsdelivr.net/npm/@gradio/lite/dist/lite.js"></script>
		<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@gradio/lite/dist/lite.css" />
	</head>
	<body>
		<gradio-lite>
			<gradio-requirements>
				huggingface-hub==0.34.4
			</gradio-requirements>
			<gradio-file name="app.py" entrypoint>
				import gradio as gr

				def greet(name):
					return "Hello, " + name + "!"

				gr.Interface(greet, "textbox", "textbox").launch()
			</gradio-file>
		</gradio-lite>
	</body>
</html>
