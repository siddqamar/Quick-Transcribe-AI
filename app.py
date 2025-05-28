import os
import gradio as gr
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import tempfile
from pathlib import Path


load_dotenv()


client = InferenceClient(token=os.getenv("HF_API_TOKEN"))

def transcribe_media(file):
    """Transcribe audio/video file using Whisper model."""
    if file is None:
        return "Please upload a file first."
    
    try:
        original_name = Path(file.name).stem
        
        result = client.audio.transcription(
            model="openai/whisper-large-v3-turbo",
            file=file.name
        )
        
        # Save transcription to a temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write(result)
            temp_path = f.name
        
        return result, temp_path, original_name
    except Exception as e:
        return f"Error during transcription: {str(e)}", None, None

# Create Gradio interface
with gr.Blocks(title="Quick Transcribe AI") as demo:
    gr.Markdown("# 🎙️ Quick Transcribe AI")
    gr.Markdown("Upload an audio or video file to get its transcription.")
    
    with gr.Row():
        with gr.Column():
            file_input = gr.File(
                label="Upload Audio/Video",
                file_types=["audio/*", "video/*"],
                type="file"
            )
            transcribe_btn = gr.Button("Transcribe")
        
        with gr.Column():
            output_text = gr.Textbox(
                label="Transcription",
                lines=10,
                max_lines=20
            )
            download_btn = gr.File(label="Download Transcript")
    
    # Set up event handlers
    transcribe_btn.click(
        fn=transcribe_media,
        inputs=[file_input],
        outputs=[output_text, download_btn, gr.Textbox(visible=False)]
    )

# Launch the app
if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        inbrowser=True
    ) 