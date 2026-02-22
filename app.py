import gradio as gr

def greet(name):
    return f"Hello {name}, Neo Finance Assistant is initializing..."

iface = gr.Interface(
    fn=greet,
    inputs="text",
    outputs="text",
    title="Neo - Finance AI Assistant"
)

if __name__ == "__main__":
    iface.launch()
